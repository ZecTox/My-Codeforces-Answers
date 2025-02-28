import sys, math
input = sys.stdin.readline

Y, W = map(int, input().split())
mx = max(Y, W)
num = 7 - mx
den = 6
g = math.gcd(num, den)
print(f"{num//g}/{den//g}")


