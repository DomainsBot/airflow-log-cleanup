import pathlib
import re
import shutil

import pendulum


def cleanup_before_date(base_folder: pathlib.Path | str, pattern: str, days_ago: int) -> None:
    before_date = pendulum.today(tz="UTC").subtract(days=days_ago)
    paths = pathlib.Path(base_folder).rglob('*')
    dirs = (path for path in paths if path.is_dir())
    for dir_ in dirs:
        match = re.search(pattern, str(dir_))
        if match is not None:
            dir_date = pendulum.date(
                year=int(match.group('year')),
                month=int(match.group('month')),
                day=int(match.group('day'))
            )
            if dir_date <= before_date:
                shutil.rmtree(dir_)
