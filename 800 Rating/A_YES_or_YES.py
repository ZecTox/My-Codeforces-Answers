import sys
input = sys.stdin.readline

tc = int(input())

for i in range(tc):
    s  = input().strip()
    if s.upper() == "YES":
        print("YES")
    else:
        print("NO")