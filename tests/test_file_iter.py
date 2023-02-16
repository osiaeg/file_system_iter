import unittest, os, fnmatch
from file_iterator import FileSystemIterator as iterator

class TestFileIterator(unittest.TestCase):
    root = './tests/tree'

    def test_all_without_pattern(self):
        expected_files = []

        for addres, dirs, files in os.walk(self.root):
            for name in files:
                expected_files.append(os.path.join(addres, name))

        generated_files = [path for path in iterator(self.root, False, False)]
        self.assertEqual(sorted(expected_files), sorted(generated_files))

    def test_only_files(self):
        expected_files = []

        files = next(os.walk(self.root))[2]
        for file in files:
            expected_files.append(os.path.join(self.root, file))

        generated_files = [path for path in iterator(self.root, True, False)]
        self.assertEqual(sorted(expected_files), sorted(generated_files))

    def test_only_dirs(self):
        expected_files = []

        for addres, dirs, files in os.walk(self.root):
            for name in dirs:
                expected_files.append(os.path.join(addres, name))

        generated_files = [path for path in iterator(self.root, False, True)]
        self.assertEqual(sorted(expected_files), sorted(generated_files))

    def test_only_dirs_with_pattern(self):
        expected_files = []
        pattern = '*.csv'

        for addres, dirs, files in os.walk(self.root):
            for name in dirs:
                if fnmatch.fnmatch(name, pattern):
                    expected_files.append(os.path.join(addres, name))

        generated_files = [path for path in iterator(self.root, False, True, pattern)]
        self.assertEqual(sorted(expected_files), sorted(generated_files))

    def test_all_with_pattern(self):
        expected_files = []
        pattern = '*.csv'

        for addres, dirs, files in os.walk(self.root):
            for name in files:
                if fnmatch.fnmatch(name, pattern):
                    expected_files.append(os.path.join(addres, name))

        generated_files = [path for path in iterator(self.root, False, False, pattern)]
        self.assertEqual(sorted(expected_files), sorted(generated_files))

    def test_only_files_with_pattern(self):
        expected_files = []
        pattern = '*.csv'

        files = next(os.walk(self.root))[2]
        for file in files:
            if fnmatch.fnmatch(file, pattern):
                expected_files.append(os.path.join(self.root, file))

        generated_files = [path for path in iterator(self.root, True, False, pattern)]
        self.assertEqual(sorted(expected_files), sorted(generated_files))
