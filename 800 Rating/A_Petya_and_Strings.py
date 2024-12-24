from operator import le
import sys
input = sys.stdin.readline

str1 = str(input()).lower()
str2 = str(input()).lower()


''' This is the first solution that I came up with. It is not the best solution but it works. '''
# if str1 == str2:
#     print(0)
# else:
#     if str1 > str2:
#         print(1)
#     if str1 < str2:
#         print(- 1)


''' This is the second solution that I came up with. It is a better solution than the first one.
    This solution is better because it uses the ASCII values of the characters to compare the strings. '''
    
for i in range(len(str1)):
    ascii1 = ord(str1[i])
    ascii2 = ord(str2[i])
    if ascii1 < ascii2:
        print(-1)
        break
    elif ascii1 > ascii2:
        print(1)
        break
    else:
        if i == len(str1) - 1:
            print(0)
            break
        else:
            continue