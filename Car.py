import random

class Car:
    def __init__(self, id) -> None:
        self.id = id
        self.time = random.randint(1, 5)
