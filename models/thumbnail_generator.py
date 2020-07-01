from pathlib import Path
from PIL import Image
import imghdr
from urllib.parse import quote


def generate_thumbnail(file_path: str) -> str:
    '''
    入力された画像ファイルを読み込んで、サムネイルを作成し、そのパスを返す。

    Args:
        file_path:　サムネイルを作りたい画像ファイルのパス

    return:
        作成したサムネイルのパス
    '''
    path = Path(file_path)

    if path.is_file():
        thumbnail_folder = get_thumbnail_folder(str(path))
        thumbnail_path = Path(thumbnail_folder) / Path(path.name)
        picture_file_type = imghdr.what(file_path)
        if not thumbnail_path.exists() and picture_file_type is not None:
            image = Image.open(file_path)
            image.thumbnail((256, 256))
            image.save(thumbnail_path, picture_file_type)
        elif picture_file_type is None:
            return ('/image/file_icon.png')
        return f'thumbnail/{quote(file_path)}'
    else:
        return ('/image/folder_icon.png')


def get_thumbnail_folder(filePath: str):
    '''
    thumbnailフォルダパスを取得する。ない場合は、作成する。
    '''
    thumbnail_directory = Path(filePath).parent / '.thumbnail'
    if not (thumbnail_directory).exists():
        thumbnail_directory.mkdir()
    return str(thumbnail_directory)
