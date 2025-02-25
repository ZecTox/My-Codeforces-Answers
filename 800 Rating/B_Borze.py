import sys
input = sys.stdin.readline

string = input().strip()

lst =  [i for i in string]

ans = ""

while lst != []:
    if lst[0] == ".":
        lst.pop(0)
        ans += "0"
    elif lst[0] == "-" and lst[1] == ".":
        lst.pop(0)
        lst.pop(0)
        ans += "1"
    elif lst[0] == "-" and lst[1] == "-":
        lst.pop(0)
        lst.pop(0)
        ans += "2"

print(ans)