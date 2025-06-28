import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

from _settings.config import GEMINI_KEY

os.environ["GOOGLE_API_KEY"] = GEMINI_KEY

# Gemini 모델 인스턴스 생성
chat_gemini = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  # 또는 "gemini-pro" 등
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()],
    temperature=1
)

# 질문에 대한 답변 생성 (predict → invoke로 변경)
answer = chat_gemini.invoke("왜 파이썬이 가장 인기있는 프로그래밍 언어야?")
print(answer.content)