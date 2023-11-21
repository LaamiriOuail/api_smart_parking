from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
# Enable CORS for all routes
CORS(app)