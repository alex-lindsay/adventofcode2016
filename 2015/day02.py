# input = """2x3x4
# 1x1x10"""

inputFile = 'day02_input.txt'
inputF = open(inputFile, 'r')
input = inputF.read()

inputRows = input.split()

print 'inputRows', inputRows

total = 0
for inputRow in inputRows:
    dims = inputRow.split('x')
    print 'dims', dims
    sides = []
    for index1, dim1 in enumerate(dims):
        for index2, dim2 in enumerate(dims):
            if index1 != index2:
                sides.append(int(dim1) * int(dim2))
        extra = min(sides)
        print 'sides', sides
    packageTotal = sum(sides) + extra
    total += packageTotal
    print 'packageTotal', packageTotal, 'total', total
