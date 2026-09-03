#1.tools.py agents.py pipeline.py
# in tools.py buliding the searching and the url reading tools function
# in agents just intergrating the tools and creating 2 more wirter and score generator
# pipeline will process all the things#


from langchain.tools import tool 
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os 
from dotenv import load_dotenv
from rich import print
load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def web_search(query : str) -> str:
    """Search the web for recent and reliable information on a topic . Returns Titles , URLs and snippets."""
    results = tavily.search(query=query,max_results=5)

    out = []
# results['results']: results = tavily. this will give dictnariy 
# results is the dictnary which contains so many things like query key then 
# result key it is the array so u want that thing sooooo results['results']:
# 
# in loop r  5 outputs in that each output has the key val
# results:{
# query:"jfdj",
# results:{
# {title:"dxgf",
# url:fksd},{ same thing },#


    for r in results['results']:
        out.append(
            f"Title: {r['title']}\nURL: {r['url']}\nSnippet: {r['content'][:300]}\n"
        )
    
    return "\n----\n".join(out)
#ALL the list ele --- 1----2----3 like this the data will print



@tool
def scrape_url(url: str) -> str:
    """Scrape and return clean text content from a given URL for deeper reading."""
    try:
        resp = requests.get(url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(resp.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()
        return soup.get_text(separator=" ", strip=True)[:3000]
    except Exception as e:
        return f"Could not scrape URL: {str(e)}"

#timeout means wait bro this time
# so here the request goes to the URL then it would extract everything
# when u inspect the things after that u have 
# this beautifulsoup hold that html text in structured manner
# 
# loop would remove all the unwanted things html code css
# 
# after that u have the text only first 3000 words#