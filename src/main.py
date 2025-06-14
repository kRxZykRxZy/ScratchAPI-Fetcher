from flask import Flask, jsonify
from InternalAPI import internal_register_routes
import os
from dotenv import load_dotenv
from flask_cors import CORS, cross_origin
from InternalAPI.API_Helpers.limiter import limiter

load_dotenv()

app = Flask(__name__)

# Set up Flask-Limiter
limiter.init_app(app)

CORS(app, supports_credentials=True, origins=[os.getenv('HOSTED_ON'),'http://localhost'])

print("DEBUG: ", os.getenv('DEBUG'))

@app.route("/")
def hello_world():
    return "<p>CodeTorch Block Compiler API is running.</p>"

# all error handlers
@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({"status": "500", "error": "Internal server error"}), 500

@app.errorhandler(400)
def bad_request(e):
    return jsonify({"status": "400", "error": "Bad request"}), 400

@app.errorhandler(403)
def forbidden(e):
    return jsonify({"status": "403", "error": "Forbidden"}), 403

@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({"status": "405", "error": "Method not allowed"}), 405

@app.errorhandler(401)
def unauthorized(e):
    return jsonify({"status": "401", "error": "Unauthorized"}), 401

@app.errorhandler(409)
def conflict(e):
    return jsonify({"status": "409", "error": "Conflict"}), 409
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"status": "404", "error": "Page not found"}), 404

@app.errorhandler(429)
def too_many_requests(e):
    return jsonify({"status": "429", "error": "Too many requests"}), 429


internal_register_routes(app)

@app.route("/<path:path>", methods=["GET"])
@cross_origin(origins="*")
@limiter.exempt
def static_files(path):    
    return app.send_static_file(path)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
