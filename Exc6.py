
# star
n=5
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()


# n = 5
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()


# n=5
for i in range(0,n):
    for j in range(n):
        print(end=" ")
    n = n-1
    for k in range(i+1):
        print("*",end=" ")
    print()


# n=5
for i in range(n,0,-1):
    for j in range(n-i):
        print(end=" ")
    for k in range(i):
        print("*",end=" ")
    print()


