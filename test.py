import os
import sys
import json
import subprocess
import unittest

BASE_PATH = os.path.dirname(os.path.abspath(__name__))
TEST_PACKAGE_PATH = os.path.join(BASE_PATH, 'testpkg')


class DevpiTestCase(unittest.TestCase):
    def setUp(self):
        self.old_argv_val = sys.argv
        self.basic_input = {
            "workspace": {
                "path": TEST_PACKAGE_PATH,
            },
            "vargs": {
                "server": "http://localhost:3141/",
                "index": "root/production",
                "username": "root",
                "password": "",
            }
        }

    def tearDown(self):
        sys.argv = self.old_argv_val

    def _create_index(self, index):
        subprocess.run(['devpi', 'index', '-c', index])

    def test_upload(self):
        self._create_index('production')
        sys.argv = ['--', json.dumps(self.basic_input)]
        from run_devpi import main
        main()


if __name__ == '__main__':
    unittest.main()
