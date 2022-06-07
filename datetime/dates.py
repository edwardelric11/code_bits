import datetime
import pytz

d = datetime.date(2020, 9, 24)
print(d)

tday = datetime.date.today()
print(tday)


# weekday() - Monday is 0 and Sunday is 6
print(tday.weekday())

# isoweekday() - Monday is 1 and Sunday is 7
print(tday.isoweekday())

tdelta = datetime.timedelta(days=7)

print(tday + tdelta)

#date2 = date1 + timedelta
# timedelta = date1 + date2

# Get days until birthday
bday = datetime.date(2020, 9, 24)

till_bday = bday - tday

print(till_bday.days)

dt = datetime.datetime(2020, 7, 24, 12, 30, 45, tzinfo=pytz.UTC)
print(dt)

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)

# strftime - Datetime to String
# strptime - String to Datetime
dt_str = 'July 24, 2020'
dt2 = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt2)
