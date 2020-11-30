import unittest
import states_itax as states


class TestStates(unittest.TestCase):

    def test_AL(self):
        self.assertEqual(states.calculate_itaxes(0, 'AL'), 0)
        self.assertEqual(states.calculate_itaxes(400, 'AL'), 8.0)
        self.assertEqual(states.calculate_itaxes(700, 'AL'), 18.0)
        self.assertEqual(states.calculate_itaxes(20000, 'AL'), 960.0)
        self.assertEqual(states.calculate_itaxes(100000, 'AK'), 0)


if __name__ == '__main__':
    unittest.main()
