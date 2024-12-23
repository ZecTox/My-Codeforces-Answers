import sys
input = sys.stdin.readline

testcase = int(input())

count = 0

for i in range(testcase):
    a,b,c = map(int,input().split())
    if a+b+c >=2:
        count += 1

print(count)