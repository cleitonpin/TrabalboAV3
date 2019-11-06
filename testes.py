from datetime import datetime

str_date = input ('DIgite data: ')
str_date2 = input ('Digite data 2: ')
date = datetime(str_date, '%d/%m/%Y')
date2 = datetime(str_date, '%d/%m/%Y')
print(date)
print (date2)

if date <= date2:
  print ('True')