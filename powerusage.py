import urllib.request, json

import sqlite3

try:
    url = urllib.request.urlopen("http://10.90.154.40/minuteavg")
    data = json.loads(url.read().decode())
    #print(data[0]['Power']['L1'])
    sql = ("INSERT INTO powerusage(L1,L2,L3) VALUES (" + str(data[0]['Power']['L1']) +","+str(data[0]['Power']['L2'])+","+str(data[0]['Power']['L3']) +");")
    conn = sqlite3.connect('/home/warddr/powerusage.sqlite3')
    c = conn.cursor()
    c.execute(sql)
    conn.commit()
    conn.close()
    f = open("/var/www/vloer.ko-lab.space/spaceapi.json", "w")
    fAPI = open("/home/warddr/Powerusage2db/spaceapi/spaceapi.json","r")
    ApiTemplate = fAPI.read()
    ApiTemplate = ApiTemplate.replace("[[power]]",str(data[0]['Power']['L1']+data[0]['Power']['L2']+data[0]['Power']['L3']))
    if ((data[0]['Power']['L1']+data[0]['Power']['L2']+data[0]['Power']['L3']) < 175):
        ApiTemplate = ApiTemplate.replace("[[state]]","false")
    else:
        ApiTemplate = ApiTemplate.replace("[[state]]","true")
    f.write(ApiTemplate)
    f.close()

except:
    print("Oops!",sys.exc_info()[0],"occured.")
    f = open("/var/www/vloer.ko-lab.space/spaceapi.json", "w")
    f.write("error")
    f.close()

