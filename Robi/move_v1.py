move = input('What Direction would you like to move?\n')

upper = move.upper()

f = upper.count("F")
l = upper.count("L")
r = upper.count("R")

print("forward = " + str(f))
print("Left = " + str(l))
print("Right = " + str(r))