import sys
input = sys.stdin.readline

iter = int(input())
arr = list(map(int, input().split()))

arr = sorted(arr)

count = 0

for i in range(iter):
    if arr[i] < arr[iter - 1]:
        count += arr[iter - 1] - arr[i]
        
print(count)