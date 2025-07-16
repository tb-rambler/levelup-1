# работа со временем (год, месяц, день, время)

import datetime

# feb = datetime.date(2025, 2, 15)

# print(feb)

# today_date = datetime.date.today()
# print(today_date)

# some_date = datetime.date.fromtimestamp(2038454430)
# print(some_date.year)
# print(some_date.month)
# print(some_date.day)

# null_time = datetime.time()
# print(null_time)

# some_time = datetime.time(11, 45, 15, 5)
# print(some_time)
# print(some_time.hour)
# print(some_time.minute)
# print(some_time.second)
# print(some_time.microsecond)

# date_and_time = datetime.datetime(2025, 7, 14, 19, 51, 20)
# print(date_and_time)

# current = datetime.datetime.now()
# print(current)
# print(current.time())
# print(current.date())
# print(current.timestamp())

# some_interval = datetime.timedelta(days=1, seconds=5, microseconds=0, milliseconds=0, minutes=15, hours=2, weeks=3)

# some_delta = datetime.datetime.now() - some_interval

# print(some_delta)


# print(datetime.datetime.now().strftime("%m%d/%Y, %H:%M:%S"))

# date_from_string = datetime.datetime.strptime("21 November, 2024", "%d %B, %Y")
# print(date_from_string)

import pytz

timezone_moscow = pytz.timezone("Europe/Berlin")
moscow_time = datetime.datetime.now(timezone_moscow)
print(moscow_time)
