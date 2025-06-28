import google.generativeai as genai

from _settings.config import GEMINI_KEY

# API 키 설정
genai.configure(api_key=GEMINI_KEY)

# 모델 목록 확인 (이걸로 어떤 모델이 가능한지 확인 가능)
for model in genai.list_models():
    print(model.name)
