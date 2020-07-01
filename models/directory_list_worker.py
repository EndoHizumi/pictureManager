from pathlib import Path
from models.thumbnail_generator import generate_thumbnail
from urllib.parse import quote

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
    data_list = [{'name': item.name, 'thumbnail': generate_thumbnail(str(item)), 'path': generate_path(item)} for item in directory_list if not str(item.name).startswith('.')]

    directory_dict = {
        'directoryPath': directory_path,
        'count': len(data_list),
        'data': data_list
    }
    return directory_dict


def generate_path(path: Path):
    print(f'"{path.absolute()}" is_dir: {path.is_dir()}: is_exists:{path.exists()}')
    if path.is_dir():
        return f'view/{quote(str(path))}'
    else:
        return f'img/{quote(str(path))}'


def get_directory_list(directory_path: Path):
    if directory_path.exists() and directory_path.is_dir():
        return [path for path in sorted(directory_path.iterdir())]
    else:
        return []
