import pathlib
import shutil


def cleanup_by_pattern(base_folder, pattern):
    paths = pathlib.Path(base_folder).rglob(pattern)
    for path in paths:
        if not path.is_file():
            shutil.rmtree(path)
