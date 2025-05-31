# claRA
Insurance claim Review Agent


## Architechture

- Uses **FastAPI** for backend, **LangGraph** for agent orchestration, **Llama parse** for text extraction and **OpenAI GPT** for all LLM operations.
- Upload claim-related PDFs, and `/process-claim` endpoint orchestrates classification, extraction, validation, and claim decision.

## AI Tool Usage

- Used **Llamaparse** for parsing the text from pdfs.
- **GPT** for analyzing input text and decision making.

## Sample Prompts Used

1. **Document Classification**  
   "You are a medical document classifier. Given the filename and content, output ONLY ONE of these types: bill, discharge_summary, id_card, or unknown."

2. **Bill Extraction**  
   "Extract the following fields from the hospital bill (as JSON): hospital_name, total_amount, date_of_service. Return ONLY a valid JSON object with those keys..."

3. **Validation**  
   "Given these structured claim documents (JSON array), identify missing required document types (must have bill and discharge_summary), and any discrepancies in patient or date fields. Return a JSON object with two arrays: missing_documents, discrepancies."

## Running Locally

1. `pip install -r requirements.txt`
2. Set your OPENAI_API_KEY and LLAMA_CLOUD_API_KEY in .env file.
3. `uvicorn main:app --reload`
4. POST PDF files to `/process-claim`

## Improvements

- We can use tesseract for OCR based text parsing from these pdf's as they are looking like scanned images.
- To classify the document, we can send the first page to determine, this can be implemented after looking at larger samples docs.
