import os
from langchain_google_genai import ChatGoogleGenerativeAI
from _settings.config import GEMINI_KEY

os.environ["GOOGLE_API_KEY"] = GEMINI_KEY

# Gemini 모델 인스턴스 생성
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  # 또는 "gemini-pro" 등 사용 가능
    temperature=0,
    max_output_tokens=200
)

# 질문에 대한 응답 생성
response = llm.invoke("한국의 수도는 어디인가요")
print(response.content)