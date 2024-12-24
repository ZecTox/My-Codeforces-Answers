import sys
input = sys.stdin.readline

str = input().strip()
str = str.split('+')
str.sort()
print('+'.join(str))