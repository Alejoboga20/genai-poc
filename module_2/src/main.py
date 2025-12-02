import os
from dotenv import load_dotenv

from langchain_openai import OpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm = OpenAI(api_key=OPENAI_API_KEY)
result = llm.invoke('tell me your name')
print(result)
