# DateBuiler class
This class gives you opportunity to use multiple operation related to date with their functions. e.g. guess future date
or past dates, getting number of years b/w two days etc

## getCustomDate
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