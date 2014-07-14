from calendar import Calendar


class month_function(object):
    """
    Expects year and month to be integers
    """
    def __init__(self, year, month):

        self.day_table = {6: 'sun', 0: 'mon', 1: 'tue', 2: 'wed',
                          3: 'thur', 4: 'fri', 5: 'sat'}
        self.year = year
        self.month = month
        c = Calendar()
        # returns nested list of weeks / days of given month in given year
        self.month1 = Calendar.monthdayscalendar(c, year, month)

    def day(self, day):
        """
        Day should be an int, returns abbreviation for the day
        """

        for i in range(len(self.month1)):
            if day in self.month1[i]:
                print self.day_table[self.month1[i].index(day)]
