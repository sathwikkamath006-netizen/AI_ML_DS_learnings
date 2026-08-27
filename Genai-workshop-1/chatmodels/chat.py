#there is something called  VENV CURL something python package manger watch
#this genai part 1 first 1hr and also the AI model api key to get FREE

from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(model = "mistral-small-2506",temperature=0.9)

response = model.invoke("write a poem on AI")

print(response.content)