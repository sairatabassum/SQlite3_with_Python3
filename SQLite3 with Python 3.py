import sqlite3

con = sqlite3.connect('student.db')
c = con.cursor()
print("hello")


def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS students(
             first text,
             last text,
             id integer

             )""")


def data_entry():
    c.execute("INSERT INTO students VALUES('SAIRA','TABASSUM',12)")
    con.commit()


def var_data_entry():
    First = "Sara"
    Last = "Tara"
    Id = 15
    c.execute("INSERT INTO Students (first,last,id) VALUES(?,?,?)",
              (First,Last,Id))
    con.commit()


def read():
    # c.execute("SELECT * FROM students") #all data
    # c.execute("SELECT id,first,last  FROM students") #change order of data
    # c.execute("SELECT id,first FROM students")  #select two types of data
    # c.execute("SELECT * FROM students WHERE id=15 AND first='Sara'") #select specific data and use condition

    # By variable
    i = 15;
    f = 'Sara'
    c.execute("SELECT * FROM students WHERE id=? AND first=?",(i,f))

    # Fetch data
    r = c.fetchall()
    for i in r:
        # print(i[0],i[1],i[2])
        print(i)


def delete_and_update():
    '''
    c.execute("UPDATE students SET id=20 WHERE id=13")
    con.commit()
    '''

    # By variable
    po = 12;
    o = 20
    c.execute("UPDATE students SET id=? WHERE id=?",(o,po))
    con.commit()

    # c.execute("DELETE FROM students") #All data deleted
    # c.execute("DELETE FROM students  WHERE id=15 AND last='Tara'") #Specific data deleted
    # con.commit()

    # By variable
    op = 15
    l = 'Tara'
    c.execute("DELETE FROM Students WHERE id=? AND last=?",(op,l,))
    con.commit()

    c.execute("SELECT * FROM students")
    for i in c.fetchall():
        print(i)


create_table()
read()
data_entry()
var_data_entry()
delete_and_update()

