import os
from dotenv import load_dotenv
from pprint import pprint
from langchain_core.messages import AIMessage, HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient
from langgraph.graph import StateGraph, START, END
from langgraph.graph import MessagesState
from langgraph.prebuilt import ToolNode
from langgraph.prebuilt import tools_condition
from src.Agents.websearch_agent import WebSearchAgent
from langgraph.checkpoint.memory import MemorySaver

class LangChainWithTools:
    def __init__(self):
        """Initialize the class by loading environment variables and setting up clients."""
        self.OPENAI_API_KEY, self.TAVILY_API_KEY, self.LANGCHAIN_TRACING_V2, self.LANGCHAIN_PROJECT = self._load_environment_variables()
        self.llm, self.tavily_client = self._instantiate_clients()
        self.llm_with_tools = self._bind_tools_to_llm()
        self.graph = self._build_graph()
        

    def _load_environment_variables(self):
        """Load environment variables from the .env file."""
        load_dotenv()
        return os.getenv('OPENAI_API_KEY'), os.getenv('TAVILY_API_KEY'), os.getenv('LANGCHAIN_TRACING_V2'), os.getenv('LANGCHAIN_PROJECT')

    def _instantiate_clients(self):
        """Instantiate and return required clients."""
        return ChatOpenAI(model="gpt-4o-mini"), TavilyClient(api_key=self.TAVILY_API_KEY)

   
    def _web_search(self, query: str) -> str:
        """ usefull for websearch """
        search = WebSearchAgent()
        result = search.web_search(query)
        return result

    

    def _bind_tools_to_llm(self):
        """Bind tools to the LLM instance."""
        tools = [self._web_search]
        return self.llm.bind_tools(tools)
    

    def _tool_calling_llm_node(self, state: MessagesState):
        """Node to handle tool calling LLM logic."""
        return {"messages": [self.llm_with_tools.invoke(state["messages"])]}  

    def _build_graph(self):
        """Build and compile the LangGraph."""
        builder = StateGraph(MessagesState)
        builder.add_node("assistant", self._tool_calling_llm_node)
        builder.add_node("tools", ToolNode([self._web_search]))
        builder.add_edge(START, "assistant")
        builder.add_conditional_edges(
            "assistant",
            # If the latest message (result) from assistant is a tool call -> tools_condition routes to tools
            # If the latest message (result) from assistant is a not a tool call -> tools_condition routes to END
            tools_condition,
        )
        builder.add_edge("tools", "assistant")
        memory = MemorySaver()
        graph = builder.compile(checkpointer=memory)

        return graph

    def process_messages(self, messages):
        """Invoke the graph with a list of messages."""
        return self.graph.invoke({"messages": messages}, config={"configurable": {"thread_id": "1"}})