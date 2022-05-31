list1 = []
list2 = []

def counting():
    for s in list2:
        c = list1.count(s)
        print(f'{s} occurred {c} times')

running = True

while running:
    n = int(input('Please enter a number (-1 to stop):'))
    if n != -1:
        list1.append(n)
        for n in list1:
            if n not in list2:
                list2.append(n)
    else:
        print(list2)
        counting()
        running = False
