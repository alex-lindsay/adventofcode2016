import math

# instructionString = "R8, R4, R4, R8"
instructionString = "L4, L1, R4, R1, R1, L3, R5, L5, L2, L3, R2, R1, L4, R5, R4, L2, R1, R3, L5, R1, L3, L2, R5, L4, L5, R1, R2, L1, R5, L3, R2, R2, L1, R5, R2, L1, L1, R2, L1, R1, L2, L2, R4, R3, R2, L3, L188, L3, R2, R54, R1, R1, L2, L4, L3, L2, R3, L1, L1, R3, R5, L1, R5, L1, L1, R2, R4, R4, L5, L4, L1, R2, R4, R5, L2, L3, R5, L5, R1, R5, L2, R4, L2, L1, R4, R3, R4, L4, R3, L4, R78, R2, L3, R188, R2, R3, L2, R2, R3, R1, R5, R1, L1, L1, R4, R2, R1, R5, L1, R4, L4, R2, R5, L2, L5, R4, L3, L2, R1, R1, L5, L4, R1, L5, L1, L5, L1, L4, L3, L5, R4, R5, R2, L5, R5, R5, R4, R2, L1, L2, R3, R5, R5, R5, L2, L1, R4, R3, R1, L4, L2, L3, R2, L3, L5, L2, L2, L1, L2, R5, L2, L2, L3, L1, R1, L4, R2, L4, R3, R5, R3, R4, R1, R5, L3, L5, L5, L3, L2, L1, R3, L4, R3, R2, L1, R3, R1, L2, R4, L3, L3, L3, L1, L2"
instructions = instructionString.split(', ')

orientation = 90
x = 0
y = 0

visitedLocations = [(0,0)]
answer2 = False

for instruction in instructions:
    print x, y, orientation, instruction
    turn = instruction[0]
    orientation = (orientation + (turn == 'L' and 90 or -90)) % 360

    distance = int(instruction[1:])

    xincr = math.trunc(math.sin(math.radians(orientation)))
    yincr = math.trunc(math.cos(math.radians(orientation)))

    if not answer2:
        for i in range(1, distance+1):
            x += xincr
            y += yincr
            try:
                visitedLocations.index((x, y))
                print "Here's the index:"
                print visitedLocations.index((x, y))
                print
                print
                print
                answer2 = "Day 1 second answer is: (%d, %d) %d" % (x, y, x + y)
            except ValueError:
                visitedLocations.append((x, y))

    print visitedLocations[-5:]
    print instruction, orientation, x, y
    print


print "Day 1 answer is: %d " % (x + y)
print answer2
