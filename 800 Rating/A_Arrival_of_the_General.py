import sys
input = sys.stdin.readline

def swap(i,j,list):
    list[i], list[j] = list[j], list[i]

num = int(input())
list = list(map(int, input().split()))

count = 0

max_int = 0
min_int = 0

max_el = list[0]
min_el = list[0]

for i in range(num):
    if list[i] > max_el:
        max_el = list[i]
        max_int = i
    if list[i] <= min_el:
        min_el = list[i]
        min_int = i
        
if max_int > min_int:
    count = max_int + (num - min_int - 2)
else:
    count = max_int + (num - min_int - 1)
    
print(count)