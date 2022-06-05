from date_cls import DateBuilder



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