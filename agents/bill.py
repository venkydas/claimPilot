from .base import BaseAgent

class BillAgent(BaseAgent):
    async def extract(self, text: str) -> dict:
        prompt = (
            "Extract the following fields from the hospital bill (as JSON): "
            "hospital_name, total_amount, date_of_service. "
            "Return ONLY a valid JSON object with those keys. Example: "
            "sample output: "
            '{"hospital_name": "...", "total_amount": 12345, "date_of_service": "YYYY-MM-DD"}'
        )
        result = await self.llm_call(prompt, text)
        import json
        return json.loads(result)
