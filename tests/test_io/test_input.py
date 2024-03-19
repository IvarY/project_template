import unittest
import pandas as pd
import os

from app.io.input import read_console, read_file, read_file_pandas


class TestReadFunctions(unittest.TestCase):
    def test_read_file(self):
        test_file_path = 'test_file.txt'
        test_content = 'Test content from file'
        with open(test_file_path, 'w') as file:
            file.write(test_content)
        self.assertEqual(read_file(test_file_path), test_content)
        os.remove(test_file_path)

    def test_read_file_pandas_csv(self):
        test_csv_file_path = 'test_data.csv'
        test_data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        test_data.to_csv(test_csv_file_path, index=False)
        result = read_file_pandas(test_csv_file_path)
        pd.testing.assert_frame_equal(result, test_data)
        os.remove(test_csv_file_path)

    def test_read_file_pandas_json(self):
        test_json_file_path = 'test_data.json'
        test_data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        test_data.to_json(test_json_file_path, orient='records')
        result = read_file_pandas(test_json_file_path)
        pd.testing.assert_frame_equal(result, test_data)
        os.remove(test_json_file_path)

    def test_read_file_pandas_invalid_format(self):
        with self.assertRaises(ValueError):
            read_file_pandas('invalid_file.txt')


if __name__ == "__main__":
    unittest.main()