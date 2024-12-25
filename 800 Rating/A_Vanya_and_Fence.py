import sys
input = sys.stdin.readline

n,h = map(int,input().split())
arr = list(map(int,input().split()))

ansofcount = 0

for i in arr:
    if i>h:
        ansofcount+=2
    else:
        ansofcount+=1
    
print(ansofcount)
