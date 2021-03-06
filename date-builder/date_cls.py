from datetime import date, timedelta


class DateBuilder:
    days = {6: 'Sunday', 0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday",
            5: "Saturday"}
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
    * @return date
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
            date_format = DateBuilder.makeDateFormatValid(date_format)
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
     * @return date
     * 
    """

    @staticmethod
    def getCustomMonthDate(date_format, months):
        if not isinstance(date_format, str):
            raise Exception('date format must be in string format')

        if not isinstance(months, int):
            raise Exception('months must be in integer format')
        try:
            date_format = DateBuilder.makeDateFormatValid(date_format)
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


    """
    /****************************************************************
     *
     * @description
     * getDay  uses to get the day name in english format
     *
     * @examples
     * getDay ("year-month-day")
     * 
     *
     * @return date
     ***************************************************************/
    """
    @staticmethod
    def getDay(given_date_format):
        try:
            date_format = DateBuilder.makeDateFormatValid(given_date_format)
            given_date = date.fromisoformat(given_date_format)
            return DateBuilder.days.get(given_date.weekday())
        except ValueError:
            raise Exception("date format is not correct")

    """** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
    @description
    weekStartDate gives you week start date w.r.t. provided date
    
    @note 
    week starts from monday

    @examples
    weekStartDate("2020-06-08") => "2020-06-06"
 
    @return date
    ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * """

    @staticmethod
    def weekStartDate(date_format):
        try:
            date_format = DateBuilder.makeDateFormatValid(date_format)
            w_day = date.fromisoformat(date_format).weekday()

            y_m_d = date_format.split("-")
            current_day = int(y_m_d[2])
            actual_day = str(current_day - w_day)

            if len(actual_day):
                actual_day = "0" + actual_day
            y_m_d[2] = actual_day

            return date.fromisoformat(date_format) if w_day == 0 else date.fromisoformat("-".join(y_m_d))
        except ValueError:
            raise Exception("date must be in format y-m-d")

    @staticmethod
    def makeDateFormatValid(date_format):
        try:
            year, month, day = date_format.split("-")
            if len(month) == 1:
                month = "0" + month
            if len(day) == 1:
                day = "0" + day
            return year + "-" + month + "-" + day
        except ValueError:
            raise Exception

    """
    @description
    weekEndDate will give you week day date w.r.t. given date
    e.g. given date 2020-6-6 will return 2020-6-12
    
    @example 
    weekEndDate("2020-6-6") => "2020-6-12"
    
    @return date 
    """

    @staticmethod
    def weekEndDate(date_format):
        date_format = DateBuilder.makeDateFormatValid(date_format)
        w_day = date.fromisoformat(date_format).weekday()
        if w_day == 6:
            return date.fromisoformat(date_format)
        w_day = 6 - w_day
        return date.fromisoformat(date_format) + timedelta(days=w_day)