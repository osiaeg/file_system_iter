import os
import fnmatch

class FileSystemIterator:

    def __init__(self, root: str, only_files: bool, only_dirs: bool, pattern=None):
        '''
        Инициализация объекта

        :param root:
        :param only_files:
        :param only_dirs:
        :param pattern:
        '''
        self.root = root
        self._pattern = pattern
        self._create_generator(only_files, only_dirs)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.generator)

    def _check_pattern(self, iterable, addres):
        for item in iterable:
            if not self._pattern is None:
                if fnmatch.fnmatch(item, self._pattern):
                    yield os.path.join(addres, item)
            else:
                yield os.path.join(addres, item)

    def _gen_only_dirs(self):
        for addr, dirs, files in os.walk(self.root):
            yield from self._check_pattern(dirs, addr)

    def _gen_only_files(self):
        files = next(os.walk(self.root))[2]
        yield from self._check_pattern(files, self.root)

    def _gen_all(self):
        for addr, dirs, files in os.walk(self.root):
            yield from self._check_pattern(files, addr)

    def _create_generator(self, only_files, only_dirs):
        if only_files and not only_dirs:
            self.generator = self._gen_only_files()
        elif only_dirs and not only_files:
            self.generator = self._gen_only_dirs()
        else:
            self.generator = self._gen_all()

