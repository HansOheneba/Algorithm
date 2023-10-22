class Pet:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def intro(self):
        print(self.name + " is a " + self.desc)
