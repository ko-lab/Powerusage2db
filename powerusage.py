import urllib.request, json

import sqlite3

with urllib.request.urlopen("http://10.90.154.40/minuteavg") as url:
    data = json.loads(url.read().decode())
    #print(data[0]['Power']['L1'])
    sql = ("INSERT INTO powerusage(L1,L2,L3) VALUES (" + str(data[0]['Power']['L1']) +","+str(data[0]['Power']['L2'])+","+str(data[0]['Power']['L3']) +");")
    conn = sqlite3.connect('/home/warddr/powerusage.sqlite3')
    c = conn.cursor()
    c.execute(sql)
    conn.commit()
    conn.close()
