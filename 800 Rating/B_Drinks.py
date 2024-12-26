import sys
input = sys.stdin.readline

num = int(input())

arr = list(map(int, input().split()))

print(sum(arr) / num )