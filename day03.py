inputFile = 'day03_input.txt'

def processInput(inputFile):
    input = open(inputFile, 'r')
    possibles = 0
    rows = 0

    for line in input:
        rows += 1
        values = line.split()
        # print 'line', line.strip()
        # print 'values', values
        values = [int(value) for value in values]
        values.sort()
        if values[0] + values[1] > values[2]:
            possibles += 1
        print 'values', values, possibles

    return (rows, possibles)

print "Day 3 answer: "
print processInput(inputFile)
