import sys
input = sys.stdin.readline

tc = int(input())

for i in range(tc):
    str1, str2 = map(str, input().split())
    print(str2[0] + str1[1:], str1[0] + str2[1:])