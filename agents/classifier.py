from .base import BaseAgent
from .prompts import DOCUMENT_CLASSIFICATION_PROMPT

class ClassificationAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.name = "ClassificationAgent"
        self.description = (
            "Classifies medical documents into bill, discharge_summary, id_card, or unknown."
        )

    async def classify(self, filename: str, text: str) -> str:
        system_message = (
            "You are a medical document classifier, responsible for determining the type of medical document "
        )

        prompt_text = DOCUMENT_CLASSIFICATION_PROMPT.format( file_name=filename, content=text)
        doc_type = await self.llm_call(system_message, prompt_text)
        doc_type = doc_type.lower().strip()

        if doc_type not in {"bill", "discharge_summary", "id_card"}:
            doc_type = "unknown"

        return doc_type
