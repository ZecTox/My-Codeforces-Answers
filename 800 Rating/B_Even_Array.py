import sys
input = sys.stdin.readline

tc = int(input())
for i in range(tc):
    n = int(input())
    a = list(map(int, input().split()))
    
    meo = 0
    moe = 0
    
    for i in range(n):
        if i % 2 == 0:
            if a[i] % 2 != 0:
                moe += 1
        else:
            if a[i] % 2 == 0:
                meo += 1
    
    if moe != meo:
        print(-1)
    else:
        print(moe)
