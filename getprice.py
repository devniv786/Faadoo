import os

from datetime import date
from datetime import datetime
from nsepy import get_history
from nsepy.derivatives import get_expiry_date

today = datetime.today()
data = []
file = open('scripts.txt', 'r') 
for line in file: 
    #int (line)
    data.append(get_history(symbol=line,start=date(today.year,today.month,today.day),end=date(today.year,today.month,today.day),
    futures=True,expiry_date=get_expiry_date(year = today.year,month = today.month+1)))

print(len(data))
print(data.pop(0),data.pop(1))

for line in file:
    print(line in  data)
