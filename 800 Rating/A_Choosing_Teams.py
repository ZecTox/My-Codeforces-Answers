import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

count = 0

for i in range(n):
    if 5 - arr[i] >= k:
        count += 1
        
print(count//3)