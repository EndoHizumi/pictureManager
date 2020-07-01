import os
import tempfile
from unittest import TestCase

from models import directory_list_worker
from tests import helper
from pathlib import Path


class testHandle(TestCase):
    def test_ディレクトリを指定した場合(self):
        self.maxDiff = None
        item_count = 1
        with tempfile.TemporaryDirectory(dir='.') as tmp:
            expect_json = {
                "directoryPath": tmp,
                "count": item_count,
                "data": [
                    {
                        "name": "sample00.png",
                        "path": f"{os.path.basename(tmp)}/.thumbnail/sample00.png"
                    }
                ]
            }
            helper.generate_sample_picture(tmp, item_count)
            actual_json = directory_list_worker.handle(tmp)
            self.assertEqual(expect_json, actual_json)

    def test_ファイルを指定した場合(self):
        self.maxDiff = None
        item_count = 0
        with tempfile.TemporaryDirectory(dir='.') as tmp:
            expect_json = {
                "directoryPath": f"{os.path.basename(tmp)}/sample00.png",
                "count": item_count,
                "data": []
            }
            helper.generate_sample_picture(tmp, item_count)
            actual_json = directory_list_worker.handle(f"{os.path.basename(tmp)}/sample00.png")
            self.assertEqual(expect_json, actual_json)


class testGetDirectoryList(TestCase):

    def test_ディレクトリを渡した時ファイルの一覧が返る(self):
        self.maxDiff = None
        with tempfile.TemporaryDirectory(dir='.') as tmp:
            expect_list = [Path(tmp) / 'sample00.png', Path(tmp) / 'sample01.png', Path(tmp) / 'sample02.png']
            # サンプル画像を生成する
            helper.generate_sample_picture(tmp, 3)
            # ディレクトリの一覧を取得する
            tmp_path = Path(f'./{tmp}')
            directory_list = directory_list_worker.get_directory_list(tmp_path)
            self.assertEqual(expect_list, directory_list)

    def test_ファイルを渡した時Noneが返る(self):
        self.maxDiff = None
        with tempfile.TemporaryDirectory() as tmp:
            # サンプル画像を生成する
            helper.generate_sample_picture(tmp)
            # ディレクトリの一覧を取得する
            directory_list = directory_list_worker.get_directory_list(Path(tmp) / 'sample00.png')
            self.assertFalse(directory_list)
