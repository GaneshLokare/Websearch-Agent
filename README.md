# Websearch-Agent


## Overview
The **Websearch Agent** is a application built using **Streamlit** and **LangChain** that interacts with users, processes queries, and provides AI-generated responses. It also includes **web search functionality** using Tavily API to retrieve relevant information when needed.

## Features
- **Conversational AI**: Uses OpenAI's GPT models to generate responses.
- **Session Persistence**: Maintains chat history using Streamlit's session state.
- **Tool Integration**: Utilizes external tools like web search to provide more accurate answers.
- **LangGraph Implementation**: Uses LangChain's LangGraph for structured conversation flows.
- **Simple & Interactive UI**: Built with Streamlit for a user-friendly experience.

## Project Structure
```
AI_Chat_Assistant/
│── src/
│   │── tools.py
│   │── Agents/
│   │   ├── websearch_agent.py
│── app.py
│── .env
│── requirements.txt
│── README.md
```
### File Descriptions:
- `app.py`: Main Streamlit application.
- `src/tools.py`: Contains LangChain integration and tool bindings.
- `src/Agents/websearch_agent.py`: Implements web search functionality.
- `.env`: Stores API keys and environment variables.
- `requirements.txt`: Lists required dependencies.
- `README.md`: Project documentation.

## Installation
### 1. Clone the repository
```sh
$ git clone https://github.com/GaneshLokare/Websearch-Agent.git
$ cd Websearch-Agent
```
### 2. Create a virtual environment (optional but recommended)
```sh
$ python -m venv venv
$ source venv/bin/activate   # On Windows: venv\Scripts\activate
```
### 3. Install dependencies
```sh
$ pip install -r requirements.txt
```
### 4. Set up environment variables
Create a `.env` file in the project root and add the required API keys:
```
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
LANGCHAIN_TRACING_V2=your_langchain_tracing_key
LANGCHAIN_PROJECT=your_langchain_project_name
```

## Usage
### 1. Run the application
```sh
$ streamlit run app.py
```
### 2. Interact with the chatbot
- Type your queries in the chat input box.
- The AI will respond based on LangChain's processing.
- Click **Clear Chat** to reset the conversation.

## Technologies Used
- **Streamlit**: UI framework for building interactive web apps.
- **LangChain**: Framework for building AI-powered applications.
- **OpenAI API**: Provides LLM-based responses.
- **Tavily API**: Enables web search functionality.
- **LangGraph**: Used for structured conversational flows.



