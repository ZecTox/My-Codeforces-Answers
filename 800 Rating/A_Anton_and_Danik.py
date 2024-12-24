import sys
input = sys.stdin.readline

n = int(input())
str = str(input().strip())

A_count, D_count = 0, 0

for i in str:
    if i == 'A':
        A_count += 1
    if i == 'D':
        D_count += 1
        
if A_count > D_count:
    print("Anton")
elif A_count < D_count:
    print("Danik")
else:
    print("Friendship")