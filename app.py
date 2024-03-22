from flask import Flask
from src.app.api.openai.route import openai_blueprint
from src.app.api.stability.route import stability_blueprint

app = Flask(__name__, template_folder="storytelling-web-app\src\app\templates")

# Register Blueprints
app.register_blueprint(openai_blueprint, url_prefix="/api/openai")
app.register_blueprint(stability_blueprint, url_prefix="/api/stability")

if __name__ == "__main__":
    app.run(debug=True, port=5100)
