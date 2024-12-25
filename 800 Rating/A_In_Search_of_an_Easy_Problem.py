import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# if 1 in arr:
#     print('HARD')
# else:
#     print('EASY')

print('HARD' if 1 in arr else 'EASY')