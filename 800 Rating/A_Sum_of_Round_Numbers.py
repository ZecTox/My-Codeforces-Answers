import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    num = str(input().strip())
    length = len(num)
    count = 0
    for j in range(length):
        if num[j] != '0':
            count += 1
    print(count) 
    for j in range(length):
        if num[j] != '0':
            print(num[j] + '0' * (length - j - 1), end=' ')
    print()
