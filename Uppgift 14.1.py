import sqlite3
import urllib.request
import re
import codecs

file = codecs.open("htmlfile.txt", "w", "utf-8")



# Get the episodes and air-times
page = urllib.request.urlopen("https://www.svtplay.se/kanaler?channel=tv6&date=2018-03-23")
svtPage = page.read().decode("utf-8")

playListFromScript = re.findall(r"programs\":(.*?)\"schedules\":", str(svtPage))
allSimp = re.findall(r"{[^}]*\"Simpsons\"}", str(playListFromScript))

simpEpisode = []
simpTime = []

for episode in allSimp:
    simpEpisode.append(re.findall(r"Säsong.*av \d\d\.", str(episode)))
    simpTime.append(re.findall(r"\"publishingTime\":\"(.*)\",\"longDescription\"", str(episode)))



# Make the Database
conn = sqlite3.connect("tvDB")
c = conn.cursor()

# un-comment if you dont have table or you want to drop the current existing table
# c.execute("CREATE TABLE simpsons(episode text, airTime text)")
# c.execute("DROP TABLE simpsons")

merge = []
for i in range(0, len(simpEpisode)):
    merge.append((simpEpisode[i], simpTime[i]))



#c.execute("INSERT INTO simpsons VALUES (?, ?)", str(simpEpisode[i]) + str(simpTime[i]))







# DEGUG
# testArr = []
# for episode in allSimp:
#     testArr.append(episode)
# for a in testArr:
#     print(a)

# Debug
#print(allSimpssons)

for i in range(0, len(simpEpisode)):
    print(str(simpEpisode[i]))
    print(str(simpTime[i]) + "\n")
  

for i in range(0, len(simpEpisode)):
    a = str(simpEpisode[i]) + "\n" + str(simpTime[i]) + "\n\n"
    file.write(a)
file.close()


