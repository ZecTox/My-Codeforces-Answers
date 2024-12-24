import sys
input = sys.stdin.readline

lc_count = 0
uc_count = 0

word = input().strip()

for i in word:
    if i.islower():
        lc_count += 1
    else:
        uc_count += 1

if lc_count >= uc_count:
    print(word.lower())
else:
    print(word.upper())
