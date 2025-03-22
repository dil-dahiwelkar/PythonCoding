
# 1.Enumerate

months = ["Jan","Feb","March","April","May","June","July","Aug","Sep","Oct","Nov","Dec"]
weekdays = ["Sunday","Monday","Tues","Thrus","Fri","Sat"]
numbers = [1,2,3,4,5,6]

for index,day in enumerate(months,10):
    print(f"{day} --> {index}")

# 2. Zip
zipped = list(zip(months,weekdays,numbers))
print(zipped)

# 3.Zip_longest
from itertools import zip_longest
zipped = list(zip_longest(months,weekdays,numbers,fillvalue="*"))
print(zipped)


