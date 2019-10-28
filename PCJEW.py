import os
import sys

from datetime import date
from datetime import datetime, timedelta
from nsepy import get_history
from nsepy.derivatives import get_expiry_date


#print(sys.argv[1])

today = datetime.today()
start_7 = date.today()#- timedelta(days=7)
start_14 = date.today() - timedelta(days=14)

#getData of last to last 7 days

_sum = 0
count = 0 

data_spot_14_days_back = get_history(symbol=str(sys.argv[1]),start=start_14,end=start_7)
data_spot_14_days_back.rename({"%Deliverble":"Percent_Deliverble"}, inplace = True)
#print(type(data_spot_14_days_back))

dataSpotLength_14 = data_spot_14_days_back.shape
dataSpotLength14 = dataSpotLength_14[0]

#print(dataSpotLength_14[0])
print(data_spot_14_days_back)

#======================================================== Volumes ==================================================================
for count in range(0,5):
    _sum = _sum + data_spot_14_days_back.Volume[count]
    print(data_spot_14_days_back.Volume[count])
    count = count +1
    print(count)

lastWeekAvgVolume =  _sum/count

count_this_week = 0
sum_this_week = 0

for count in range(5,int(dataSpotLength14)):
    sum_this_week  = sum_this_week + data_spot_14_days_back.Volume[count]
    print(data_spot_14_days_back.Volume[count])
    count_this_week = count_this_week  +1

print("Coun this week=", count_this_week)
thisWeekAvgVolume = sum_this_week/count_this_week
print(thisWeekAvgVolume)

#========================================================= Deliverables==============================================================

print(data_spot_14_days_back.Percent_Deliverble[count])
for count in range(0,5):
    _sum = _sum + data_spot_14_days_back.Percent_Deliverble[count]
    print(data_spot_14_days_back.Deliverble[count])
    count = count +1

lastWeekAvgDeliverble =  _sum/count

count_this_week = 0
sum_this_week = 0

for count in range(5,int(dataSpotLength14)):
    sum_this_week  = sum_this_week + data_spot_14_days_back.Deliverble[count]
    print(data_spot_14_days_back.Deliverble[count])
    count_this_week = count_this_week  +1

print("Coun this week=", count_this_week)
thisWeekAvgDeliverble = sum_this_week/count_this_week
print(thisWeekAvgDeliverble)

data_spot_7_days_back = get_history(symbol=str(sys.argv[1]),start=start_7,end=date(today.year,today.month,today.day))

dataSpotLength = data_spot_7_days_back.size/15

dataSpotRecords = int(dataSpotLength) -1 



data_futures= get_history(symbol=str(sys.argv[1]),start=date(today.year,10,10),end=date(today.year,today.month,today.day),futures=True,expiry_date=get_expiry_date(year = today.year,month = today.month))

Length = data_futures.size
print(Length)
print(data_futures.columns)

numRecords = Length/13 #number of fields in column = 13
NumOfRecords = int(numRecords) -1

print(NumOfRecords)
if data_futures.Open[NumOfRecords] > data_futures.Close[NumOfRecords -1] and data_futures.Open[NumOfRecords] > data_futures.High[NumOfRecords -1]:
    print(data_futures.Symbol, " closed above yesterdays close and also breached yesterdays high")
else:
    print(data_futures.Symbol, " closed above yesterdays high")
    
#f data.Open() > data



print(data_futures)


