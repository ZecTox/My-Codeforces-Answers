import sys
input = sys.stdin.readline

n, k, l, c, d, p, nl, np = map(int, input().split())

print(min(k*l//nl, c*d, p//np)//n)