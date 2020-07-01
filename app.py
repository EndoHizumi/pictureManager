from flask import Flask, Response, abort
from endpoints.view import app as view_app

import magic
import imghdr
import os

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.register_blueprint(view_app, url_prefix='/view')


@app.route('/', methods={'GET'})
def hello():
    return 'hello'


@app.route('/img/<path:file_path>', methods={'GET'})
def get_file(file_path):
    file = load_file(file_path)
    if file is not None:
        return Response(response=file, content_type=magic.from_file(file_path, mime=True))
    else:
        return abort(404)


@app.route('/thumbnail/<path:file_path>', methods={'GET'})
def get_thumbnail(file_path):
    file_name = os.path.basename(file_path)
    file_parent_path = os.path.dirname(file_path) or "."
    thumbnail_file_path = f'{file_parent_path}/.thumbnail/{file_name}'
    file = load_file(thumbnail_file_path)
    app.logger.debug(file_path)
    app.logger.debug(thumbnail_file_path)
    if file is not None:
        return Response(response=file, content_type=magic.from_file(thumbnail_file_path, mime=True))
    else:
        return abort(404)


def load_file(file_path):
    if not os.path.exists(file_path):
        return None

    # 画像ファイルではない時、Noneを返す
    if imghdr.what(file_path) is None:
        return None

    with open(file_path, 'rb') as f:
        file = f.read()
        return file


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080, threaded=True)
