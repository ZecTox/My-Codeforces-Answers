import sys
input = sys.stdin.readline


tc = int(input())

for i in range(tc):
    strr = input().strip()
    if strr == "c" or strr =="o" or strr == "d" or strr == "e" or strr == "f" or strr == "o" or strr == "r" or strr == "c" or strr == "e" or strr == "s":
        print("YES")
    else:
        print("NO")