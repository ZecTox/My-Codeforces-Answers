import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

untreated = 0
police_hired = 0

for i in range(n):
    if arr[i] == -1 and police_hired == 0:
        untreated += 1
    if arr[i] == -1 and police_hired > 0:
        police_hired -= 1
    if arr[i] > 0:
        police_hired += arr[i]
        
print(untreated)