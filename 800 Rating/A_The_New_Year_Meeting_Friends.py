import sys
input = sys.stdin.readline

arr = map(int, input().split())
arr = sorted(arr)

sum = (arr[1] - arr[0]) + (arr[2] - arr[1])
print(sum)