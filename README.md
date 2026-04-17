# PDF/A-3 API 

# Member 1 Complete 

## Setup Instructions

1. Extract the ZIP file
2. Open terminal in the project folder
3. Create virtual environment:
   - Windows: `python -m venv venv` then `venv\Scripts\activate`
   - Kali Linux: `python3 -m venv venv` then `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run the app: `python app.py`
6. Swagger UI available at: `http://localhost:5000/apidocs/`

## API Endpoints (Ready for implementation)

- `POST /pdf-a3/generate` - Returns 501 (Not implemented)
- `POST /pdf-a3/extract` - Returns 501 (Not implemented)
# Member 2

# Member 3 — /pdf-a3/generate Implementation completed
This endpoint takes a Base64-encoded PDF and Base64-encoded XML file and returns a Base64-encoded PDF/A-3 document with the XML embedded using the Factur-X Python library.

Endpoint

`POST /pdf-a3/generate`

Request Body
{
  "pdf": {
    "content": "base64-encoded-pdf"
  },
  "xml": {
    "content": "base64-encoded-xml"
  }
}
Success Response (200)
{
  "successful": true,
  "pdfa3": {
    "content": "base64-encoded-pdfa3"
  }
}

## Error Responses
400 — Missing fields or invalid Base64
500 — Internal error during PDF/A-3 generation

## How It Works
1. Decode Base64 PDF and XML
2. Call Factur-X library to generate PDF/A-3
3. Encode the result back to Base64
4. Return JSON response

## Testing with Swagger
1. Run the server: python app.py
2. Open: `http://localhost:5000/apidocs/`
3. Use /pdf-a3/generate
4. Provide Base64 PDF and XML

## Note
Attachments and extraction are handled by other team members.
