import sys
input = sys.stdin.readline

tc = int(input())

for i in range(tc):
    ans = int(input())
    if 1900 <= ans:
        print("Division 1")
    elif 1600 <= ans <= 1899:
        print("Division 2")
    elif 1400 <= ans <= 1599:
        print("Division 3")
    elif ans <= 1399:
        print("Division 4")
