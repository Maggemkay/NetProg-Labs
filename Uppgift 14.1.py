import sqlite3
import urllib.request
import re
import codecs
import datetime

svtPlayUrl = "https://www.svtplay.se/kanaler?channel=tv6"
dateTracker = datetime.datetime.now()
days = 0
maxDays = 30

conn = sqlite3.connect("tvDB")
c = conn.cursor()

# remake the table after each run
c.execute("DROP TABLE simpsons")
c.execute("CREATE TABLE simpsons(date text, time text, season INTEGER, episode INTEGER, totalEpisodes INTEGER)")

while days < maxDays:
    # Get the episodes and air-times
    page = urllib.request.urlopen(svtPlayUrl + "&date=" + dateTracker.strftime("%Y-%m-%d"))
    svtPage = page.read().decode("utf-8")

    playListFromScript = re.findall(r"programs\":(.*?)\"schedules\":", str(svtPage))
    allSimp = re.findall(r"{[^}]*\"Simpsons\"}", str(playListFromScript))

    simpDetails = []
    for episode in allSimp:
        simpDetails.append(re.findall(r"publishingTime...(\d\d\d\d.\d\d.\d\d).(\d\d.\d\d).*Säsong.(\d?[|*\d]).*Del.(\d?[|*\d]).*av.(\d?[|*\d])", str(episode)))  

    for detail in simpDetails:
        c.execute("SELECT * FROM simpsons WHERE season = {} AND episode = {}".format(detail[0][2], detail[0][3]))
        checkDuplicates = c.fetchall()
        if len(checkDuplicates) == 0:
            c.execute("INSERT INTO simpsons VALUES (?, ?, ?, ?, ?)", (detail[0][0], detail[0][1], detail[0][2], detail[0][3], detail[0][4]))

    # DEBUG
    for a in simpDetails:
        print(a)

    dateTracker += datetime.timedelta(days = 1)
    days += 1


conn.commit()
conn.close()




