import sys
input = sys.stdin.readline

testcase = int(input())
for i in range(testcase):
    ans = input().strip()
    if len(ans) > 10:
        print(ans[0] + str(len(ans) -2) + ans[len(ans)-1])
    else:
        print(ans)