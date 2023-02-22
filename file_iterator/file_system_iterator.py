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
        self._root = root
        self._pattern = pattern
        self._generator = self._create_generator(only_files, only_dirs)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self._generator)

    def _check_pattern(self, iterable, addres):
        for item in iterable:
            if not self._pattern is None:
                if fnmatch.fnmatch(item, self._pattern):
                    yield os.path.join(addres, item)
            else:
                yield os.path.join(addres, item)

    def _create_generator(self, only_files, only_dirs):
        for addr, dirs, files in os.walk(self._root):
            if only_files and not only_dirs:
                yield from self._check_pattern(files, addr)
            elif only_dirs and not only_files:
                yield from self._check_pattern(dirs, addr)
            else:
                yield from self._check_pattern(files, addr)
                yield from self._check_pattern(dirs, addr)

