import numpy as np

ini_ts = 788400
ts = 80

months_str = ['Jan','Feb','Mar','Apr','May','Jun',
              'Jul','Aug','Sep','Oct','Nov','Dec']
months = np.array([31,28,31,30,31,30,31,31,30,31,30,31])
months_leap = np.array([31,29,31,30,31,30,31,31,30,31,30,31])

cum_months = months.cumsum()
cum_months_leap = months_leap.cumsum()

monthly_ts = ini_ts + (cum_months * (86400/ts))
monthly_leap_ts = ini_ts + (cum_months_leap * (86400/ts))

for i, month in enumerate(months_str):
    print (month, ': ', monthly_ts[i])
print ('')
for i, month in enumerate(months_str):
    print (month, ': ', monthly_leap_ts[i])
