import os
import pathlib
import re
import shutil
from datetime import date


def cleanup_before_date(base_folder, pattern, before_date):
    paths = pathlib.Path(base_folder).rglob('*')
    for path in paths:
        if path.is_dir():
            match = re.search(pattern, str(path))
            if match is not None:
                dir_date = date(
                    year=int(match.group('year')),
                    month=int(match.group('month')),
                    day=int(match.group('day'))
                )
                if dir_date <= before_date:
                    shutil.rmtree(path)
