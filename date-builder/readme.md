# DateBuiler class
This class gives you opportunity to use multiple operation related to date with their functions. e.g. guess future date
or past dates, getting number of years b/w two days etc

## getCustomDate
##### static method
 @ description <br/>
 getCustomDate gives you next or previous date depending upon the
 number of days your want

@param <br/>
getCustomDate(date_format: str, days: int): str 

@examples <br/> 
 1. getCustomDate("year-month-date",2) returns date that comes after two days in the format "year-month-date"
 2. getCustomDate("year-month-date",-2) returns date that comes before two days in the format "year-month-date"

@return string <br/>
@author Nouman Ahmad

*******************************
## getCustomMonthDate
##### static method
 @description <br/>
 getCustomMonthDate gives you next or previous date depending 
 upon the number of months you provide 

@examples <br/>
- getCustomMonthDate("year-month-date",2) returns date that comes after
two month in the format "year-month-date"

- getCustomMonthDate("year-month-date",-2) returns date that comes before
two month in the format "year-month-date"

@return string <br/>

## getDay
##### static method
 @description
 getDay uses to get the day name in english format

 @examples
 - getDay ("2020-06-06") => Monday
 - getDay ("2020-06-07") => Tuesday

 @return String
