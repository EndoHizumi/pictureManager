from unittest import TestCase, mock
from models import file_list_worker
from urllib.parse import quote


class testHandle(TestCase):

    @mock.patch("models.file_list_worker.get_directory_list")
    def test_指定したファイルとその前とその次のJSONファイルが返ってくる(self, mock_get_directory_list):
        mock_get_directory_list.return_value = [
            "./file1.png",
            "./file2.png",
            "./file3.png",
        ]
        expect_json = {
            "name": "file2.png",
            "path": f'img/./{quote("file2.png")}',
            "prev": f'view/./{quote("file1.png")}',
            "next": f'view/./{quote("file3.png")}',
            "parent": "view/."
        }
        file_info_json = file_list_worker.handle('./file2.png')
        self.assertEqual(expect_json, file_info_json)

    @mock.patch("models.file_list_worker.get_directory_list")
    def test_指定したファイルとその前とその次のJSONファイルが返ってくる2(self, mock_get_directory_list):
        mock_get_directory_list.return_value = [
            "./img/file1.png",
            "./img/file2.png",
            "./img/file3.png",
        ]
        expect_json = {
            "name": "file2.png",
            "path": f'img/{quote("img/file2.png")}',
            "prev": f'view/{quote("img/file1.png")}',
            "next": f'view/{quote("img/file3.png")}',
            "parent": "view/img/"
        }
        file_info_json = file_list_worker.handle('./img/file2.png')
        self.assertEqual(expect_json, file_info_json)
