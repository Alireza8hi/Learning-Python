from datetime import datetime
import pytz

tz = pytz.timezone("Asia/Tehran")  # how to access timezone
tz2 = pytz.timezone("America/Mexico_City")
tz3 = pytz.timezone("US/Central")

print(type(tz))

x = datetime.now(tz)  # how to access now time in special timezone
x2 = datetime.now(tz2)
x3 = datetime.now(tz3)
x4 = datetime.now()  # now timezone is your location
print(x)
print(x2)
print(x3)


'''           country_names in pytz
for code, name in pytz.country_names.items():
    print(code, ':', name)
print(pytz.country_names.get("US"))
print(pytz.country_names.keys())
print(list(pytz.country_names.values()))
'''
print(list(pytz.country_timezones))
print(pytz.all_timezones)
print(pytz.common_timezones)
