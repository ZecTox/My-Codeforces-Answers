import sys
input = sys.stdin.readline

num = int(input())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
ans_arr = set(arr1[1:] + arr2[1:]) #to bybass 0 if there in the set

if len(ans_arr) == num:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
 