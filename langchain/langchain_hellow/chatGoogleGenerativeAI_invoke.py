from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
import os

from _settings.config import GEMINI_KEY

os.environ["GOOGLE_API_KEY"] = GEMINI_KEY

chat = ChatGoogleGenerativeAI(model="models/gemini-2.5-flash", google_api_key=os.environ["GOOGLE_API_KEY"])
response = chat.invoke([HumanMessage(content="대한민국의 수도는 어디인가요?")])
print(response.content)