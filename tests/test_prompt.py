import unittest

from gpt_traceback.prompt import predict_prompt


class TestSimple(unittest.TestCase):

    def test_add(self):
        def iscallable():
            return callable(predict_prompt)
        self.assertEqual(iscallable, True)


if __name__ == '__main__':
    unittest.main()
