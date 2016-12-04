import re
inputFile = 'day04_input.txt'

def createChecksum(char_count):
    sort = [v[0] for v in sorted(char_count.items(), key=lambda(k,v): (-v,k))]
    return ''.join(sort)[0:5]

def processInput(inputFile):
    valid_room_total = 0
    input = open(inputFile, 'r')
    for line in input:
        char_count = {}
        # print line
        matches = re.match(r"([-a-z]+)([0-9]+)\[([a-z]{5})\]", line)
        # print matches.group(1)
        # print matches.group(2)
        # print matches.group(3)
        # print

        for char in matches.group(1):
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        del char_count['-']
        checksum = createChecksum(char_count)
        if checksum == matches.group(3):
            # print char_count
            valid_room_total += int(matches.group(2))
            decoded = ""
            for char in matches.group(1):
                if char == '-':
                    decoded += ' '
                else:
                    new_char = ((ord(char) - ord('a') + int(matches.group(2))) % 26) + ord('a')
                    decoded += chr(new_char)
            print 'decode: ', decoded
            if decoded == "northpole object storage ":
                print matches.group(2)

    print valid_room_total


print processInput(inputFile)
