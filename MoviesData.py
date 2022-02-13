import sqlite3
connection=sqlite3.connect("myDatabase.db")
cursor=connection.cursor()

Query1="""
        CREATE TABLE movies2(
        Movie_Name TEXT,
        Actor_Name TEXT,
        Actress_Name TEXT,
        Director_Name TEXT,
        Year_Of_Release TEXT);"""

cursor.execute(Query1)

details=[("Iron Man 1","Robert Downey.Jr","Gwyneth Paltrow","Shane Black","2008"),
         ("2.O","Rajinikanth","Amy Jackson","S.Shankar","2018"),
         ("Spiderman No Way Home","Tom Holland","Zendaya","Jon Watts","2021"),
         ("Thor Ragnorak","Chris Hemsworth","Natalic Portman","Alan Taylor","2017")]

cursor.executemany('INSERT INTO movies2 VALUES(?,?,?,?,?);',details);

connection.commit()
connection.close()

print("Table Created Successfully!!!")



        
        
