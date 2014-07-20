from calendar import Calendar


class make_month(object):
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
                return self.day_table[self.month1[i].index(day)]

if __name__ == '__main__':
    import datetime

    day_table = {6: 'sun', 0: 'mon', 1: 'tue', 2: 'wed',
                 3: 'thur', 4: 'fri', 5: 'sat'}

    test_years = [1000, 1100, 1215, 1310, 1492, 1500,
                  1646, 1776, 1865, 1969, 215, 1, 19]

    correct = 0
    for i in test_years:
        date1 = datetime.date(i, 1, 1)
        date2 = make_month(i, 1)
        if day_table[date1.weekday()] == date2.day(1):
            correct += 1

    if correct == len(test_years):
        print 'tests pass'
