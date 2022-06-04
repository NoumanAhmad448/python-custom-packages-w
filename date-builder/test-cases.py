from date_cls import DateBuilder

date = DateBuilder().getCustomDate("2022-12-09", 2)
print(date, end='\n')
date = DateBuilder().getCustomDate("2022-12-02", 2)
print(date, end='\n')
date = DateBuilder().getCustomDate("2022-12-02", -2)
print(date, end='\n')