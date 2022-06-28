import logging

from flask import Flask, request, render_template, send_from_directory
# from functions import ...
from loader.views import loader_blueprint
from main.views import main_blueprint

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

app.register_blueprint(main_blueprint)  # Регистрация главного блюпринта
app.register_blueprint(loader_blueprint)  # Регистрация блюпринта загрузки
logging.basicConfig(filename='basic.log', level=logging.INFO)  # загрузка файла логов


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()

