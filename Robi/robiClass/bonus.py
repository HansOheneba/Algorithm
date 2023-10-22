import random


class Bonus:
    def __init__(self):

        self.x = random.randint(-100, 100)
        self.y = random.randint(-100, 100)
        self.collected = False

    def checkCollected(self, robiX, robiY):

        if robiX == self.x and robiY == self.y:
            self.collected = True
