import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
)
from langchain.prompts.prompt import PromptTemplate

from _settings.config import GEMINI_KEY

# 1. API 키 설정
os.environ["GOOGLE_API_KEY"] = GEMINI_KEY  # 실제 키로 교체

# 2. Gemini 모델 로드
gemini = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.4)

# 3. Few-shot 예시
examples = [
    {
        "question": "삼성전자, 카카오를 5회 분할 매수하고 싶어요. 총 투자금은 1000만 원입니다.",
        "answer": """
| 종목명   | 회차 | 매수가(예상) | 매수금액 (원) |
|----------|------|---------------|----------------|
| 삼성전자 | 1    | 74,500원       | 100,000         |
| 삼성전자 | 2    | 74,000원       | 100,000         |
| 삼성전자 | 3    | 73,500원       | 100,000         |
| 삼성전자 | 4    | 73,000원       | 100,000         |
| 삼성전자 | 5    | 72,500원       | 100,000         |
| 카카오   | 1    | 45,000원       | 100,000         |
| 카카오   | 2    | 44,500원       | 100,000         |
| 카카오   | 3    | 44,000원       | 100,000         |
| 카카오   | 4    | 43,500원       | 100,000         |
| 카카오   | 5    | 43,000원       | 100,000         |

※ 각 종목에 500만 원씩 균등 분배했고, 매수가는 시장 등락을 감안해 회차별로 하향 조정했습니다.
"""
    }
]

# 4. 프롬프트 포맷
example_prompt = PromptTemplate(
    input_variables=["question", "answer"],
    template="고객 요청: {question}\n응답:\n{answer}"
)

# 5. 예제 조합
formatted_examples = "\n\n".join([example_prompt.format(**ex) for ex in examples])

# 6. 새로운 요청
new_question = "삼성전자, NAVER를 5회 분할 매수하고 싶어요. 총 투자금은 1000만 원입니다."

# 7. 최종 프롬프트 조립
full_prompt = f"""아래는 고객의 주식 분할 매수 요청에 대한 예시입니다:

{formatted_examples}

이제 아래 요청에 따라 각 종목별로 분할 매수 전략을 표로 작성해주세요:

고객 요청: {new_question}
응답:
"""

# 8. 시스템 메시지 (역할 부여)
system_message_prompt = SystemMessagePromptTemplate.from_template(
    "너는 투자 전략을 분석해 표로 작성하는 AI 트레이딩 어시스턴트야. 요청에 따라 종목별 분할 매수 전략을 테이블로 제안해줘."
)

# 9. 사용자 메시지 템플릿
human_message_prompt = HumanMessagePromptTemplate.from_template("{input}")

# 10. ChatPromptTemplate 조립
chat_prompt = ChatPromptTemplate.from_messages([
    system_message_prompt,
    human_message_prompt
])

# 11. 메시지 생성 및 Gemini 호출
messages = chat_prompt.format_prompt(input=full_prompt).to_messages()
response = gemini(messages)

# 12. 결과 출력
print(response.content)
