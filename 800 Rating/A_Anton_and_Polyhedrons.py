import sys
input = sys.stdin.readline

n = int(input())

count = 0

for i in range(n):
    str = input().strip()
    if str == "Tetrahedron":
        count += 4
    if str == "Cube":
        count += 6
    if str == "Octahedron":
        count += 8
    if str == "Dodecahedron":
        count += 12
    if str == "Icosahedron":
        count += 20
    
print(count)