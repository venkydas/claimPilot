import json
from .base import BaseAgent
from .prompts import DISCHARGE_SUMMARY_PROMPT

class DischargeAgent(BaseAgent):
    async def extract(self, text: str) -> dict:
        system_message = """
            You are a medical documents analyzer, responsible for extracting structured information from discharge summaries.
            """
        
        prompt_text = DISCHARGE_SUMMARY_PROMPT.format(content=text)
        result = await self.llm_call(system_message, prompt_text)

        try:
            result = json.loads(result)
        except json.JSONDecodeError:
            raise ValueError("Failed to parse JSON from the LLM response.")
        return result
