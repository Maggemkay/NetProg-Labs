import sqlite3

score2 = open("score2.txt", encoding="utf-8")

conn = sqlite3.connect("exam.db")
c = conn.cursor()

# remake the table after each run
c.execute("DROP TABLE persons")
c.execute("DROP TABLE scores")

c.execute("""CREATE TABLE persons(
    id INTEGER PRIMARY KEY,
    firstName text,
    lastName text)
    """)
c.execute("""CREATE TABLE scores(
    number INTEGER,
    score INTEGER,
    id INTEGER,
    FOREIGN KEY (id) REFERENCES persons(id) ON DELETE CASCADE
    )""")

for person in score2:
    temp = person.split()

    c.execute("SELECT * FROM persons WHERE firstName=? AND lastName=?", (temp[2], temp[3]))
    a = c.fetchall()

    if len(a) == 0:
        c.execute("INSERT INTO persons VALUES ((SELECT count(*) FROM persons) + 1, ?, ?)", (temp[2], temp[3]))

    c.execute("INSERT INTO scores VALUES (?, ?, (SELECT id FROM persons WHERE firstName=? AND lastName=?))", (temp[1], temp[4], temp[2], temp[3]))

conn.commit()
conn.close()

# Answer to question a)
# SELECT firstName, lastName, SUM(score) FROM persons JOIN scores ON persons.id=scores.id GROUP BY persons.id ORDER BY SUM(score) DESC limit 10;

# Answer to question b)
# SELECT number, SUM(score) FROM scores GROUP BY number ORDER BY SUM(score) limit 10;
