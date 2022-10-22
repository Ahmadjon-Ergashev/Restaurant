import sqlite3

connection = sqlite3.connect("./databases/database.db")
cursor = connection.cursor()
connection.commit()


def products(catagory):
    return cursor.execute("Select * from products where catagory_id = (select id from catagories where catagory_name=?)", (catagory,)).fetchall()

def get_productByID(id):
    return cursor.execute("Select * from products where id = ?", (id,)).fetchall()
