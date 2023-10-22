class Robi:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = 'T'
        self.bonus_collected = 0 

    def move(self, command, distance):
        if command == 'L':
            self.turnLeft()
        elif command == 'R':
            self.turnRight()
        elif command == 'F':
            self.moveForward(distance)

    def turnLeft(self):
        if self.direction == 'T':
            self.direction = 'L'
        elif self.direction == 'L':
            self.direction = 'B'
        elif self.direction == 'B':
            self.direction = 'R'
        else:
            self.direction = 'T'

    def turnRight(self):
        if self.direction == 'T':
            self.direction = 'R'
        elif self.direction == 'R':
            self.direction = 'B'
        elif self.direction == 'B':
            self.direction = 'L'
        else:
            self.direction = 'T'

    def moveForward(self, distance):
        if self.direction == 'T':
            self.y += distance
        elif self.direction == 'B':
            self.y -= distance
        elif self.direction == 'L':
            self.x -= distance
        else:
            self.x += distance
