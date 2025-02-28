import sys
input = sys.stdin.readline
from collections import Counter

num = int(input())
arr = list(map(int, input().split()))

if Counter(arr)[1] == 0 or Counter(arr)[2] == 0 or Counter(arr)[3] == 0:
    print(0)
    
else:
    prog = []
    math = []
    pe = []
    
    for i in range(num):
        if arr[i] == 1:
            prog.append(i+1)
        elif arr[i] == 2:
            math.append(i+1)
        else:
            pe.append(i+1)
            
    print(min(len(prog), len(math), len(pe)))
    
    for i in range(min(len(prog), len(math), len(pe))):
        print(prog[i], math[i], pe[i])