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
        data_list: 
        [
            {
                "name": "file1.png",
                "thumbnail": "thumbnail/file1.png",
                "path": "img/file1.png"
            },
            {
                "name": "file2.png",
                "thumbnail": "thumbnail/file2.png",
                "path": "img/file2.png"
            }
        ]         
    '''
    directory_list = get_directory_list(Path(directory_path))
    data_list = [{'name': os.path.basename(item), 'thumbnail': generate_thumbnail(item), 'path': generate_path(item)} for item in directory_list if not os.path.basename(item).startswith('.')]
    return data_list


def generate_path(directory_path: str):
    directory_path = directory_path.replace("./", "")
    if os.path.isdir(directory_path):
        return f'view/{quote(directory_path)}'
    else:
        return f'view/{quote(directory_path)}'


def get_directory_list(directory_path: Path):
    if directory_path.exists() and directory_path.is_dir():
        return glob.glob(glob.escape(str(directory_path)) + '/*')
    else:
        return []
