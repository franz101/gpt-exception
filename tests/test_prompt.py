import unittest


class TestSimple(unittest.TestCase):

    def test_example(self):

        self.assertEqual((Number(5) + Number(6)).value, 11)


if __name__ == '__main__':
    unittest.main()
