import sys
input = sys.stdin.readline

ans = list(map(int, input().split()))
ans = set(ans)  #better one
# ans list(set(ans)) ''' commented this out because it increased the rumtime'''

print(abs(4 - len(ans)))