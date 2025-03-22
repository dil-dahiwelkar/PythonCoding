
# 1. pallindrome
def palindrome(n):
    if n == n[::-1]:
        return "Palindrome"
    else:
        return "Not palindrome"

print(palindrome("madam"))


# 2. Even & Odd
def even_or_odd():
    n = int(input("Enter a number"))
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(even_or_odd())


# 3.String Reverse
def rev_str(str1):
    return str1[::-1]
print(rev_str("cool"))


# 4. sort data - Modifies the original list (does not return a new list).
numbers = [8, 3, 1, 6, 2]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)         # Sorting in descending order
print(numbers)


# 5. Sorted -  (Returns a New List)
numbers = [8, 3, 1, 6, 2]
sorted_numbers = sorted(numbers)
print(sorted_numbers)




