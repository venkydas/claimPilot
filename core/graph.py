from agents.classifier import ClassificationAgent
from agents.bill import BillAgent
from agents.discharge import DischargeAgent
from agents.validation import ValidationAgent
from .utils import get_markdown, pdf_to_text

import asyncio

class ClaimProcessingGraph:
    def __init__(self):
        self.classifier = ClassificationAgent()
        self.bill_agent = BillAgent()
        self.discharge_agent = DischargeAgent()
        self.validator = ValidationAgent()

    async def run(self, files):
        documents = []
        tasks = []

        # Step 1: Classify and extract
        for file in files:
            tasks.append(self._process_single(file))
        docs = await asyncio.gather(*tasks)
        docs = [doc for doc in docs if doc is not None]
        
        # Step 2: Validation
        validation = await self.validator.validate(docs)
        
        # Step 3: Decision
        status = "approved" if not validation["missing_documents"] and not validation["discrepancies"] else "rejected"
        reason = (
            "All required documents present and data is consistent"
            if status == "approved"
            else f"Missing or inconsistent data: {validation}"
        )

        return {
            "documents": docs,
            "validation": validation,
            "claim_decision": {"status": status, "reason": reason}
        }

    async def _process_single(self, file):
        # text_pdf = await pdf_to_text(file.file)
        text = await get_markdown(file.file, filename=file.filename)
        doc_type = await self.classifier.classify(file.filename, text)
        if doc_type == "bill":
            fields = await self.bill_agent.extract(text)
            fields["type"] = "bill"
            return fields
        elif doc_type == "discharge_summary":
            fields = await self.discharge_agent.extract(text)
            fields["type"] = "discharge_summary"
            return fields
        else:
            return None
