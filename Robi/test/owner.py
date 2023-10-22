class Owner:
    def __init__(self, name, age, out):
        self.name = name
        self.age = age
        self.isOut = out
        self.petsOwned = []

    def goOut(self):
        self.isOut = True

    def goIn(self):
        self.isOut = False
