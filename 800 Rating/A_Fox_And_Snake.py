import sys
input = sys.stdin.readline

row, column = map(int, input().split())

for i in range(row):
    if i % 2 == 0:
        print('#' * column)
    else:
        if i % 4 == 1:
            print('.' * (column - 1) + '#')
        else:
            print('#' + '.' * (column - 1))