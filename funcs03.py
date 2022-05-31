#!/usr/bin/env python3


def get_price(age):
    if age <= 16:
        return 5
    elif age >= 60:
        return 7
    else:
        return 10

def weird_case(some_str):
    ret = ""
    char_check = True
    for char in some_str:
        if char_check:
            ret += char.upper()
        else:
            ret += char.lower()
        if char != " ":
            char_check = not char_check
    return ret.strip()

def every_second(l1, l2):
    l3 = []
    for num in l1[1::2]:
        l3.append(num)
    for num in l2[1::2]:
        l3.append(num)
    return l3


def is_neg(num):
    return num < 0


def remove_neg(lst):
    indexlst = []
    for i in lst:
        if i < 0:
            indexlst.append(i)
    for i in indexlst:
        if i in lst:
            lst.remove(i)
    return lst


def countdown(num):
    i = num
    while i > 0:
        print(i)
        i -= 1
    return print("LIFT OFF!")


def search(str, letter):
    return letter in str


def index(str, letter):
    if letter in str:
        return str.index(letter)
    else:
        return -1


def previous_two(n):
    inp = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    return inp[n]


if __name__ == "__main__":
    print(get_price(4))
    print(weird_case("I love Python"))
    print(every_second([3, 4, 5, 6], [12, 2, 5]))
    print(is_neg(-3))
    print(remove_neg([-50, -1, 9]))
    print(countdown(3))
    print(search("python", "a"))
    print(search("python", "h"))
    print(index("python", "a"))
    print(index("python", "h"))
    print(previous_two(3))
    print(previous_two(6))
    print(previous_two(1))
