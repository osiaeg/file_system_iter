import os

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
        self._create_generator(only_files, only_dirs)

    def __iter__(self):
        return self.generator

    def __next__(self):
        return next(self.generator)

    def _gen_only_dirs(self):
        for addr, dirs, files in os.walk(self.root):
            for name in dirs:
                yield os.path.join(addr, name)

    def _gen_only_files(self):
        for addr, dirs, files in os.walk(self.root):
            for name in files:
                yield os.path.join(addr, name)

    def _gen_all(self):
        pass

    def _create_generator(self, only_files, only_dirs):
        if only_files:
            self.generator = self._gen_only_files()
        elif only_dirs:
            self.generator = self._gen_only_dirs()
        else:
            self.generator = self._gen_all()



if __name__ == '__main__':
    root = '/home/osia/Documents/code/Python3/file_system_iter/tree'

    for item in FileSystemIterator(root, False, True, None):
        print(item)

    print('#' * 50)

    print(next(FileSystemIterator(root, False, True, None)))
