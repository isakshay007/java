
# Java Generator 🚀

## Overview
The **Java Generator** is a Streamlit-based application powered by **Lyzr Agent API**. It converts natural language inputs into precise Java code, making coding simpler and more accessible for developers of all skill levels. With advanced AI integration, this app delivers accurate and relevant Java solutions based on user input.

---

## Features
- **AI-Driven Java Code Generator**:
  - Analyze natural language inputs to generate accurate Java code.
  - Provides clear explanations for the generated code.
- **Tool Integration**:
  - Utilizes `perplexity_search` for context-aware code generation.
- **Interactive UI**:
  - User-friendly interface for entering natural language queries.
  - Displays the corresponding Java code with explanations.

---

## Installation

### Prerequisites
- **Python**: Ensure Python 3.8 or higher is installed.
- **Dependencies**: Install required packages via `requirements.txt`.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/java-generator.git
   cd java-generator
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your **API Keys**:
   - Create a `.env` file in the project directory.
   - Add your API keys in the following format:
     ```env
     OPENAI_API_KEY="your_openai_api_key"
     LYZR_API_KEY="your_lyzr_api_key"
     ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```

5. Open your browser and navigate to:
   ```
   http://localhost:8501
   ```

---

## Usage

1. **Enter Natural Language Query**: Input your desired Java operation or functionality in plain language.
   - Example: *"Write a program to check if a number is prime."*

2. **Generate Java Code**: Click the **"Generate!"** button to view the generated Java code.

3. **Review Results**: The app provides Java code tailored to your input, along with an explanation.

---

## File Structure
```
java-generator/
│
├── app.py                  # Main application file
├── lyzr_agent.py           # Lyzr Agent API integration
├── requirements.txt        # Python dependencies
├── .env                    # API key configuration
└── .streamlit/             # Streamlit configuration
    └── config.toml         # UI settings
```

---

## Key Functionalities

### 1. **Natural Language Input**
- Accepts plain language descriptions of Java tasks or functionality.

### 2. **Java Code Generation**
- Uses Lyzr Agent API and OpenAI models to generate accurate Java code.

### 3. **Explanations**
- Provides detailed explanations for the generated Java code.

---

## Dependencies

- **Streamlit**: Interactive UI framework.
- **Lyzr Agent API**: Integrates advanced AI capabilities.
- **dotenv**: Manages environment variables securely.
- **requests**: Handles API interactions.
- **Python (>=3.8)**

### Install all dependencies with:
```bash
pip install -r requirements.txt
```

---

## Acknowledgments
- Built with the **Lyzr Agent API**.
- Designed to simplify Java programming and enhance developer productivity.
