import sys
input = sys.stdin.readline

num = int(input())
count = 1
arr = []

for i in range(num):
    arr.append(int(input()))

for i in range(num-1):
    if arr[i] != arr[i+1]:
        count += 1

print(count)