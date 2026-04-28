import sqlite3
from datetime import datetime

def create_order():
    connection = sqlite3.connect("tienda_virtual.db")
    cursor = connection.cursor()

    print("*** Create Order ***")
    user_id = int(input("Enter user ID: "))
    total_amount = float(input("Enter total amount: "))
    status = input("Enter order status (Pending/Completed/Cancelled): ").capitalize()

    try:
        # don't send order_id because it's autoincrement
        cursor.execute('''
            INSERT INTO "Order" (user_id, total_amount, status)
            VALUES (?, ?, ?)
        ''', (user_id, total_amount, status))

        connection.commit()
        print(f"\nSuccesfully created! Order ID: {cursor.lastrowid}")
    
    except Exception as e:
        print(f"\nAn error occurred: {e}")

    finally:
        connection.close()

if __name__ == "__main__":
    create_order()

    