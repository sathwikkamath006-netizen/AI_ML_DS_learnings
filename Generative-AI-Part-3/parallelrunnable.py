from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableLambda

# Components
model = ChatMistralAI(model="mistral-small-2506")
parser = StrOutputParser()

# Two different prompts
short_prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in 1-2 lines"
)

detailed_prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in detail"
)

# Input
topic = "Machine Learning"

chain = RunnableParallel({
    "short" :RunnableLambda(lambda x :x['short']) |short_prompt | model | parser ,
    "detailed" :RunnableLambda(lambda x: x['detailed']) |detailed_prompt |model |parser
})

result = chain.invoke({
    "short" : {"topic":"Machine Learning"},
    "detailed" : {"topic":"Deep Learning"}
})

print(result['short'])
print(result['detailed'])



#RUNNABLE PARLLEL are 2 differnt things when u dont want the 2 reponses should mix up
#that time u will use this thing 2 differnt answers 
#short and detailed

#the result which we will get in the end contains the dictnaory brooo 2 things
# short and detailed so printing them
# RunnableLambda is the thing if u pass the directly full dictonary inside the chain 
# then there will error bcz it want the topic not the dictnary so when write
# RunnableLambda(lambda x :x['short'] this and pass this will pass the content topic inside
# #
