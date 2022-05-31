import sys
fullname = sys.argv[1]
name_lst = []
with open(fullname, 'r') as infile:
    lname = input('Please enter a surname:')
    for line in infile:
        if lname in line or lname.lower() in line.lower() or lname.upper() in line.upper():
            name_lst.append(line.split(' ')[0])
if len(name_lst) > 0:
    print(name_lst)
else:
    print('No-one has that surname')
