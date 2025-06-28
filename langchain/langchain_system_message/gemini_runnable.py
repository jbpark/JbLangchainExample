import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable
from langchain_google_genai import ChatGoogleGenerativeAI

from _settings.config import GEMINI_KEY

os.environ["GOOGLE_API_KEY"] = GEMINI_KEY

# ✅ Gemini LLM 인스턴스 생성
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)

# ✅ LangChain PromptTemplate 정의
prompt = ChatPromptTemplate.from_messages([
    ("human", "{system_message}\n\n질문: {user_input}")
])

# ✅ Runnable 체인 구성
chain: Runnable = prompt | llm

# ✅ 실행 테스트
response = chain.invoke({
    "system_message": "너는 5살 어린이처럼 말해야 해.",
    "user_input": "블랙홀이 뭐야?"
})

print(response.content)

