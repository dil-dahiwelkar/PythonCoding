# 1. Prime Number
n = int(input("enter a num"))
for i in range(2,n):
    if n%i==0:
        print("not prime")
        break
else:
    print("prime")


2.# Factorial
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))


3.# Armstrong
def armstorng(n):
    sum=0
    original=n
    while n>0:
        digit=n%10
        n//=10
        if original==sum:
            print("armstrong")
        else:
            print("not armstrong")
print(armstorng(4))


4.# amicable
def amicable(n):
    return sum(i for i in range(1, n) if n % i == 0)

n1 = 220
n2 = 284

if amicable(n1) == n2 and amicable(n2) == n1:
    print("Amicable")
else:
    print("Not Amicable")


# 5. anagram race=care
# check two strings are anagram to each other

def is_anagram(str1,str2):
    if len(str1)!=len(str2):
        return False
    if sorted(str1)==sorted(str2):
        return True
s1 = input("enter first word")
s2 = input("enter second word")

if is_anagram(s1,s2):
    print("anagram")
else:
    print("not anagram")