import time
import datetime

print(f'datetime.datetime.now(): {datetime.datetime.now()}')

dt = datetime.datetime(2019, 10, 21, 16, 29, 0)
print(f'(dt.year, dt.month,dt.day): {(dt.year, dt.month,dt.day)}')

print(f'(dt.hour, dt.minute, dt.second): {(dt.hour, dt.minute, dt.second)}')


print(
    f'datetime.datetime.fromtimestamp(1000000): {datetime.datetime.fromtimestamp(1000000)}')

# datetime.datetime.fromtimestamp(time.time()) do the same thing as datetime.datetime.now()
print(
    f'datetime.datetime.fromtimestamp(time.time()): {datetime.datetime.fromtimestamp(time.time())}')

# Compare datetime objects
halloween2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)
newyears2020 = datetime.datetime(2020, 1, 1, 0, 0, 0)
oct31_2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)

print(f'halloween2019 == oct31_2019: {halloween2019 == oct31_2019}')
print(f'halloween2019 > newyears2020: {halloween2019 > newyears2020}')
print(f'newyears2020 > halloween2019: {newyears2020 > halloween2019}')
print(f'newyears2020 != oct31_2019: {newyears2020 != oct31_2019}')

# The timedelta Data Type
delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)

print(
    f'(delta.days, delta.seconds, delta.microseconds): {(delta.days, delta.seconds, delta.microseconds)}')

print(f'delta.total_seconds(): {delta.total_seconds()}')
print(f'str(delta): {str(delta)}')

dt = datetime.datetime.now()
print(f'dt: {dt}')
thousandDays = datetime.timedelta(days=1000)
print(f'dt + thousandDays: {dt + thousandDays}')

oct21st = datetime.datetime(2019, 10, 21, 16, 29, 0)
aboutThirtyYears = datetime.timedelta(days=365*30)
print(f'oct21st: {oct21st}')
print(f'oct21 - aboutThirtyYears: {oct21st - aboutThirtyYears}')
print(f'oct21st - (2 * aboutThirtyYears): {oct21st - (2 * aboutThirtyYears)}')

# Pausing Until a Specific Date
halloween2016 = datetime.datetime(2016, 10, 31, 0, 0, 0)
while datetime.datetime.now() < halloween2016:
    time.sleep(1)

# Converting datetime Objects into Strings
ost21st = datetime.datetime(2019, 10, 21, 16, 29, 0)
print(
    f"ost21st.strftime('%Y/%m/%d %H:%M%S'): {ost21st.strftime('%Y/%m/%d %H:%M:%S')}")
print(f"ost21st.strftime('%I:%M %p'): {ost21st.strftime('%I:%M %p')}")
print(f"""oct21st.strftime("%B of '%y"): {oct21st.strftime("%B of '%y")}""")

# Converting Strings into datetime Objects

print(
    f"datetime.datetime.strptime('October 21, 2019', '%B %d, %Y'): {datetime.datetime.strptime('October 21, 2019', '%B %d, %Y')}")
print(
    f"datetime.datetime.strptime('2019/10/21 16:29:00', '%Y/%m/%d %H:%M:%S'): {datetime.datetime.strptime('2019/10/21 16:29:00', '%Y/%m/%d %H:%M:%S')}")

print(
    f"""datetime.datetime.strptime("October of '19", "%B of '%y"): {datetime.datetime.strptime("October of '19", "%B of '%y")}""")

print(
    f"""datetime.datetime.strptime("November of '63", "%B of '%y"): {datetime.datetime.strptime("November of '63", "%B of '%y")}""")
