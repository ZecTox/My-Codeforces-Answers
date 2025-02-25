import sys
input = sys.stdin.readline

tc = int(input())

for i in range(tc):
    arr_num = int(input())
    arr = list(map(int, input().split()))
    
    arr = sorted(arr)
    
    a = 0
    b = 1
    
    
    for i in range(arr_num - 1):
        if arr[a] == arr[b] or arr[a] + 1 == arr[b]:
            arr.pop(a)
            
    if len(arr) == 1:
        print("YES")
    else:
        print("NO")
