
from abc import ABC, abstractmethod


class OrderState(ABC):

    @abstractmethod
    def confirm(self, order):
        pass

    @abstractmethod
    def ship(self, order):
        pass

    @abstractmethod
    def deliver(self, order):
        pass

    @abstractmethod
    def cancel(self, order):
        pass
