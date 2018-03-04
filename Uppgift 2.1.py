people = open("score2.txt", "r")

total = {}

for person in people:
    temp = person.split()
    name = temp[2] + " " + temp[3]
    if(name not in total):
        total[name] = 0
    total[name] = total[name] + int(temp[4])

inOrder = []

for item in total:
    temp = (item, total[item])
    inOrder.append(temp)

scores = sorted(inOrder, key=lambda score: score[1], reverse = True)


print(scores)