import sys
input = sys.stdin.readline

hehe = int(input())
 
if hehe%2 == 0 and hehe >2:
    sys.stdout.write("YES" + "\n")
else:
    sys.stdout.write("NO" +  "\n")