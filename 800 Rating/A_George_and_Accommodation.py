import sys
input = sys.stdin.readline

num = int(input())
room_count = 0

for i in range(num):
    pi, qi = map(int, input().split())
    if qi - pi >= 2:
        room_count += 1

print(room_count)