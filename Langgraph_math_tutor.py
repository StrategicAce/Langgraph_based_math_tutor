import os
from pprint import pprint
import json
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain.prompts import PromptTemplate

from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import JsonOutputParser

from langchain.schema import Document
from langgraph.graph import END, StateGraph

from typing_extensions import TypedDict
from typing import List

os.environ["GROQ_API_KEY"] = "Insert_your_groqCloud_KEY"

GROQ_LLM = ChatGroq(
            model="llama3-70b-8192",
        )


# chain to recive the question and block non-math questions
question_reciver = PromptTemplate(
    template="""
    You are a question Categorizer agent, you are a master at identifing the nature of the question proposed by the user it in a useful way


    Conduct a comprehensive analysis of the email provided and categorize into one of the following categories:
        math - when the asked question is math related, this question should present math symbols like +, -, *, / or any other
        non_math = when the asked question is not math related

            Output a single cetgory only from the types ('math, non_math') \

            if you categorize a question as a non_math question, please tell the user to try again and do not proceed to the next step!

             Return a JSON with a single key 'keywords' with no more than 2 keywords, the complete initial question asked by the student and category, dont' give any other premable or explaination. use the following exemple:

             
                question: (question asked by the user),
                category: (category that you chosed)
            

    QUESTION CONTENT:\n\n {initial_question} \n\n
    """,
    input_variables=["initial_question"],
)


#chain for answer the proposed question
question_answering = PromptTemplate(
    template="""

    You are a famous math teacher, trained to anwser any math question for children from 8 to 12 years old.

    given the CATEGORY of the question, respond as the following:

      for the "math" CATEGORY, solve the equation or anser as aked in QUESTION

      for the "non_math" CATEGORY, tell the user to try again with a math question

    QUESTION: {initial_question} \n
    CATEGORY: {category} \n
    """,
    input_variables=["initial_question","category"],
)


#Represents the state of the graph
class GraphState(TypedDict):
    initial_question : str
    category : str
    num_steps : int


#Define the tool for categorize the question
def Categorize_question(state):
    print("---CATEGORIZING INITIAL QUESTION---")
    initial_question = state['initial_question']
    num_steps = int(state['num_steps'])
    num_steps += 1

    question_category_generator = question_reciver | GROQ_LLM | StrOutputParser()

    #question categorization
    question_result = question_category_generator.invoke({"initial_question": initial_question})
    

    #save the categorize in a JSON file
    with open('question.json', 'w') as f:
      json.dump(question_result, f)


    return {"num_steps":num_steps}


#Define the tool for answering the question
def Question_answering(state):

    print("---ANSWERING THE QUESTION---")
    num_steps = state['num_steps']
    num_steps += 1


    #load the JSON file with the category and question
    with open('question.json', 'r') as f:
      data = json.load(f)

    initial_question = data["question"]
    category = data["category"]

    question_answering = question_answering | GROQ_LLM | JsonOutputParser()

    # question answer
    answer = question_answering.invoke({"initial_question": initial_question,
                                            "category": category })
    
    return {"answer": answer, "num_steps":num_steps}


# --- Debug---
def state_printer(state):
    """print the state"""
    print("---STATE PRINTER---")
    print(f"initial_question: {state['initial_question']} \n" )
    print(f"Category: {state['category']} \n")
    print(f"Num Steps: {state['num_steps']} \n")
    return

#Define workflow
workflow = StateGraph(GraphState)

# Define nodes
workflow.add_node("Categorize_question", Categorize_question) # Filters question
workflow.add_node("Question_answering", Question_answering) # Answer the question

#workflow direction
workflow.set_entry_point("Categorize_question")
workflow.add_edge("Categorize_question", "Question_answering")
workflow.add_edge("Question_answering", END)

#compile the workflow
app = workflow.compile()

#proposed question
question = """

Hey teacher, can you please help me with my home work? i need help to solve this equation: 5x2 + 2x + 2 = 0

"""

# run the agent
inputs = {"initial_question": question, "num_steps":0}
for output in app.stream(inputs):
    for key, value in output.items():
        pprint(f"Finished running: {key}:")