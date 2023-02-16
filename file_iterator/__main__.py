from .file_system_iterator import FileSystemIterator
root = './tests/tree'

for item in FileSystemIterator(root, False, False, None):
    print(item)

print('#' * 50)

for item in FileSystemIterator(root, True, False, None):
    print(item)

print('#' * 50)

for item in FileSystemIterator(root, False, True, None):
    print(item)

print('#' * 50)

for item in FileSystemIterator(root, False, False, '*.csv'):
    print(item)

print('#' * 50)

for item in FileSystemIterator(root, True, False, '*.csv'):
    print(item)

print('#' * 50)

for item in FileSystemIterator(root, False, True, 'inner*'):
    print(item)

