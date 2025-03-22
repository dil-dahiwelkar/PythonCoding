
# 1. Filter
data = ["abcd","1234","12ab","abc9080"]
filtered=[]
for item in data:
    if item.isalpha():
        filtered.append(item)
print(filtered)


# 2. Map
import operator
numbers = [1,2,3,4,5,6]
result = list(map(operator.add,numbers,numbers))
print(result)


# 3. Reduce
from functools import reduce
numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, numbers)
print(result)


# 4. Accumulate
import operator
from itertools import accumulate
data = [1,2,3,4,5,6]
result = list(accumulate(data,operator.add))
print(result)