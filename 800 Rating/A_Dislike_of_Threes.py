import sys
input = sys.stdin.readline

tc = int(input())

for i in range(tc):
    
    n = int(input())
    count = 0
    num = 1
    
    while count < n:
        if num % 3 != 0 and num % 10 != 3:
            count += 1
        if count < n:
            num += 1
            
    print(num)  