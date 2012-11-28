mport serial
import re
import MySQLdb

dbName = "your_database_name"
tblName = "consumption"
uName = "your_username"
pswd = "your_password"

ser = serial.Serial(
                port='/dev/ttyUSB0',
                baudrate=57600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS
)
db=MySQLdb.connect(user=uName, passwd=pswd,db=dbName)

c = db.cursor()
prevWatts = 0
deltaT = 0

while 1:
        line=""
        line = ser.readline()   #read a '\n' terminated line
        print line #prints the output so you can see it working
        m = re.search('.*<ch1><watts>[0]*([1-9][0-9]*).*',line)
        n = re.search('.*<time>([0-9][0-9]):([0-9][0-9]):([0-9][0-9]).*',line)
        o = re.search('.*<tmpr>([0-9\.]*)</tmpr>.*',line)
        if m is not None:
                watts = m.group(1)
                hours = n.group(1)
                mins = n.group(2)
                secs = n.group(3)
                temp = o.group(1)

                totalTime = (int(hours)*3600) + (int(mins)*60) + int(secs)

                if deltaT == 0:
                        deltaT = 6

                else:
                        deltaT = int(totalTime) - int(prevTime)

                prevTime = totalTime
                deltaW = int(watts) - int(prevWatts)
                prevWatts = int(watts)
                joules = (prevWatts + int(watts))*0.5*deltaT

                c.execute("INSERT INTO consumption (power, temp, joules, time) VALUES (%s, %s, %s, NOW())",(watts,temp,joules))

                #prints individual readings, so you can check it is working
                print watts+"W"
                print hours+":"+mins+":"+secs
                print temp+"C"
                print deltaT
                print deltaW
