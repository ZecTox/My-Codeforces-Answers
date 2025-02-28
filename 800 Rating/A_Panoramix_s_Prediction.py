import sys
input = sys.stdin.readline
# from sympy import isprime


def isprime(n):
    if n <= 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


a ,b = map(int, input().split())

nextprime_condn = False

new_b = 0

while nextprime_condn == False:
    a += 1
    if isprime(a):
        nextprime_condn = True
        new_b = a
        break
    
if new_b == b:
    print("YES")
else:
    print("NO")