inputFile = 'day01_input.txt'

def processInput(inputFile):
    input = open(inputFile, 'r')

    inputData = input.read()

    # ups = inputData.count('(')
    # dns = inputData.count(')')
    #
    # result = ups - dns

    currentFloor = 0
    position = 0
    while (currentFloor != -1) and (position < len(inputData)):
        position +=1
        currentFloor += (inputData[position-1] == '(') and 1 or -1
        print position, inputData[position-1], currentFloor

    result = position

    return result

print "Day 1 answer: "
print processInput(inputFile)
