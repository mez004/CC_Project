from flask import Blueprint, request, jsonify
#from .auth import token_required #will not work until Person 2 adds auth, so we have a temporary token_required function below 
import base64

# temporary until Person 2 adds auth
try:
    from .auth import token_required
except ImportError:
    def token_required(f):
        return f

from facturx import generate_facturx_from_binary
pdfa3_bp = Blueprint('pdfa3', __name__, url_prefix='/pdf-a3')

@pdfa3_bp.route('/generate', methods=['POST'])
@token_required
def generate():
    try:
        data = request.get_json()

        # Check required fields
        if not data or "pdf" not in data or "xml" not in data:
            return jsonify({"error": "Missing pdf or xml field"}), 400

        # Decode Base64
        try:
            pdf_bytes = base64.b64decode(data["pdf"]["content"])
            xml_bytes = base64.b64decode(data["xml"]["content"])
        except Exception:
            return jsonify({"error": "Invalid Base64 encoding"}), 400

        # Create PDF/A-3 using Factur-X
        pdfa3_bytes = generate_facturx_from_binary(
            pdf_bytes,
            xml_bytes
        )

        # Encode result back to Base64
        pdfa3_b64 = base64.b64encode(pdfa3_bytes).decode("utf-8")

        return jsonify({
            "successful": True,
            "pdfa3": {
                "content": pdfa3_b64
            }
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@pdfa3_bp.route('/extract', methods=['POST'])
def extract():
    """
    Extract XML from a PDF/A-3 document
    ---
    tags:
      - PDF/A-3
    summary: Extract embedded XML from PDF/A-3
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            pdfa3:
              type: object
              properties:
                content:
                  type: string
    responses:
      200:
        description: Success
      501:
        description: Not implemented
    """
    return jsonify({
        "successful": False,
        "error": "Not implemented yet - Person 3 will add logic"
    }), 501
