import hashlib
# input = "abc"
input = "ojvtpuvg"

def processInput(input):
    counter = 0
    index = 0
    result = "*" * 8
    while (index < 8):
        hash = hashlib.md5(input + str(counter)).hexdigest()
        # if counter % 10000 == 0:
        #     print counter
        if hash[0:4] == "0000":
            print (input + str(counter)), hash
            if hash[0:5] == "00000":
                # result += hash[5]
                position = int(hash[5], base=16)
                if (position < 8) and (result[position] == "*"):
                    result = result[:position] + hash[6] + result[position+1:]
                    index += 1
                    print "RESULT SO FAR:", result
        counter += 1

    return result

result = processInput(input)

print "Day 5 result:", result
