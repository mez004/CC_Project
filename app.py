from flask import Flask, redirect
from flasgger import Swagger
from pdfa3.routes import pdfa3_bp

app = Flask(__name__)

# Swagger template (Swagger 2.0 only - no openapi field)
swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "PDF/A-3 API",
        "version": "1.0.0"
    },
    "basePath": "/pdf-a3",
    "securityDefinitions": {
        "BearerAuth": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header"
        }
    }
}

# Initialize Swagger
swagger = Swagger(app, template=swagger_template)

# Register blueprint
app.register_blueprint(pdfa3_bp)

# Redirect root to Swagger UI
@app.route('/')
def index():
    return redirect('/apidocs/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)