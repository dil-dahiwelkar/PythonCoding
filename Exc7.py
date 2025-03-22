# 1 Sum
n = int(input("enter a num"))
sum = 0
while n>0:
    sum = sum+n%10
    n = n//10
print(sum)


# 2 Square
n = int(input("enter num"))
sum = 0
while n>0:
    sum = sum+(n%10)*(n%10)
    n = n//10
print(sum)


# 3. Cube
n = int(input("enter a num"))
sum = 0
while n>0:
    sum = sum+(n%10)*(n%10)*(n%10)
    n = n//10
print(sum)


# 4. Prdouct of digits
n = int(input("enter a num"))
prod = 1
while n>10:
    prod = prod*(n%10)
    n =n//10
print(prod)


# 5. Reverse
n = int(input("enter a num"))
rev=0
while n>0:
    rev = (rev*10)+n%10
    n = n//10
print(rev)
