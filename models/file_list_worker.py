from pathlib import Path
import glob
from typing import Dict
from urllib.parse import quote


def handle(file_path: str) -> Dict:
    parent_path = Path(file_path).parent
    directory_path = get_directory_list(parent_path)
    print(directory_path)
    target_index = directory_path.index(file_path)

    return {
        "name": Path(file_path).name,
        "path": f'img/{quote(directory_path[target_index])}',
        "prev": f'view/{quote(directory_path[target_index -1])}',
        "next": f'view/{quote(directory_path[target_index +1])}',
        "parent": f"view/{parent_path}/"
    }


def get_directory_list(directory_path: Path):
    if directory_path.exists() and directory_path.is_dir():
        return glob.glob(glob.escape(str(directory_path)) + '/*')
    else:
        return []
