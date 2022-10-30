import sqlite3
from datetime import datetime

connection = sqlite3.connect("data/database.db")
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

def logIn_admin(username, password):
    if len(cursor.execute("Select * from admins where admin_name = ? and password = ?", (username, password, )).fetchall()) == 1:
        return True
    else:
        return False

def getAdminid(username, password):
    return cursor.execute("Select * from admins where admin_name = ? and password = ?", (username, password, )).fetchall()[0][0]

def updateAdminInfo(id, f_name, l_name, phone, address, male):
    cursor.execute("update admins_info set f_name = ?, l_name = ?, phone = ?, address = ?, male = ? where admin_id = ?",
                   (f_name, l_name, phone, address, male, id))
    connection.commit()

def updateAdminPassword(id, password):
    cursor.execute("update admins set password = ? where id = ?", (password, id,))
    connection.commit()

def registr(number, password, f_name, l_name):
    cursor.execute("Insert into users(phone, password) values(?, ?)", (number, password,))
    connection.commit()
    cursor.execute("Insert into users_info(user_id, f_name, l_name) values(?, ?, ?)", (getUserid(number, password), f_name, l_name,))
    connection.commit()

def getUserInfo(id):
    result = cursor.execute("SELECT * FROM users_info WHERE user_id = ?", (id,)).fetchall()[0]
    return result[1], result[2], cursor.execute("Select * from users where id = ?", (id,)).fetchall()[0][1], result[3], result[4]

def getAdminInfo(id):
    r = cursor.execute("SELECT * FROM admins_info WHERE admin_id = ?", (id,)).fetchall()[0]
    return r[1], r[2], r[3], r[4], r[5]

def updateUserInfo(id, f_name, l_name, phone, address, male):
    cursor.execute("update users_info set f_name = ?, l_name = ?, address = ?, male = ? where user_id = ?", (f_name, l_name, address, male, id))
    connection.commit()
    cursor.execute("update users set phone = ? where id = ?", (phone, id,))
    connection.commit()

def updatePassword(id, password):
    cursor.execute("update users set password = ? where id = ?", (password, id,))
    connection.commit()

def checkPassword(id, password):
    return cursor.execute("Select * from users where id = ?", (id,)).fetchall()[0][2] == password

def checkAdminPassword(id, password):
    return cursor.execute("Select * from admins where id = ?", (id,)).fetchall()[0][2] == password

def addorder(id, orders):
    now = datetime.now()
    cursor.execute("Insert into order_list(user_id, time, status) values(?, ?, ?)", (id, now, "Yuborilgan"))
    connection.commit()
    orderID = cursor.execute("SELECT * FROM order_list WHERE user_id = ? and time = ?", (id, now)).fetchall()[0][0]

    for productID, product in orders.items():
        cursor.execute("Insert into orders(id, product_id, count) values(?, ?, ?)", (orderID, productID, product['count']))
        connection.commit()

def getOrderHistory(id, a, b, c, d):
    query = "status = NULL"
    if a:
        query += " or status = 'Yuborilgan'"
    if b:
        query += ' or status = "Yo\'lda"'
        # query += " or status = "Yo'lda"'
    if c:
        query += " or status = 'Qabul qilingan'"
    if d:
        query += " or status = 'Bekor qilingan'"
    return cursor.execute("SELECT * FROM order_list WHERE user_id = ? and " + query + " order by time desc", (id,)).fetchall()