
1. # fibonacci series
n = int(input("enter a num"))
first,second=0,1
print(first," ",second,end=" ")
for i in range(2,n):
    third=first+second
    print(third,end=" ")
    first=second
    second=third


2. # recursion
# Recursion - Recursion is a function that calls itself.
def rev_str(st):
    if len(st)==0:
        return st
    else:
        return rev_str(st[1:])+st[0]
print(rev_str("madam"))


# 3.  break
for i in range(1,10):
    print(i)
    if i==2:
        break;


# 4. continue
for i in range(10):
    if i==5:
        continue
    print(i)


# 5. Multiplication table
n = int(input("enter a num"))
for i in range(1,11):
    print(f"{n}*{i}={n*i}")