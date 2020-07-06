from flask import Blueprint, current_app, jsonify, request
from models import directory_list_worker, file_list_worker
from pathlib import Path

app = Blueprint('view', __name__)

@app.route('/', methods={'GET'})
def get_directory_root():
    directory_list = directory_list_worker.handle('.')
    directory_dict = {
        'type': 'directory',
        'directoryPath': '.',
        'count': len(directory_list),
        'data': directory_list
    }
    return jsonify(directory_dict)

@app.route('/<path:directory_path>', methods={'GET'})
def get_directory(directory_path):
    '''
        指定されたパスに応じたJSONを返す
    Args:
        directory_path: 対象のパス
    return:
        パターン１：ディレクトリを指定した場合
        ex:
        {
            type:"directory"
            "directoryPath": /var/hoge,
            "count": 2,
            "data": [
                {
                    "name": "file1.jpg",
                    "path": ".thumbnail/file1.png"
                },
                {
                    "name": "file2.jpg",
                    "path": "view/file2.png"
                    "thumbnail": "thumbnail/file1.png"
                }
            ]
        }

        パターン２：ファイルを指定した場合
        ex:
        {
            "type":"file"
            "directoryPath": /var/hoge.png,
            "count": 1,
            "data": [
                {
                    "name": "file1.jpg",
                    "path": "img/file1.png",
                    "prev": "view/file0.png",
                    "next": "view/file2.png",
                    "parent": "view/"
                }
            ]
        }
    '''

    data_type = ''
    if Path(directory_path).is_dir():
        data_type = 'directory'
        target_path_info = directory_list_worker.handle(directory_path)
    else:
        data_type = 'file'
        target_path_info = file_list_worker.handle(directory_path)
    target_path_dict = {
        'type': data_type,
        'directoryPath': directory_path,
        'count': len(target_path_info),
        'data': target_path_info
    }
    return jsonify(target_path_dict)
