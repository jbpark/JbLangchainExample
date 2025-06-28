import os

from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

from _settings.config import GEMINI_KEY

os.environ["GOOGLE_API_KEY"] = GEMINI_KEY

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=1
)

messages = [HumanMessage(content="왜 파이썬이 가장 인기있는 프로그래밍 언어야?")]

# 수동 스트리밍 구현
response = llm.stream(messages)
for chunk in response:
    print(chunk.content, end="", flush=True)
