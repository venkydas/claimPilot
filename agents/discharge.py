from .base import BaseAgent

class DischargeAgent(BaseAgent):
    async def extract(self, text: str) -> dict:
        prompt = (
            """
            Extract the following fields from the discharge summary (as JSON):
            patient_name, diagnosis, admission_date, discharge_date.
            Return ONLY a valid JSON object with those keys. Example: 
            {"patient_name": "...", "diagnosis": "...", "admission_date": "YYYY-MM-DD", "discharge_date": "YYYY-MM-DD"}
            """

        )
        result = await self.llm_call(prompt, text)
        import json
        try:
            result = json.loads(result)
        except json.JSONDecodeError:
            raise ValueError("Failed to parse JSON from the LLM response.")
        return result
