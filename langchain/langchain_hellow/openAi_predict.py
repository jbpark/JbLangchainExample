import os
from langchain.llms import OpenAI

from _settings.config import OPENAI_KEY

os.environ["OPENAI_API_KEY"] = OPENAI_KEY

davinch3 = OpenAI(model_name="gpt-3.5-turbo-instruct")
davinch3.predict("한국의 수도는 어디인가요")