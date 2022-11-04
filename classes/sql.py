import sqlite3
from datetime import datetime

# Connection
connection = sqlite3.connect("data/database.db")
cursor = connection.cursor()
connection.commit()


# Products
def products(catagory="*"):
    if catagory == "*":
        return cursor.execute("Select * from products").fetchall()
    return cursor.execute(
        "Select * from products where catagory_id = (select id from catagories where catagory_name=?)",
        (catagory,)).fetchall()


def getproductByID(id):
    return cursor.execute("Select * from products where id = ?", (id,)).fetchall()


def updateProductInfo(id, name, price, description, catagory):
    cursor.execute("update products set name = ?, description = ?, price = ?, catagory_id = ? where id = ?",
                   (name, description, price, catagory, id))
    connection.commit()


def addProduct(name, price, description, catagory):
    cursor.execute("Insert into products(name, description, price, catagory_id) values(?, ?, ?, ?)", (name, description, price, catagory))
    connection.commit()


def deleteProduct(id):
    cursor.execute("Delete from products where id = ?", (id,))
    connection.commit()


def getProductid(name, price, description, catagory):
    return cursor.execute("Select * from products where name = ? and description = ? and price = ? and catagory_id = ?",
                          (name, description, price, catagory)).fetchall()[0][0]

# Admins
def addAdmin(username, name, surname, phone, male, address, password, permissions):
    cursor.execute("Insert into admins(admin_name, password) values(?, ?)", (username, password,))
    connection.commit()
    id = getAdminid(username, password)
    cursor.execute("Insert into admins_info(admin_id, f_name, l_name, phone, address, male) values(?, ?, ?, ?, ?, ?)",
                   (id, name, surname, phone, address, male))
    connection.commit()

    cursor.execute("""Insert into admins_permissions(admin_id, orders, addAdmin, editAdmin, editUser, 
                    addProduct, editProduct) values(?, ?, ?, ?, ?, ?, ?)""", (id, *permissions))
    connection.commit()


def admins():
    return cursor.execute("Select * from admins_info").fetchall()


def loginAdmin(username, password):
    if len(cursor.execute("Select * from admins where admin_name = ? and password = ?",
                          (username, password,)).fetchall()) == 1:
        return True
    else:
        return False


def checkUsername(username):
    if len(cursor.execute("Select * from admins where admin_name = ?", (username,)).fetchall()) == 1:
        return False
    else:
        return True


def getAdminid(username, password):
    return cursor.execute("Select * from admins where admin_name = ? and password = ?",
                          (username, password,)).fetchall()[0][0]


def updateAdminInfo(id, username, f_name, l_name, phone, address, male, permissions=()):
    if permissions == ():
        permissions = getAdminPermissions(id)
    cursor.execute("update admins_info set f_name = ?, l_name = ?, phone = ?, address = ?, male = ? where admin_id = ?",
                   (f_name, l_name, phone, address, male, id))
    cursor.execute("update admins set admin_name = ? where id = ?", (username, id))
    connection.commit()
    cursor.execute("""update admins_permissions set orders = ?, addAdmin = ?, editAdmin = ?,
                      editUser = ?, addProduct = ?, editProduct = ? where admin_id = ?""", (*permissions, id))
    connection.commit()


def updateAdminPassword(id, password):
    cursor.execute("update admins set password = ? where id = ?", (password, id,))
    connection.commit()


def deleteAdmin(id):
    cursor.execute("Delete from admins where id = ?", (id,))
    connection.commit()
    cursor.execute("Delete from admins_info where admin_id = ?", (id,))
    connection.commit()
    cursor.execute("Delete from admins_permissions where admin_id = ?", (id,))
    connection.commit()


def getAdminInfo(id):
    r = cursor.execute("SELECT * FROM admins_info WHERE admin_id = ?", (id,)).fetchall()[0]
    username = cursor.execute("SELECT admin_name FROM admins WHERE id = ?", (id,)).fetchall()[0][0]
    return username, r[1], r[2], r[3], r[4], r[5]


def getAdminPermissions(id):
    return cursor.execute("SELECT * FROM admins_permissions WHERE admin_id = ?", (id,)).fetchall()[0][1:]


def checkAdminPassword(id, password):
    return cursor.execute("Select * from admins where id = ?", (id,)).fetchall()[0][2] == password


# Users
def users():
    return cursor.execute("Select * from users_info").fetchall()


def logIn(number, password):
    if len(cursor.execute("Select * from users where phone = ? and password = ?", (number, password,)).fetchall()) == 1:
        return True
    else:
        return False


def getUserid(number, password):
    return cursor.execute("Select * from users where phone = ? and password = ?", (number, password,)).fetchall()[0][0]


def checkPhone(phone):
    if len(cursor.execute("Select * from users where phone = ?", (phone,)).fetchall()) == 1:
        return False
    else:
        return True


def updateUserPassword(id, password):
    cursor.execute("update users set password = ? where id = ?", (password, id,))
    connection.commit()


def registr(number, password, f_name, l_name):
    cursor.execute("Insert into users(phone, password) values(?, ?)", (number, password,))
    connection.commit()
    cursor.execute("Insert into users_info(user_id, f_name, l_name) values(?, ?, ?)",
                   (getUserid(number, password), f_name, l_name,))
    connection.commit()


def getUserInfo(id):
    """Firt name, Last name, Phone, Address, Gender"""
    result = cursor.execute("SELECT * FROM users_info WHERE user_id = ?", (id,)).fetchall()[0]
    return result[1], result[2], cursor.execute("Select * from users where id = ?",
                                                (id,)).fetchall()[0][1], result[3], result[4]


def updateUserInfo(id, f_name, l_name, phone, address, male):
    cursor.execute("update users_info set f_name = ?, l_name = ?, address = ?, male = ? where user_id = ?",
                   (f_name, l_name, address, male, id))
    connection.commit()
    cursor.execute("update users set phone = ? where id = ?", (phone, id,))
    connection.commit()


def checkPassword(id, password):
    return cursor.execute("Select * from users where id = ?", (id,)).fetchall()[0][2] == password


# Orders
def orders_list():
    return cursor.execute("Select * from order_list order by time").fetchall()


def getOrdersByID(id):
    return cursor.execute("Select * from orders where id=?", (id,)).fetchall()


def getOrderListByID(id):
    return cursor.execute("Select * from order_list where id=?", (id,)).fetchall()[0]


def addorder(id, orders):
    now = datetime.now()
    cursor.execute("Insert into order_list(user_id, time, status) values(?, ?, ?)", (id, now, "Yuborilgan"))
    connection.commit()
    orderID = cursor.execute("SELECT * FROM order_list WHERE user_id = ? and time = ?", (id, now)).fetchall()[0][0]

    for productID, product in orders.items():
        cursor.execute("Insert into orders(id, product_id, count) values(?, ?, ?)",
                       (orderID, productID, product['count']))
        connection.commit()


def getOrderHistory(id, sent, accepted, delivered, canceled):
    query = "status = NULL"
    if sent:
        query += " or status = 'Yuborilgan'"
    if accepted:
        query += ' or status = "Qabul qilingan"'
        # query += " or status = "Yo'lda"'
    if delivered:
        query += " or status = 'Yetkazilgan'"
    if canceled:
        query += " or status = 'Bekor qilingan'"
    return cursor.execute("SELECT * FROM order_list WHERE user_id = ? and " + query + " order by time desc",
                          (id,)).fetchall()


def setOrderStatus(id, status, admin_id):
    cursor.execute("update order_list set status = ?, admin_id = ? where id = ?", (status, admin_id, id))
    connection.commit()
