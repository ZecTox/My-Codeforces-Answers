import sys
input = sys.stdin.readline

num = int(input().strip())

lucky = 0
while num > 0:
    if num % 10 == 4 or num % 10 == 7:
        lucky += 1
    num //= 10
if lucky == 4 or lucky == 7:
    print('YES')
else:
    print('NO')