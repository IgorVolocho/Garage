import sqlite3 as sq

connection = sq.connect('Garage.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS People
              (name TEXT, old INTEGER, date TEXT, car TEXT)''')#Create Table
cursor.execute('''CREATE TABLE IF NOT EXISTS Cars
              (mark TEXT, number_of_the_car TEXT)''')


def add_person(List_info):
    connection = sq.connect('Garage.db')
    cursor = connection.cursor()
    cursor.execute(
        f"INSERT INTO People VALUES {List_info}")#Add
    connection.commit()
    connection.close()


def add_car(List_info):
    connection = sq.connect('Garage.db')
    cursor = connection.cursor()
    cursor.execute(
        f"INSERT INTO Cars VALUES {List_info}")#Add
    connection.commit()
    connection.close()


def show_people():
    connection = sq.connect('Garage.db')
    cursor = connection.cursor()
    result = cursor.execute("SELECT * FROM People")
    return result


def show_cars():
    connection = sq.connect('Garage.db')
    cursor = connection.cursor()
    result = cursor.execute("SELECT * FROM Cars")
    return result



# cursor.execute(
#     "INSERT INTO Shows VALUES ('Igor Volokho4', 21, '20.2102')")#Add

# cursor.execute("""DELETE from People where name = 'Igor Volokho3'""")# Delete



connection.commit()
connection.close()