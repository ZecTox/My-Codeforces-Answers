from re import X
import sys
input = sys.stdin.readline

a, b = map(int, input().split())

print(min(a, b), (max(a, b) - min(a, b)) // 2)