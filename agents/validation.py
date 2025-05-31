from .base import BaseAgent

class ValidationAgent(BaseAgent):
    async def validate(self, docs: list) -> dict:
        prompt = (
            "Given these structured claim documents ( array of jsons ), identify missing required document types "
            "(must have bill and discharge_summary), and any discrepancies in patient or date fields. "
            "Return a JSON object with two arrays: missing_documents, discrepancies."
        )
        import json
        docs_json = json.dumps(docs)
        result = await self.llm_call(prompt, docs_json)
        return json.loads(result)
