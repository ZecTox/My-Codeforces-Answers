import sys
input = sys.stdin.readline

tc = int(input())

ans = 0

for i in range(tc):
    _str = str(input().strip())
    if _str == "X++" or _str == "++X":
        ans += 1
    elif _str == "X--" or _str == "--X":
        ans -= 1

print(ans)