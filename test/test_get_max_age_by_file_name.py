import unittest

from main import _get_max_age_by_file_name


class GetMaxAgeByFileNameTest(unittest.TestCase):
    def test_get_max_age_by_file_name(self):
        # html max 5min
        self.assertEqual(_get_max_age_by_file_name("abc.html"), 300)
        # png, css, js max 1 year
        self.assertEqual(_get_max_age_by_file_name("abc.png"), 31536000)
        self.assertEqual(_get_max_age_by_file_name("abc.css"), 31536000)
        self.assertEqual(_get_max_age_by_file_name("abc.js"), 31536000)
        # default 1 year
        self.assertEqual(_get_max_age_by_file_name("abc"), 31536000)
        self.assertEqual(_get_max_age_by_file_name("abc.txt"), 31536000)
