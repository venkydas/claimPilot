DOCUMENT_CLASSIFICATION_PROMPT = """
Classify the document '{file_name}' based on its content.

Possible types:
- bill
- discharge_summary
- id_card
- unknown

Return **only** the type of document, in lowercase, using exactly one of the following values: `bill`, `discharge_summary`, `id_card`, `unknown`.

CONTENT:
{content}
"""

DISCHARGE_SUMMARY_PROMPT = """
            Given an array of structured claim documents (each as a JSON object) given below as content, identify:

            1. **Missing document types:** 
            - The set must include both a `bill` and a `discharge_summary`. 
            - List any missing required types in the `missing_documents` array.

            2. **Discrepancies:** 
            - Look for mismatches in `patient` or `date` fields across the documents.
            - List each discrepancy as a JSON object in the `discrepancies` array, specifying the field, and the conflicting values.

            **Return a single JSON object with two arrays:**
            ```json
            {
            "missing_documents": [],
            "discrepancies": []
            }

            CONTENT: {content}
        """

VALIDATION_PROMPT = """
Your task is to identify any missing documents or discrepancies in the provided data.
Return a JSON object with the following structure:
{{
    "missing_documents": ["list", "of", "missing", "documents"],
    "discrepancies": ["list", "of", "discrepancies"]
}}
If no issues are found, return empty lists.

CONTENT: {content}
"""
