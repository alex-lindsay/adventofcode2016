from collections import Counter

# input = """eedadn
# drvtee
# eandsr
# raavrd
# atevrs
# tsrnev
# sdttsa
# rasrtv
# nssdts
# ntnada
# svetve
# tesnvt
# vntsnd
# vrdear
# dvrsen
# enarar"""

inputFile = 'day06_input.txt'
inputF = open(inputFile, 'r')
input = inputF.read()

instructions = input.split("\n")
instructions = instructions[:-1]
print instructions
positions = []
for i in range(len(instructions[0])):
    positions.append(Counter([instruction[i] for instruction in instructions]).most_common(1))

print positions
print ''.join([item[0][0] for item in positions])
# print [position.keys()[0] for position in positions]
