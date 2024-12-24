import sys
input = sys.stdin.readline

str = input().strip()
#used set as it removes duplicates
if len(set(str)) % 2 == 0: 
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")