import json
from .base import BaseAgent
from .prompts import VALIDATION_PROMPT

class ValidationAgent(BaseAgent):
    async def validate(self, docs: list) -> dict:
        system_message ="You are a medical document validator, responsible for checking the consistency and completeness of medical documents."
        
        docs_json = json.dumps(docs)
        prompt_text = VALIDATION_PROMPT.format(content=docs_json)
        result = await self.llm_call(system_message, prompt_text)
        
        return json.loads(result)
