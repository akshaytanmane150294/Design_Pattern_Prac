
from abc import ABC, abstractmethod
from typing import List


class FileSystemItem(ABC):
    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def getSize(self):
        pass

    @abstractmethod
    def show(self, indent: str = ""):
        pass
