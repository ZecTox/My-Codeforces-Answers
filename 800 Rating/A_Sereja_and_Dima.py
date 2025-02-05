import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

left=0
right=n-1
sereja_score = 0
dima_score = 0

for i in range(n):
    if i%2==0:
        if arr[left]>arr[right]:
            sereja_score+=arr[left]
            left+=1
        else:
            sereja_score+=arr[right]-1
            right-=1
    else:
        if arr[left]>arr[right]:
            dima_score+=arr[left]
            left+=1
        else:
            dima_score+=arr[right]
            right-=1
            
print(sereja_score, dima_score)