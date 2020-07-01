import tempfile
from unittest import TestCase
from models import thumbnail_generator
from pathlib import Path
from tests import helper


class testThumbnailGenerator(TestCase):
    def test_ファイルのとき生成したサムネイル保存先パスが返る(self):
        with tempfile.TemporaryDirectory() as tmp:
            helper.generate_sample_picture(tmp)
            expect = '.thumbnail/sample00.png'
            actual = thumbnail_generator.generate_thumbnail(f'{tmp}/sample00.png')
            self.assertEqual(expect, actual)

    def test_ディレクトリのときフォルダ用のサムネイル画像パスが返る(self):
        with tempfile.TemporaryDirectory() as tmp:
            target_directory = (Path(tmp) / 'sample')
            target_directory.mkdir()
            expect = '/image/folder_icon.png'
            actual = thumbnail_generator.generate_thumbnail(str(target_directory))
            self.assertEqual(expect, actual)

    def test_画像ファイル以外のときファイル用のサムネイル画像パスが返る(self):
        with tempfile.TemporaryDirectory() as tmp:
            target_directory = (Path(tmp) / 'sample.txt')
            target_directory.touch()
            expect = '/image/file_icon.png'
            actual = thumbnail_generator.generate_thumbnail(str(target_directory))
            self.assertEqual(expect, actual)