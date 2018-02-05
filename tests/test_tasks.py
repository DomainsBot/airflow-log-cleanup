import pathlib

from pyfakefs import fake_filesystem_unittest


from log_cleanup.tasks import cleanup_by_pattern


class TasksTestCase(fake_filesystem_unittest.TestCase):

    def setUp(self):
        self.setUpPyfakefs()

    def tearDown(self):
        # It is no longer necessary to add self.tearDownPyfakefs()
        pass

    def test_when_a_directory_is_passed_then_it_deletes_correct_dirs(self):
        base_dir = '/madir'
        delete_prefix = 'to_delete'
        files = [
            '/loper.py',
            '/safe/hiper.py',
            '/%s_1/log.log' % delete_prefix,
            '/safe/%s_2/log.log' % delete_prefix,
            '/safe/safe/%s_3/log.log' % delete_prefix
        ]

        for _file in files:
            self.fs.CreateFile(base_dir + _file)

        safe_paths = []
        for p in pathlib.Path(base_dir).rglob('*'):
            if delete_prefix not in str(p):
                safe_paths.append(p)

        cleanup_by_pattern('/madir', 'to_delete*')

        remaining_paths = list(pathlib.Path('/madir').rglob('*'))

        self.assertEqual(safe_paths, remaining_paths)
