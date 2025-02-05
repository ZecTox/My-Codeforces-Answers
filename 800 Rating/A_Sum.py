import sys
input = sys.stdin.readline

n = int(input().strip())

for i in range(n):
    ans = list(int, input().split())
    ans = sorted(ans)

    if ans[0] + ans[1] == ans[2]:
        print("YES")
    else:
        print("NO")
    