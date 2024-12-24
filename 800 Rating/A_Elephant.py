import sys
input = sys.stdin.readline

dist = int(input())
if dist % 5 == 0:
    print(dist // 5)
else:
    print(dist // 5 + 1)
    
# The step elephant takes is in multiple of 5 and plus whatever the remainder is, so we can directly add 1 to the quotient of the division of the distance by 5.