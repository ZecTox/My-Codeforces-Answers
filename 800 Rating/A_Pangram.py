import sys
input = sys.stdin.readline

num = int(input())
str = input().strip().lower()
str1 = set(str)

if len(str1) >= 26:
    print("YES")
else:
    print("NO")