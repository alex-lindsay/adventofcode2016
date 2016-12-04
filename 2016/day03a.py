inputFile = 'day03_input.txt'

def processInput(inputFile):
    input = open(inputFile, 'r')
    possibles = 0
    rows = 0

    triangles = [[],[],[]]

    for line in input:
        rows += 1
        values = line.split()
        # print 'line', line.strip()
        # print 'values', values
        values = [int(value) for value in values]

        for index, value in enumerate(values):
            triangles[index].append(value)

        if rows % 3 != 0:
            continue

        for triangle in triangles:
            triangle.sort()
            if triangle[0] + triangle[1] > triangle[2]:
                possibles += 1
            print 'triangle', triangle, possibles
        triangles = [[],[],[]]

    return (rows, possibles)

print "Day 3 answer: "
print processInput(inputFile)
