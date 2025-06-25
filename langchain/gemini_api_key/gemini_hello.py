from google import genai

from _settings.config import GEMINI_KEY

client = genai.Client(api_key=GEMINI_KEY)

response = client.models.generate_content(
    model="gemini-2.0-flash",  # or "gemini-1.5-pro" or other available models
    contents="한국의 수도는 어디인가요?"
)
print(response.text)
