import sqlite3
import urllib.request
import re


page = urllib.request.urlopen("https://www.svtplay.se/kanaler?channel=tv6&date=2018-03-23")
svtSite = page.read()

conn = sqlite3.connect("tvDB")
c = conn.cursor()

#playList = re.findall(r"<ul class=\"play_guide-page-program-list-schedule\"(.*?)<div class=\"play_guide-channel-list__item--single play_guide-page-channel-chooser\">", str(svtSite))
#<a(.*?)</a>

playListFromScript = re.findall(r"programs\":(.*?)\"schedules\":", str(svtSite))

allSimpssons = re.findall(r"{[^}]*\"Simpsons\"}", str(playListFromScript))





# Debug
print(allSimpssons)


