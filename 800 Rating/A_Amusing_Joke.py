import sys
input = sys.stdin.readline

a = str(input().strip())
b = str(input().strip())
c = str(input().strip())

d = str(a + b)

if sorted(d) == sorted(c):
    print("YES")
else:
    print("NO")