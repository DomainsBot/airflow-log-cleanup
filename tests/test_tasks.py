import pathlib
import re
from datetime import date, timedelta

from pyfakefs import fake_filesystem_unittest


from airflow_log_cleanup.tasks import cleanup_before_date


class TasksTestCase(fake_filesystem_unittest.TestCase):

    def setUp(self):
        self.setUpPyfakefs()

    def tearDown(self):
        # It is no longer necessary to add self.tearDownPyfakefs()
        pass

    def test_when_a_directory_is_passed_then_it_deletes_correct_dirs(self):
        base_dir = '/madir'
        today = date.today()
        yesterday = today - timedelta(days=1)
        two_days_ago = today - timedelta(days=2)
        three_days_ago = today - timedelta(days=3)
        pattern = r'(?P<year>[0-9]{4})-(?P<month>[0-9]{2})-(?P<day>[0-9]{2})'
        files = [
            '/loper.py',
            '/{day:%Y-%m-%d}/hiper.py'.format(day=today),
            '/{day:%Y-%m-%d}/log.log'.format(day=yesterday),
            '/safe/{day:%Y-%m-%d}/log.log'.format(day=two_days_ago),
            '/safe/safe/{day:%Y-%m-%d}/log.log'.format(day=three_days_ago)
        ]

        for _file in files:
            self.fs.CreateFile(base_dir + _file)

        safe_paths = []
        for path in pathlib.Path(base_dir).rglob('*'):
            match = re.search(pattern, str(path))
            if match is None:
                safe_paths.append(path)
            else:
                dir_date = date(
                    year=int(match.group('year')),
                    month=int(match.group('month')),
                    day=int(match.group('day')),
                )
                if dir_date > yesterday:
                    safe_paths.append(path)
        print(safe_paths)
        cleanup_before_date('/madir', pattern, yesterday)

        remaining_paths = list(pathlib.Path('/madir').rglob('*'))

        self.assertEqual(safe_paths, remaining_paths)
