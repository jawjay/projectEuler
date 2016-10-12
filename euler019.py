class day:
    def __init__(self,year,day,month):
        self.year = year
        self.day = day
        self.month = month
        self.month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    
    def isLeapYear(month):
        if month%4==0:
            if month%100==0:
                if month%400==0:
                    return True
                return False
            return True
        return False

    def daysBetween(self,other):
        diffYear = other.year-self.year
        diffMonth = other.month-self.month
        diffDay = other.day-self.day

        

