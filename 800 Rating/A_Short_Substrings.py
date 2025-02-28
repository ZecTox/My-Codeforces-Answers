import sys
input = sys.stdin.readline

tc = int(input())

for i in range(tc):
    s = input().strip()
    print(s[0] + s[1::2])
        