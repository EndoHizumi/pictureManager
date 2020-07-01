from flask import Blueprint, current_app, jsonify, request
from models import directory_list_worker

app = Blueprint('view', __name__)

@app.route('/', methods={'GET'})
def get_directory_root():
    return jsonify(directory_list_worker.handle('.'))

@app.route('/<path:directory_path>', methods={'GET'})
def get_directory(directory_path):
    return jsonify(directory_list_worker.handle(directory_path))
