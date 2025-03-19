import pymysql

def connect_db():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="gloryspurs123",
        database="BillingApp"
    )

def insert_customer(name, email, phone):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO Customers (name, email, phone) VALUES (%s, %s, %s)", (name, email, phone))
    db.commit()
    db.close()

def insert_bill(customer_id, amount):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO Bills (customer_id, amount) VALUES (%s, %s)", (customer_id, amount))
    db.commit()
    db.close()

def fetch_customers():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Customers")
    data = cursor.fetchall()
    db.close()
    return data

def fetch_bills():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Bills")
    data = cursor.fetchall()
    db.close()
    return data
