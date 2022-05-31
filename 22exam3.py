import sys
numone = sys.argv[1]
numtwo = sys.argv[2]
num_out = []
numtwo_out = []

with open(numone, 'r') as f:
    num = int(input("Enter a number to check: "))
    for line in f:
        if str(num) in line:
            num_out.append(str(num))

with open(numtwo, 'r') as f:
    for line in f:
        if str(num) in line:
            numtwo_out.append(str(num))

last_num = len(num_out)
last_num2 = len(numtwo_out)
dict1 = {numone:last_num, numtwo: last_num2}
print("Number " + str(num) + " occurs " + str(dict1) + " times")
