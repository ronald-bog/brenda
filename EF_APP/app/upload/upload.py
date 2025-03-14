from flask import Blueprint, render_template, request
import pandas as pd

upload_bp = Blueprint("upload", __name__)


@upload_bp.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return "No file part"
    file = request.files["file"]
    if file.filename == "":
        return "No selected file"
    if file:
        df = pd.read_excel(file)
        return df.to_html()
