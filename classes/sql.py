import sqlite3

connection = sqlite3.connect("./databases/database.db")
cursor = connection.cursor()
connection.commit()


def products(catagory):
    return cursor.execute("Select * from products where catagory_id = (select id from catagories where catagory_name=?)", (catagory,)).fetchall()

def getproductByID(id):
    return cursor.execute("Select * from products where id = ?", (id,)).fetchall()

def logIn(number, password):
    if len(cursor.execute("Select * from users where phone = ? and password = ?", (number, password, )).fetchall()) == 1:
        return True
    else:
        return False

def getUserid(number, password):
    return cursor.execute("Select * from users where phone = ? and password = ?", (number, password, )).fetchall()[0][0]

def registr(number, password, f_name, l_name):
    cursor.execute("Insert into users(phone, password) values(?, ?)", (number, password,))
    connection.commit()
    cursor.execute("Insert into users_info(user_id, f_name, l_name) values(?, ?, ?)", (getUserid(number, password), f_name, l_name,))
    connection.commit()

def getUserInfo(id):
    result = cursor.execute("SELECT * FROM users_info WHERE user_id = ?", (id,)).fetchall()[0]
    return result[1], result[2], cursor.execute("Select * from users where id = ?", (id,)).fetchall()[0][1], result[3]

def updateUserInfo(id, f_name, l_name, phone, address):
    cursor.execute("update users_info set f_name = ?, l_name = ?, address = ? where user_id = ?", (f_name, l_name, address, id))
    connection.commit()
    cursor.execute("update users set phone = ? where id = ?", (phone, id,))
    connection.commit()

def updatePassword(id, password):
    cursor.execute("update users set password = ? where id = ?", (password, id,))
    connection.commit()

def checkPassword(id, password):
    return cursor.execute("Select * from users where id = ?", (id,)).fetchall()[0][2] == password