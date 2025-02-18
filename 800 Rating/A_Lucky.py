import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    newnum = int(input())
    num1 = 0
    num2= 0
    
    for i in range(3):
        num1 += newnum % 10
        newnum = newnum // 10
    for i in range(3):
        num2 += newnum % 10
        newnum = newnum // 10   
        
    if num1 == num2:
        print('YES')
    else:
        print('NO')