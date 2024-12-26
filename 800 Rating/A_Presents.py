import sys
input = sys.stdin.readline

num = int(input())

arr = list(map(int, input().split()))

for i in range(num):
    print(arr.index(i + 1) + 1, end = ' ')