import sys
input = sys.stdin.readline

tc = int(input())

for i in range(tc):
    num = int(input())

    if num % 4 != 0:
        print("NO")
    else:
        arr_firsthalf = []
        arr_secondhalf = []

        for i in range(1, num//2 + 1):
            arr_firsthalf.append(2 * i)

        for i in range(1, num//2):
            arr_secondhalf.append(2 * i - 1)

        arr_secondhalf.append(sum(arr_firsthalf) - sum(arr_secondhalf))

        print("YES")
        print(*arr_firsthalf, *arr_secondhalf)
