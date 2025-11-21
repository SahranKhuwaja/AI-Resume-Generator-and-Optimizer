from flask import Flask
from routers.generator_router import generator_router

app = Flask(__name__)

@app.get('/')
def index():
    return {
        "App": "AI Resume Generator"
    }

app.register_blueprint(generator_router, url_prefix="/generator")

if __name__ == "__main__":
    app.run(debug=True)
