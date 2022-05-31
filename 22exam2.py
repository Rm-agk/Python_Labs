import sys
numbers = sys.argv[1]
num_out = []

with open("numbers.txt", 'r') as f:
    num = int(input("Enter a number to check: "))
    for line in f:
        if str(num) in line:
            num_out.append(str(num))

last_num = len(num_out)
print("Number " + str(num) + " occurs " + str(last_num) + " times in file numbers.txt")
