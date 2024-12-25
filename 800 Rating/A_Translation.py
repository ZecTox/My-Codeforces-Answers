import sys
input = sys.stdin.readline

s = input().strip()
t = input().strip()

'''Method 1'''
# if list(reversed(s)) == list(t):
#     print("YES")
# else:
#     print("NO")

'''Method 2'''
# s_reversed = ''.join(reversed(s))

# if s_reversed == t:
#     print("YES")
# else:
#     print("NO")

'''Method 3'''
if s[::-1] == t:
    print("YES")
else:
    print("NO")
