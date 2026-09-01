#1.sequential doing 1 thing
#2.runnable passthrough doing 2 things
#anything u pass to this runnable passthorugh it wiil return that same thing to u

from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough


model = ChatMistralAI(model="mistral-small-2506")
parser = StrOutputParser()

code_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a code generator"),
    ("human", "{topic}")
])

explain_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant who explains code in simple terms"),
    ("human", "Explain the following code in simple words:\n{code}")
])

seq = code_prompt | model | parser 


seq2 = RunnableParallel(
    {"code" :  RunnablePassthrough(),
     "explanation" : explain_prompt | model | parser
    }
)

chain = seq | seq2

result = chain.invoke({"topic" : "please write a code of palindrome in python "})

print(result['code'])
print(result['explanation'])



#RunnablePassthrough() when u pass anything it will give u back the same thing
# so here seq is the would store the code 
# 
# then it will get passwed to expain_prmpt then it will exapin it 
# 
# chain = seq | seq2 here all the magic will happen seq1 here palindrome in python 
# seq from this code is genrate this is the code is current output this will runuablpassthrough
# to the next seq2 here exapination
# 
# inside the code it will be there code will passed to the next#