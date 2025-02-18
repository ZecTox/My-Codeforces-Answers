import sys
input = sys.stdin.readline

tc = int(input().strip())

for _ in range(tc):
    ans = input().strip()
    ans_list = list(ans)
    if len(ans_list) >= 2:
        ans_list.pop()  
        ans_list.pop()  
    modified_ans = ''.join(ans_list) + 'i'
    print(modified_ans)
