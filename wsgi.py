from flask import Flask
from application.bp.homepage.routes import homepage

app = Flask(__name__)

# Register the Blueprint
app.register_blueprint(homepage)
