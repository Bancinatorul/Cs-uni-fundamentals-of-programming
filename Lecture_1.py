"""
    Problem statement:
        1. Read a string from the program's console
        2. Divide the string into numbers, words (using space)
        3. Build a list of primes, a list of negative numbers, a list of the rest of the numbers, a list
        of capitalized names

        4. Print out all primes numbers etc. in ascending order, without duplicates :)
"""
from math import sqrt
def is_prime(n: int) -> bool:
    if n == 2:
        return True
    if(n<2 or n%2==0):
        return False
    for i in range(3,int(sqrt(n))+1,2):
        if(n%i==0):
            return False
    return True

def is_capitalized(word: str) -> bool:
    return 'A' <= word <= 'Z'

line=input("Give a string=")
tokens = line.split(" ")
primes_list=[]
negatives_list=[]
other_numbers_list=[]
cap_names_list=[]
for token in tokens:
    try:
        int_token=int(token)
        if int_token<0:
            negatives_list.append(int_token)
        elif is_prime(int_token):
            primes_list.append(int_token)
        else:
            other_numbers_list.append(int_token)
    except ValueError:
        if is_capitalized(token):
            cap_names_list.append(token)
primes_list=list(set(primes_list))
negatives_list=list(set(negatives_list))
other_numbers_list=list(set(other_numbers_list))
cap_names_list=list(set(cap_names_list))
other_numbers_list.sort()
primes_list.sort()
negatives_list.sort()
cap_names_list.sort()
print(primes_list)
print(negatives_list)
print(other_numbers_list)
print(cap_names_list)

