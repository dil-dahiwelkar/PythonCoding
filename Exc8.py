#1. convert list of characters into string
s = ['a','b','c','d']
str = " ".join(s)
print(str)


#2 Split
d = "dilasha padmakar dahiwelkar"
names_split = d.split()
print(names_split)


#3 extend a list without append
a = [10,20,30]
b = [40,50,60]
a.extend(b)
print(a)


#4 Lambda
rev_upper = lambda inp:inp.upper()[::-1]
print(rev_upper)
result = rev_upper("bit")
print(result)
#
add = lambda a,b:(a+b)
print(add(10,20))


# 5
sorted_data = {"apple":100,"banana":40,"papaya":50,"grapes":80}
print(sorted_data)
data={key:value for key, value in sorted_data.items()}
print(data)
#
def sample(k):
    return k[1]
#
sorted_data = sorted(data.items(),key=sample)
print(sorted_data)

data = {key:value for key,value in sorted_data}
print(data)


#6 select the odd items of a list
l = [1,2,43,4,56,5,90,8]
odd_numbers = [x for x in l if x % 2 != 0]
print(odd_numbers)

