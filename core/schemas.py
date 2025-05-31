from pydantic import BaseModel
from typing import List, Optional

class Document(BaseModel):
    type: str
    hospital_name: Optional[str]
    total_amount: Optional[float]
    date_of_service: Optional[str]
    patient_name: Optional[str]
    diagnosis: Optional[str]
    admission_date: Optional[str]
    discharge_date: Optional[str]

class ValidationResult(BaseModel):
    missing_documents: List[str]
    discrepancies: List[str]

class ClaimDecision(BaseModel):
    status: str
    reason: str

class ClaimResponse(BaseModel):
    documents: List[Document]
    validation: ValidationResult
    claim_decision: ClaimDecision
