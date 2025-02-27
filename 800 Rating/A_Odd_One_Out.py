import sys
input = sys.stdin.readline
from collections import Counter

tc = int(input())

for i in range(tc):
    arr = list(map(int, input().split()))
    Counter(arr)

    for i in range(len(arr)):
        if Counter(arr)[arr[i]] == 1:
            print(arr[i])
            break