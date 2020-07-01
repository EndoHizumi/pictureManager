import os

from PIL import Image


def generate_sample_picture(directory_path: str, count: int = 1) -> None:
    '''テスト用の画像ファイルを生成する
        Args:
            file_path: 画像ファイルの保存先
            count: 生成するファイル数
    '''
    for index in range(count):
        file_path = os.path.join(directory_path, f'sample{str(index).zfill(2)}.png')
        pic = Image.new('RGB', (500, 300), (128, 128, 128))
        pic.save(file_path)
