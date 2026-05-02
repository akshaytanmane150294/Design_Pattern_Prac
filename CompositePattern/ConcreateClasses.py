

from baseInterface import *

# Leaf node


class File(FileSystemItem):

    def __init__(self, name: str, size: int):
        self._name = name
        self._size = size

    def getName(self):
        return self._name

    def getSize(self):
        return self._size

    def show(self, indent: str):
        print(f'{indent} {self._name} ({self._size}) KB')

# Composite node  - Folder


class Folder(FileSystemItem):
    def __init__(self, name):
        self._name = name
        self._children = []

    def add(self, item: FileSystemItem):
        self._children.append(item)
        return self

    def remove(self, item: FileSystemItem):
        self._children.remove(item)

    def getName(self):
        return self._name

    def getSize(self):
        return sum(child.getSize() for child in self._children)

    def show(self, indent=""):
        print(f"{indent} {self._name}/")

        for child in self._children:
            child.show(indent+" ")


root = Folder('Project')
root.add(File('Readme.md', 2))
root.add(File('.gitignore', 1))


src = Folder('src')
src.add(File('main.py', 15))
src.add(File('utils.py', 8))

tests = Folder('tests')
tests.add(File('test_main.py', 12))

src.add(tests)
root.add(src)
root.show()
