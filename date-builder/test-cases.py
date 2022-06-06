from date_cls import DateBuilder


date = DateBuilder.weekEndDate("2022-6-6")
print(date)



print(type(DateBuilder.weekStartDate("2022-06-08")))

print("********************new testing")
date = DateBuilder.getDay("2022-06-06")
print(date)

date = DateBuilder.getDay("2022-06-07")
print(date)
date = DateBuilder.getDay("2022-06-08")
print(date)
date = DateBuilder.getDay("2022-06-09")
print(date)
date = DateBuilder.getDay("2022-06-10")
print(date)
date = DateBuilder.getDay("2022-06-11")
print(date)
date = DateBuilder.getDay("2022-06-12")
print(date)









print("**********old*************testing")
date = DateBuilder.getCustomMonthDate("2022-12-09", 2)
print(date, end='\n')

date = DateBuilder.getCustomMonthDate("2022-12-31", 2)
print(date, end='\n')

date = DateBuilder.getCustomMonthDate("2022-12-31", 12)
print(date, end='\n')

print("****************************************************")


date = DateBuilder.getCustomDate("2022-12-09", 2)
print(date, end='\n')
date = DateBuilder.getCustomDate("2022-12-02", 2)
print(date, end='\n')
date = DateBuilder.getCustomDate("2022-12-02", -2)
print(date, end='\n')