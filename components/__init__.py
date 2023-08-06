from abc import ABC, abstractmethod

class ComponentBase():
    def __init__(self, rover):
        self.rover = rover
        super().__init__()

    @abstractmethod
    def update(self):
        pass
