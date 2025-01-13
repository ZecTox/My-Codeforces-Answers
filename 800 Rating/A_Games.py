import sys
input = sys.stdin.readline

n = int(input())

h = []
a = []

count = 0

for i in range(n):
    h_i, a_i = map(int, input().split())
    h.append(h_i)
    a.append(a_i)
    
for i in range(len(h)):
    for j in range(len(h)):
        if h[i] == a[j]:
            count += 1
            
print(count)