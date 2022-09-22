"""Season validation"""
from datetime import date, datetime

def get_season(given_date:str):
    """Function that finds under which season a date falls"""
    # dummy leap year to allow input X-02-29 (leap day)
    dummmy_year = 2000

    #Already validated string date tranformed into datetime object
    given_date = datetime.strptime(given_date, '%m/%d/%y')
    # we parce our datetime object to date which makes the comparisons latter on possible
    given_date = given_date.date()
    # since we are intersted on having a year with a leap day we just in case..
    # we replace our year with one that we know will have it
    given_date = given_date.replace(year=dummmy_year)

    # Seasons list: each season has its start and end which were given in the problem's document
    seasons = [('Winter', (date(dummmy_year,  1,  1),  date(dummmy_year,  3, 18))),
            ('Spring', (date(dummmy_year,  3, 19),  date(dummmy_year,  6, 19))),
            ('Summer', (date(dummmy_year,  6, 20),  date(dummmy_year,  9, 21))),
            ('Fall', (date(dummmy_year,  9, 22),  date(dummmy_year, 12, 20))),
            ('Winter', (date(dummmy_year, 12, 21),  date(dummmy_year, 12, 31)))]

    # Return de value (season) within the list that fits the criteria start <= given_date <= end
    return next(season for season, (start, end) in seasons
                if start <= given_date <= end)
