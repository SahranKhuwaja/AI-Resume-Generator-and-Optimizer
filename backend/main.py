from flask import Flask
from flask_cors import CORS
from routers.generator_router import generator_router
from routers.optimizer_router import optimizer_router

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.get('/')
def index():
    return {
        "App": "AI Resume Generator and Optimizer"
    }

app.register_blueprint(generator_router, url_prefix="/generator")
app.register_blueprint(optimizer_router, url_prefix="/optimizer")

if __name__ == "__main__":
    app.run(debug=True)
