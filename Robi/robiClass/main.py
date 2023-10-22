from robi import Robi
from bonus import Bonus

def main():
    robi = Robi()
    bonus = Bonus()

    movement = input('Enter Command\n')
    move = movement.upper()

    i = 0
    while i < len(move):
        command = move[i]

        if command == 'F':
            distance = ''
            i += 1

            while i < len(move) and move[i].isdigit():
                distance += move[i]
                i += 1

            if distance:
                distance = int(distance)
                robi.move(command, distance)
            if i < len(move) and not move[i].isdigit():
                i -= 1
        else:
            robi.move(command, 0)


        bonus.checkCollected(robi.x, robi.y)

        i += 1
        
    if bonus.collected:
        robi.bonus_collected = 1

    print(f"Result: X:{robi.x}, Y:{robi.y}, D:{robi.direction}, B:{robi.bonus_collected}")
    print(bonus.x,bonus.y)

if __name__ == "__main__":
    main()
