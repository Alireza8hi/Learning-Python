from datetime import datetime, timedelta

start = datetime.now()
end = start + timedelta(days=30)  # how to add some days, minutes, second, .... in our time
end2 = start + timedelta(hours=48)
end3 = start + timedelta(seconds=3600)
end4 = start + timedelta(minutes=180)


x = end - start  # how to calculate between two times

print(start)
print(end)
print(x)
print(type(x), type(start), type(end))
print(x.days)  # days of our time
print(x.seconds)  # seconds of our time
print(x.microseconds)  # microsecond of our time
print(x.total_seconds())  # all of our time base on seconds
print(x.total_seconds() / 60)  # all of our time base on minutes
print(x.total_seconds() / 86400)  # all of our time base on days
print(int(x.total_seconds() / 86400))
