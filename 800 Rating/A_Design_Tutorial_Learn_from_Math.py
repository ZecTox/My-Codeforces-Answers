import sys
input = sys.stdin.readline

def iscomposite(int):
    if int == 1:
        return False
    for i in range(2, int):
        if int % i == 0:
            return True
    return False

num = int(input())
for i in range(1, num+1):
    if i + (num-i) == num and iscomposite(i) and iscomposite(num-i):
        print(i, num-i)
        break   