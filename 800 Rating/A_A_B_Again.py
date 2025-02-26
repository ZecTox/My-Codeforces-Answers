import sys
input = sys.stdin.readline

tc = int(input())

for i in range(tc):
    num = int(input())
    unit_digit = num % 10
    tens_digit = num // 10
    print(unit_digit + tens_digit)