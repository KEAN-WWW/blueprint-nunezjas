from flask import Flask
from application.bp.homepage.routes import homepage

# Tell Flask where to find the global templates folder
app = Flask(__name__)

# Register the Blueprint
app.register_blueprint(homepage)

if __name__ == '__main__':
    app.run(debug=True)