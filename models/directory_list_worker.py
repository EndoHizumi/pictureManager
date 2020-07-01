from pathlib import Path
from models.thumbnail_generator import generate_thumbnail
from urllib.parse import quote
import glob
import os

def handle(directory_path):
    '''
    指定されたディレクトリのリストを返す

    Args:
        directory_path: 対象のディレクトリのパス

    return: 
        パターン１：ディレクトリを指定した場合
        ex:
        {
            "directoryPath": /var/hoge,
            "count": 2,
            "data": [
                {
                    "name": "file1.jpg",
                    "path": ".thumbnail/file1.png"
                }
            ]
        }

        パターン２：ファイルを指定した場合
        ex:
        {
            "directoryPath": /var/hoge.png,
            "count": 1,
            "data": []
        }
    '''
    directory_list = get_directory_list(Path(directory_path))
    data_list = [{'name': os.path.basename(item), 'thumbnail': generate_thumbnail(item), 'path': generate_path(item)} for item in directory_list if not os.path.basename(item).startswith('.')]
    directory_dict = {
        'directoryPath': directory_path,
        'count': len(data_list),
        'data': data_list
    }
    return directory_dict


def generate_path(directory_path: str):
    # print(f'"{os.path.abspath(directory_path)}" is_dir: {os.path.isdir(directory_path)}: is_exists:{os.path.exists(directory_path)}')
    if os.path.isdir(directory_path):
        return f'view/{quote(directory_path)}'
    else:
        return f'img/{quote(directory_path)}'


def get_directory_list(directory_path: Path):
    if directory_path.exists() and directory_path.is_dir():
        return glob.glob(glob.escape(str(directory_path))+'/*')
    else:
        return []
