import sys
input = sys.stdin.readline

tc = int(input())

for i in range(tc):
    a, b = map(int, input().split())
    if a % b == 0:
        print(0)
    else:
        print(b - a % b)