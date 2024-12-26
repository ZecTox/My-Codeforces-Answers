import sys
input = sys.stdin.readline

num = int(input())

''' Method 1 '''
# if num % 2 == 0:
#     print(num // 2)
# else:
#     print(-(num // 2 + 1))

''' Method 2 '''    
print(num // 2 if num % 2 == 0 else -(num // 2 + 1))