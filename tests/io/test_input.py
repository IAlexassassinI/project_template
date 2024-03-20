import unittest
import os
import app.io.input as inp


class TestInputFunctions(unittest.TestCase):
    def setUp(self):
        self.test_content = "Test Test TEST TEST 123 123 12 \n123 123 14 12 1 Test Test"
        self.test_content_csv = "Name Num Var\nAAA 123 BBB\nCCC 321 DDD\nEEE 232 FFF"
        self.csv_correct_header = ["Name", "Num", "Var"]
        self.csv_correct = [["AAA", 123, "BBB"], ["CCC", 321, "DDD"], ["EEE", 232, "FFF"]]
        self.non_existing_file = "non_existing_file.txt"

        self.test_file_path = '../../data/test_file.txt'
        self.test_file_path_csv = '../../data/test_file.csv'
        self.test_file_path_empty = '../../data/empty_file.txt'

        with open(self.test_file_path, 'w') as file:
            file.write(self.test_content)

        with open(self.test_file_path_csv, 'w') as file:
            file.write(self.test_content_csv)

        with open(self.test_file_path_empty, 'w') as file:
            file.write("")

    def tearDown(self):
        os.remove(self.test_file_path)
        os.remove(self.test_file_path_csv)
        os.remove(self.test_file_path_empty)

    def test_read_file(self):
        readed_content = inp.read_file(self.test_file_path)
        self.assertEqual(self.test_content, readed_content)

    def test_read_file_not_found(self):
        readed_content = inp.read_file(self.non_existing_file)
        self.assertIsNone(readed_content)

    def test_read_file_empty(self):
        readed_content = inp.read_file(self.test_file_path_empty)
        self.assertEqual("", readed_content)

    def test_read_file_pandas(self):
        readed_content = inp.read_file_pandas(self.test_file_path_csv)
        self.assertListEqual(self.csv_correct_header, list(readed_content.columns))
        self.assertEqual(self.csv_correct, readed_content.values.tolist())

    def test_read_file_pandas_not_found(self):
        readed_content = inp.read_file_pandas(self.non_existing_file)
        self.assertIsNone(readed_content)

    def test_read_file_pandas_empty(self):
        readed_content = inp.read_file_pandas(self.test_file_path_empty)
        self.assertIsNone(readed_content)


if __name__ == '__main__':
    unittest.main()
