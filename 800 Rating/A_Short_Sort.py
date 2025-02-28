import sys
input = sys.stdin.readline

tc = int(input())


for i in range(tc):
    arr = list(input().strip())
    count = 0
    
    if arr[0] != 'a':
        count += 1
    if arr[1] != 'b':
        count += 1
    if arr[2] != 'c':
        count += 1
    
    if count == 0 or count == 2:
        print("YES")    
    else:
        print("NO")