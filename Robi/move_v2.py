movement = input('Enter Command\n')

move = movement.upper()

X = 0
Y = 0
D = 'T' 
B = 0

i = 0

while i < len(move):
    command = move[i]

    if command == 'L':
        if D == 'T':
            D = 'L'
        elif D == 'L':
            D = 'B'
        elif D == 'B':
            D = 'R'
        else:
            D = 'T'
            
    elif command == 'R':
        if D == 'T':
            D = 'R'
        elif D == 'R':
            D = 'B'
        elif D == 'B':
            D = 'L'
        else:
            D = 'T'
            
    elif command == 'F':
        distance = ''
        i += 1

        while i < len(move) and move[i].isdigit():
            distance += move[i]
            i += 1


        if distance:
            distance = int(distance)
            if D == 'T':
                Y += distance
            elif D == 'B':
                Y -= distance
            elif D == 'L':
                X -= distance
            else:
                X += distance
                
        if i < len(move) and not move[i].isdigit():
            i -= 1

    i += 1

print(f"Result:  X:{X}, Y:{Y}, D:{D}")
