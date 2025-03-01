import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    x, y, n = map(int, input().split())
    
    if (n//x)*x + y <= n:
        print((n//x)*x + y)
    else:
        print((n//x-1)*x + y)