import unittest

from gpt_traceback.prompt import predict_prompt


class TestSimple(unittest.TestCase):

    def test_add(self):
        self.assertNotEqual(predict_prompt, None)


if __name__ == '__main__':
    unittest.main()
