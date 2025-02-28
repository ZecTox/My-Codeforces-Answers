import sys
input = sys.stdin.readline

tc = int(input())

for i in range(tc):
    arr = list(map(int, input().split()))

    arr = sorted(arr, reverse=True)
    
    if arr[0] + arr[1] >= 10:
        print("YES")
    else:
        print("NO")
