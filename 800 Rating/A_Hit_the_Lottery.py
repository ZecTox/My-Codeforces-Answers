import sys
input = sys.stdin.readline

n = int(input())

no_of_notes = 0

while n > 0:
    if n >= 100:
        no_of_notes += n // 100
        n = n % 100
    elif n >= 20:
        no_of_notes += n // 20
        n = n % 20
    elif n >= 10:
        no_of_notes += n // 10
        n = n % 10
    elif n >= 5:
        no_of_notes += n // 5
        n = n % 5
    else:
        no_of_notes += n
        n = 0
        
print(no_of_notes)