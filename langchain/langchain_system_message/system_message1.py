import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

from _settings.config import GEMINI_KEY

os.environ["GOOGLE_API_KEY"] = GEMINI_KEY

# Gemini 모델 초기화
gemini = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  # 또는 "gemini-1.5-pro"
    temperature=1
)

# 메시지 구성 (시스템 메시지를 HumanMessage로 변환)
messages = [
    HumanMessage(  # SystemMessage 대체
        content="너는 20년차 시니어 개발자야. 사용자의 질문에 매우 건방지게 대답해줘."
    ),
    HumanMessage(
        content="파이썬의 장점에 대해서 설명해줘."
    )
]

# 응답 생성
response = gemini.invoke(messages)
print(response.content)
