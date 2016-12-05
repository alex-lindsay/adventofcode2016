import hashlib
# input = "abc"
input = "ojvtpuvg"

def processInput(input):
    counter = 0
    index = 0
    result = ""
    while (index < 8):
        hash = hashlib.md5(input + str(counter)).hexdigest()
        # if counter % 10000 == 0:
        #     print counter
        if hash[0:4] == "0000":
            print (input + str(counter)), hash
            if hash[0:5] == "00000":
                result += hash[5]
                index += 1
                print "RESULT SO FAR:", result
        counter += 1

    return result

result = processInput(input)

print "Day 5 result:", result
