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

# 6. 역할 프롬프트 템플릿 정의
template = (
    "너는 경험 많은 증권사 직원이야. "
    "사용자가 입력한 종목과 비중을 보고 매수 전략을 제안해줘. "
    "시장 상황도 간단히 고려해서 설명해줘."
)
system_message_prompt = SystemMessagePromptTemplate.from_template(template)

# 7. 사용자가 입력할 매개변수 템플릿 선언
human_template = "{매수요청}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

# 8. ChatPromptTemplate에 system + human 메시지를 결합
chat_prompt = ChatPromptTemplate.from_messages([
    system_message_prompt, human_message_prompt
])

# 9. Gemini에게 매수 전략 요청!
answer = gemini(chat_prompt.format_prompt(
    매수요청="삼성전자 80%, 카카오 20% 비중으로 1천만 원 매수하고 싶습니다."
).to_messages())

# 10. 결과 출력
print(answer.content)
