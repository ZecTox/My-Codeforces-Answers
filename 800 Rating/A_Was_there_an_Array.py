import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    
    if len(set(b)) == 1:
        print("YES")
        continue
    
    possible = True
    for i in range(1, len(b)-1):
        if b[i-1] == 1 and b[i] == 0 and b[i+1] == 1:
            possible = False
            break
    
    if possible:
        print("YES")
    else:
        print("NO")