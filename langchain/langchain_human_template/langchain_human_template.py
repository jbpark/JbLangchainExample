# 1. API KEY 저장을 위한 os 라이브러리 호출
import os

# 2. Google Gemini LLM 로드를 위한 라이브러리 호출
from langchain_google_genai import ChatGoogleGenerativeAI

# 3. 프롬프트 템플릿 관련 라이브러리 호출
from langchain.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
)

from _settings.config import GEMINI_KEY

# 4. Google Gemini API 키 환경변수에 저장
os.environ["GOOGLE_API_KEY"] = GEMINI_KEY  # 실제 API 키로 변경

# 5. Gemini 모델을 로드합니다.
gemini = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)

# 6. 역할 프롬프트 템플릿 정의 (예시 template 사용)
template = "너는 창의적인 요리사야. 사용자가 입력한 재료로 만들 수 있는 요리 아이디어를 제안해줘."
system_message_prompt = SystemMessagePromptTemplate.from_template(template)

# 7. 사용자가 입력할 매개변수 template 선언
human_template = "{재료}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

# 8. ChatPromptTemplate에 system message와 human message 템플릿을 삽입
chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

# 9. Gemini API에 ChatPromptTemplate을 입력할 때, human message의 매개변수인 '재료'를 할당하여 전달
answer = gemini(chat_prompt.format_prompt(재료="양파, 계란, 사과, 빵").to_messages())
print(answer.content)
