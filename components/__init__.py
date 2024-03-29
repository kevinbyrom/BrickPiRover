from abc import ABC, abstractmethod

class ComponentBase():
    def __init__(self, rover):
        self.rover = rover
        super().__init__()

    @abstractmethod
    def startup(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def shutdown(self):
        pass