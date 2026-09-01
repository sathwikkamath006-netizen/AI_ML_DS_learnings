from dotenv import load_dotenv
load_dotenv()
from langchain_mistralai import ChatMistralAI
from langchain.tools import tool 
from langchain_core.messages import HumanMessage
from rich import print 

#1 creating a tool 

@tool
def get_text_length(text: str) -> int:
    """Returns the number of character in a given text"""
    return len(text)

tools = {
    "get_text_length" : get_text_length
}
llm = ChatMistralAI(model = "mistral-small-2506")

#tool binding 
llm_with_tool = llm.bind_tools([get_text_length])

message = []
prompt = input("You: ")
query = HumanMessage(prompt)
message.append(query)

result = llm_with_tool.invoke(message)

message.append(result)

#after the query there will be only tool_calls resutls fi the query matches
if result.tool_calls:
    tool_name = result.tool_calls[0]["name"]
    tool_message = tools[tool_name].invoke(result.tool_calls[0])
    message.append(tool_message)
   

result = llm_with_tool.invoke(message)
print(result.content)

#1.get_length tool returns the length
# query find the length in this "Hello bro how are you"
# so this understand LLM there might be tool_calling by the 
# docstrring
# 
# then the answer is written back to LLM that will make proper sentence of 
# it and give back the reponse
# 
# when the query is passed that time in the result section
# there are so many things in that tool_calls[0]["name"] u would take this and call it #