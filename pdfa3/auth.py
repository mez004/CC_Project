import requests
import jwt
from functools import wraps
from flask import request, jsonify


JWKS_URL = "https://www.googleapis.com/oauth2/v3/certs"
ISSUER = "https://accounts.google.com"
def get_token_from_header():
    """Extract Bearer token from Authorization header"""
    auth_header = request.headers.get("Authorization")

    if not auth_header:
        return None, "Missing Authorization header"

    parts = auth_header.split()

    if len(parts) != 2 or parts[0] != "Bearer":
        return None, "Invalid Authorization format"

    return parts[1], None


def fetch_jwks():
    """Fetch public keys from FrontEgg"""
    try:
        response = requests.get(JWKS_URL)
        return response.json()
    except Exception:
        return None


def validate_token(token):
    """Decode and validate JWT token"""
    try:
        
        decoded = jwt.decode(token, options={"verify_signature": False})

        
        if "sub" not in decoded:
            return None, "Invalid token: 'sub' missing"

        return decoded, None

    except Exception:
        return None, "Invalid token"



def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        
        token, error = get_token_from_header()
        if error:
            return jsonify({"error": error}), 401

    
        jwks = fetch_jwks()
        if jwks is None:
            return jsonify({"error": "Failed to fetch JWKS"}), 500

        decoded, error = validate_token(token)
        if error:
            return jsonify({"error": error}), 403

       
        request.user = decoded

        return f(*args, **kwargs)

    return decorated
