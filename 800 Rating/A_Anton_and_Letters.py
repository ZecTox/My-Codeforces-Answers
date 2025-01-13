import sys
input = sys.stdin.readline

s = input().strip()
s = s[1:-1]
if s == "":
    print(0)
else:
    s = s.split(", ")
    s = set(s)
    print(len(s))
    
# print(len(set(s[1:-1].split(", "))) if s != "{}" else 0)
    