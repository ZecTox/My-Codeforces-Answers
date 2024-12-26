import sys
input = sys.stdin.readline

num = int(input())

for i in range(num):
    if i % 2 == 0:
        print("I hate", end=" ")
    else:
        print("I love", end=" ")
    if i != num - 1:
        print("that", end=" ")
print("it")