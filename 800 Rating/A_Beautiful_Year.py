import sys
input = sys.stdin.readline

given_year = input().strip()
given_year = str(int(given_year) + 1) # incrementing the year by 1

while len(set(given_year)) != 4: # checking if the year has all distinct digits
    given_year = str(int(given_year) + 1) 
    
print(given_year)