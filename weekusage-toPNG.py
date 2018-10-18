import matplotlib.pyplot as plt
from matplotlib.dates import datetime as dt
import matplotlib.dates as mdates
from dateutil import tz
from datetime import datetime
import sqlite3

L1 = []
L2 = []
L3 = []
tijd = []
tijd2 = []

conn = sqlite3.connect('/home/warddr/powerusage.sqlite3')
c = conn.cursor()
for row in c.execute("select * from powerusage where Timestamp >= Datetime('now', '-7 days');"):
    L1.append(row[1])
    L2.append(row[2])
    L3.append(row[3])
    utc = datetime.strptime(row[4], '%Y-%m-%d %H:%M:%S')
    tijd.append(utc)
conn.commit()
conn.close()

plt.plot(tijd, L1, label='L1')
plt.plot(tijd, L2, label='L2')
plt.plot(tijd, L3, label='L3')
plt.suptitle("Power consumption per phase last week")
plt.title("1 minute average")
plt.gcf().autofmt_xdate()
myFmt = mdates.DateFormatter('%d/%m')
plt.gca().xaxis.set_major_formatter(myFmt)
plt.ylabel('Power (W)')
plt.xlabel('Current: ' + str(round(L1[-1] + L2[-1] + L3[-1],2))  + 'W\nAverage: ' + str(round(sum(L1)/float(len(L1)) + sum(L2)/float(len(L2)) +sum(L3)/float(len(L3)) ,2))+"W")
plt.savefig("/var/www/vloer.ko-lab.space/verbruikweek.png")
