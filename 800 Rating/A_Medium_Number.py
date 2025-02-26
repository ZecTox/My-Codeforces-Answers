import sys
input = sys.stdin.readline

tc = int(input())

for i in range(tc):
    arr = list(map(int, input().split()))
    arr = sorted(arr)
    print(arr[1])