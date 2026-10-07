import datetime
from math import pi

date = datetime.date(2026, 3, 16)
today = datetime.date.today()

time = datetime.time(minute=30, hour=12, second=0)
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S _ %Y.%m.%d")

target_datetime = datetime.datetime(2030, 1, 2, 12, 3, 0)
current_datetime = datetime.datetime.now()


if target_datetime < current_datetime:
    print("target date has passed")
else:
    print("target date has NOT passed")

  