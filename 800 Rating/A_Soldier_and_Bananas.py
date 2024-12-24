import sys
input = sys.stdin.readline

k, n, w = map(int, input().split())  # k: initial price, n: money the soldier has, w: number of bananas

total = 0
for i in range(1, w+1):
    total += i*k
if total > n:
    print(total - n)
else:
    print(0)