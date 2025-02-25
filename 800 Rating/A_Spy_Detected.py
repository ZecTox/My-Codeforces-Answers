import sys
input = sys.stdin.readline        
from collections import Counter

tc = int(input())

for i in range (tc):
    n = int(input())
    arr = list(map(int, input().split()))
    Counter(arr)
    for i in range(n):
        if Counter(arr)[arr[i]] == 1:
            print(i+1)
            break

