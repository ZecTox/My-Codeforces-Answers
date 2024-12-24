import sys
input = sys.stdin.readline

num = int(input())
stones = input().strip()
count = 0 

for i in range(1,num):  # can use range(1,len(stones)) instead of range(1,num) or range(0,num-1)
    if stones[i] == stones[i-1]:
        count += 1

print(count)
