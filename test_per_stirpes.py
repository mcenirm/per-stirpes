import unittest

import per_stirpes


class PerStirpesTests(unittest.TestCase):
    def test_main_can_launch_a_process(self):
        returncode = per_stirpes.main(['true'])
        self.assertEqual(0, returncode, 'true command should have exit status 0')
        returncode = per_stirpes.main(['false'])
        self.assertNotEqual(0, returncode, 'false command should not have exit status 0')
