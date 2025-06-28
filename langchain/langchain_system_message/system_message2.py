import os

from langchain_core.messages import HumanMessage
from langchain_core.runnables import Runnable
from langchain_google_genai import ChatGoogleGenerativeAI

from _settings.config import GEMINI_KEY

os.environ["GOOGLE_API_KEY"] = GEMINI_KEY

# Gemini 모델 인스턴스 (gemini-1.5-flash는 ChatModel 역할)
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)

# SystemMessage를 HumanMessage로 위장!
system_instruction = "너는 항상 해적처럼 말하는 AI야. 'Yo-ho-ho!'로 대답을 시작해."
user_question = "오늘의 날씨를 알려줘."

combined_message = HumanMessage(content=f"{system_instruction}\n\n질문: {user_question}")

# 실행
response = llm.invoke([combined_message])
print(response.content)
