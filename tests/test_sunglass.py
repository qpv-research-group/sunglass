import unittest


class ExampleTestCase(unittest.TestCase):
    def test_nothing(self):
        self.assertEqual(True, True)


if __name__ == "__main__":
    unittest.main()
