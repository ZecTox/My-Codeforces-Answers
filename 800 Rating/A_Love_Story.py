import sys
input = sys.stdin.readline

tc = int(input())

main_str = "codeforces"

for i in range(tc):
    
    count = 0
    str1 = input().strip()
    
    for i in range(len(main_str)):
        if main_str[i] != str1[i]:
            count += 1
    
    print(count)
