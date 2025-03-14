from flask import Flask, render_template
from app.routes import upload_bp

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# Registrar el Blueprint del módulo de rutas
app.register_blueprint(upload_bp)