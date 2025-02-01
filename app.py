import streamlit as st
from streamlit_chat import message
from src.tools import LangChainWithTools
from langchain_core.messages import AIMessage, HumanMessage

def init_session_state():
    """Initialize session state variables"""
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'lang_chain_tools' not in st.session_state:
        st.session_state.lang_chain_tools = LangChainWithTools()

def display_chat_history():
    """Display chat messages from history"""
    for i, msg in enumerate(st.session_state.messages):
        # Display user messages
        if isinstance(msg, HumanMessage):
            message(msg.content, is_user=True, key=f"user_{i}")
        # Display AI messages
        elif isinstance(msg, AIMessage):
            message(msg.content, is_user=False, key=f"ai_{i}")

def process_input(user_input):
    """Process user input and get AI response"""
    if user_input:
        # Add user message to state
        st.session_state.messages.append(HumanMessage(content=user_input))
        
        # Get AI response
        result = st.session_state.lang_chain_tools.process_messages(st.session_state.messages)
        ai_msg = result['messages'][-1]
        
        # Add AI response to state
        st.session_state.messages.append(ai_msg)

def main():
    st.title("AI Chat Assistant")
    
    # Initialize session state
    init_session_state()
    
    # Create chat input
    user_input = st.chat_input("Type your message here...")
    
    # Process user input
    if user_input:
        process_input(user_input)
    
    # Display chat history
    display_chat_history()
    
    # Add a clear chat button
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.experimental_rerun()

if __name__ == "__main__":
    main()