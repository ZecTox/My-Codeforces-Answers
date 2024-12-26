import sys
input = sys.stdin.readline

num1 = input().strip()
num2 = input().strip()

for i in range(len(num1)):
    if num1[i] == num2[i]:
        print(0, end = '')
    else:
        print(1, end = '')
print()