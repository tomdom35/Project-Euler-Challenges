def is_leap_year(year):
    if year % 100 == 0:
        return year % 400 == 0
    return year % 4 == 0

def get_day(year,month,day):
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    month_names = ["January","February","March","April","May","June","July","August","September","October","Novermber","December"]
    week_days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    
    if(is_leap_year(year)):
        if(month == 2 and day > 29):
            return "February cannot have more than 29 days."
        if(month == 2 and day == 29):
            days = -1
        else:
            valid_date = check_date(year,month,day)
            if(valid_date != "Valid Date"):
                return valid_date
            if(month <= 2 and day <= 28):
                days = -1
            else:
                days = 0
    else:
        valid_date = check_date(year,month,day)
        if(valid_date != "Valid Date"):
            return valid_date
        days = 0
    
    leap_years = 0
    years = year - 1900
    for i in range(years+1):
        cur_year = 1900+i
        if (is_leap_year(cur_year)):
            leap_years += 1
            
    days = days + 365*years + leap_years

    for i in range(month):
        if(i == month-1):
            days += day
        else:
            days+=months[i]

    days = days%7

    return (str(month_names[month-1]) + " " + str(day) + ", " + str(year) + ": " + week_days[days])

def check_date(year,month,day):
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    month_names = ["January","February","March","April","May","June","July","August","September","October","Novermber","December"]
    if(year<1900):
        return "Year must be 1900 or later."
    if(month < 1 or month > 12):
        return "Month must be 1 - 12."
    if(day < 1):
        return "Day must be greater than 0."
    if(months[month-1]<day):
        return (str(month_names[month-1]) + " must have " + str(months[month-1]) + " days or less.")
    return "Valid Date"

print(get_day(3490,12,31))
    

    
    
        
