a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print("equilateral")

elif a == b or b == c or c == a:
    print("isosceles")

else:
    print("neither")

