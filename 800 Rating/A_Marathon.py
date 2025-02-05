import sys
input = sys.stdin.readline

tc = int(input())

for i in range(tc):
    ans = list(map(int, input().split()))
    
    count = 0
    for i in range(1, len(ans)):
        if ans[i] > ans[0]:
            count += 1 
    print(count)