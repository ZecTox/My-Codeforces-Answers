import sys
input = sys.stdin.readline

a, b, c, d = map(int, input().split())

num = input().strip()

dict = {'1': a, '2': b, '3': c, '4': d}

ans = sum(dict[i] for i in num)
print(ans)