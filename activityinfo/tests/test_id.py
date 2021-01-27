from unittest import TestCase

import activityinfo


class Test(TestCase):
    def test_generate_id(self):
        new_id = activityinfo.generate_id()
        self.assertTrue(len(new_id) > 5)
