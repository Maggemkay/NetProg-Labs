import re

txt = open("tabla.html", encoding="utf-8")

tabla = txt.read()

allPrograms = re.findall(r"<td.*?>\n(\d\d\.\d\d)\n</td>\n<td.*?>\n<h4.*?>\n(Simpsons)[\S\s]*?.*Säsong.(\d?[|*\d]).*Del.(\d?[|*\d]).*av.(\d?[|*\d])\..(.*?)\s</p>", str(tabla))

simpDetails = []
for episode in allPrograms:
    print("------------------------")
    print("Serie:     {}".format(episode[1]))
    print("Tid:       {}".format(episode[0]))
    print("Säsong:    {}".format(episode[2]))
    print("Avsnitt:   {} av {}".format(episode[3], episode[4]))
    print("Tid: {}".format(episode[5]))
    print("\n")


txt.close()