import sys
input = sys.stdin.readline

max_person = 0
tracker = 0

tc = int(input())

for _ in range(tc):
    a, b = map(int, input().split())
    tracker += b - a
    max_person = max(max_person, tracker)
    
print(max_person)