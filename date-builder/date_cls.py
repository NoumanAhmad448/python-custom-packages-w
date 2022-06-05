from datetime import date, timedelta


class DateBuilder:
    """** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
    *
    * @ description
    * getCustomDate gives you next or previous date depending upon the
    * number of days your want

    * @examples
    * getCustomDate("year-month-date",2) returns date that comes after
    * two days in the format "year-month-date"
    *
    * getCustomDate("year-month-date",-2) returns date that comes before
    * two days in the format "year-month-date"
    *
    * @return string
    * @author Nouman Ahmad
    *
    ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * """

    @staticmethod
    def getCustomDate(date_format, days):
        if not isinstance(date_format, str):
            raise Exception('date format must be in string format')

        if not isinstance(days, int):
            raise Exception('days must be in integer format')

        try:
            given_date = date.fromisoformat(date_format)
            new_date = timedelta(days=days)
            return given_date + new_date

        except ValueError:
            raise Exception("date format must be in yyyy-mm-dd format")

    """      
     * @description 
     * getCustomMonthDate gives you next or previous date depending 
     * upon the number of months you provide 
     * 
     * @examples
     * getCustomMonthDate("year-month-date",2) returns date that comes after
     * two month in the format "year-month-date"
     * 
     * getCustomMonthDate("year-month-date",-2) returns date that comes before
     * two month in the format "year-month-date"
     * 
     * @return string
     * 
    """

    @staticmethod
    def getCustomMonthDate(date_format, months):
        if not isinstance(date_format, str):
            raise Exception('date format must be in string format')

        if not isinstance(months, int):
            raise Exception('months must be in integer format')
        try:
            given_date = date.fromisoformat(date_format)
            day = given_date.day
            month = given_date.month
            year = given_date.year

            next_expected_month = month + months
            if next_expected_month > 12:
                next_year_to_add = int(next_expected_month / 12)
                next_month_to_add = 12 if next_expected_month % 12 == 0 else next_expected_month % 12
                year += next_year_to_add
                month = next_month_to_add
            else:
                month += months

            # check either month or date include 0 if there is a value in b/w 1-9
            month = str(month)
            year = str(year)
            first_day = "01"
            if len(month) == 1:
                month = "0" + month

            # getting first day of next date
            new_date = date.fromisoformat(year+"-"+month+"-"+first_day)

            # finalizing that calculated day should not exceed from the actual last day of the new upcoming date
            if new_date.month == 12:
                new_date = new_date.replace(day=31)
            else:
                new_date = new_date.replace(month=new_date.month + 1, day=1) - timedelta(days=1)
            last_day = new_date.day

            if day > last_day:
                day = last_day
            day = str(day)
            if len(day) == 1:
                day = "0" + day
            return date.fromisoformat(year+"-"+month+"-"+day)

        except ValueError:
            raise Exception("date must be in the yy-mm-dd format")
