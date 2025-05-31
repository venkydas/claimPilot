from .base import BaseAgent

class ClassificationAgent(BaseAgent):
    async def classify(self, filename: str, text: str) -> str:
        prompt = (
            "You are a medical document classifier. "
            "Given the filename and content, output ONLY ONE of these types: bill, discharge_summary, id_card, or unknown."
        )
        full_text = f"Filename: {filename}\nContent: {text}"
        doc_type = await self.llm_call(prompt, full_text)
        doc_type = doc_type.lower().strip()
        if doc_type not in {"bill", "discharge_summary", "id_card"}:
            doc_type = "unknown"
        return doc_type
