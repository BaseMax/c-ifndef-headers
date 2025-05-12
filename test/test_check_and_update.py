import unittest
from utils import generate_guard_name, update_file
import tempfile
import os

class TestFileUpdate(unittest.TestCase):

    def test_generate_guard_name(self):
        file_path = 'utility/utf8/utf8_char_decode/utf8_char_decode.h'
        expected_guard = '_UTILITY_UTF8_UTF8_CHAR_DECODE_UTF8_CHAR_DECODE_H_'
        guard_name = generate_guard_name(file_path)
        self.assertEqual(guard_name, expected_guard)

    def test_update_file(self):
        with tempfile.NamedTemporaryFile(delete=False, mode='w') as temp_file:
            temp_file.write('Some content\n')
            file_path = temp_file.name

        guard_name = '_TEST_FILE_UPDATE_TEST_FILE_UPDATE_H_'
        update_file(file_path, guard_name)

        with open(file_path, 'r') as f:
            content = f.read()
            self.assertIn(f"#ifndef {guard_name}", content)
            self.assertIn(f"#endif // {guard_name}", content)

        os.remove(file_path)

if __name__ == '__main__':
    unittest.main()
