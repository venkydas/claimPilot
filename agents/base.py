import os
import openai
from dotenv import load_dotenv
import json

load_dotenv(verbose=True)

OPENAI_API_KEY=os.environ["OPENAI_API_KEY"]


class BaseAgent:
    def __init__(self):
        openai.api_key = OPENAI_API_KEY
    
    async def llm_call(self, prompt: str, text: str = "") -> str:
        response = openai.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "system", "content": prompt}, {"role": "user", "content": text}],
            temperature=0,
        )

        result = response.choices[0].message.content.strip()
        result = result.replace("\n", " ").replace("  ", " ")
        result = result.replace("```json", "").replace("```", "").strip()
        return result
    
