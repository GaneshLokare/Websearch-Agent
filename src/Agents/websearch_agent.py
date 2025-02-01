from tavily import TavilyClient
import os


class WebSearchAgent:
    def __init__(self):
        self.TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
        self.tavily_client = self._instantiate_clients()
        
    
    def _instantiate_clients(self):
        """Instantiate and return required clients."""
        return  TavilyClient(api_key=self.TAVILY_API_KEY)


    def web_search(self, query: str) -> str:
        """ usefull for websearch """
        return self.tavily_client.search(query)