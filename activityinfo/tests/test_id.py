from unittest import TestCase

import activityinfo


class Test(TestCase):
    def test_generate_id(self):
        new_id = activityinfo.generate_id()
        self.assertTrue(len(new_id) > 5)

    def test_cuid_counter(self):
        """Test to ensure that the counter in the CUID generator is global and therefore incremented at each call to
        cuid_counter() """
        old_value = activityinfo.id.cuid_counter()
        new_value = activityinfo.id.cuid_counter()
        self.assertTrue(new_value >= old_value + 1)
