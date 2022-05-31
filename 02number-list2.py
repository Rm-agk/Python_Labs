
a = int(input('Please enter a number (-1 to stop):'))
l = []

while a != -1:
    if a not in l:
        l.append(a)
        a = int(input('Please enter a number (-1 to stop):'))
    else:
        a = int(input('Please enter a number (-1 to stop):'))

print(l)

