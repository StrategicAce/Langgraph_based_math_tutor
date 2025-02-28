# Langgraph based math tutor

This project is a math tutor developed using the **LangGraph** library to create a workflow that categorizes and answers math-related questions. The tutor can identify whether a question is math-related and, if so, provide an appropriate response.

---

## 📋 Requirements

- Python 3.8 or higher
- LangGraph library
- LangChain library
- LangChain-Groq library
- Groq Cloud API Key

---

## 🛠️ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/StrategicAce/Langgraph_based_math_tutor.git
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up the Groq Cloud API key:

   ```bash
   export GROQ_API_KEY="your_api_key_here"
   ```

---

## 🚀 Usage

The project consists of a workflow that categorizes the user's question and, if it is a math-related question, provides an answer. The workflow is defined using the **LangGraph** library.

### Running the Tutor

To run the tutor, simply execute the Python script:

```bash
langgraph_based_math_tutor.py
```

The script will process the provided question and display the answer.

### Example Question

Here is an example of a question the tutor can answer:

```python
question = """
Hey teacher, can you please help me with my homework? I need help to solve this equation: 5x2 + 2x + 2 = 0
"""
```

### Workflow

1. **Question Categorization**: The tutor first categorizes the question as `math` or `non_math`.
2. **Answering the Question**: If the question is categorized as `math`, the tutor provides a detailed answer. Otherwise, it asks the user to try again with a math-related question.

---

## 🗂️ Code Structure

- `tutor.py`: Contains the main code for the tutor, including the workflow definition and the categorization and answering functions.
- `README.md`: This file, containing information about the project.

---

## 🤝 Contributing

Contributions are welcome! Feel free to open **issues** and **pull requests**.

1. Fork the repository.
2. Create a branch for your feature (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a **pull request**.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## 👨‍🏫 Example Workflow

Here is an example of how the tutor works:

1. The user asks a math-related question, such as:
   ```
   What is the solution to the equation 5x² + 2x + 2 = 0?
   ```

2. The tutor categorizes the question as `math`.

3. The tutor solves the equation and returns the answer:
   ```
   The solution to the equation 5x² + 2x + 2 = 0 is x = [-2 ± sqrt(-36)] / 10.
   ```

4. If the question is not math-related, the tutor responds:
   ```
   Please try again with a math-related question.
   ```

---

## 📌 Notes

- Make sure the Groq Cloud API key is correctly configured.
- The tutor is designed for children aged 8 to 12 but can be adapted for other age groups.

---

### Explanation of the Content

1. **Title and Description**: Introduces the project and its purpose.
2. **Requirements**: Lists the requirements needed to run the project.
3. **Installation**: Steps to clone, install dependencies, and set up the API key.
4. **Usage**: Explains how to run the project and how it works, with examples.
5. **Code Structure**: Describes the main files.
6. **Contributing**: Instructions for contributing to the project.
7. **License**: Information about the license.
8. **Example Workflow**: A practical example of how the tutor works.
9. **Notes**: Additional tips and notes.

This README is complete and ready to be used in your repository!
