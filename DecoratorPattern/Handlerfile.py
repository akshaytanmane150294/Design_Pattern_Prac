

from abc import ABC, abstractmethod
# Base Interface


class Handler:
    # No implementation → behaves like interface
    @abstractmethod
    def handle(self, request: dict):
        pass
