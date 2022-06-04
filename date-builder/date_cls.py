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

    def getCustomDate(self, date_format, days):
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
