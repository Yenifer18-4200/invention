import sqlite3

def show_inventory():
    connection = sqlite3.connect("tienda_virtual.db")
    cursor = connection.cursor()

    print("\n--- REGISTERED USERS ---")
    try:
        # * Bring all the columns without mattering its name
        cursor.execute("SELECT * FROM user")
        user = cursor.fetchall()
        for u in user:
            # print for seeing what is inside
            print(f"Data found: {u}")
    except Exception as e:
        print(f"Error in user table: {e}")

    print("\n--- REGISTERED PRODUCTS --- ")
    try:
        cursor.execute("SELECT * FROM product")
        product = cursor.fetchall()
        for p in product:
            print(f"Data found: {p}")
    except Exception as e:
        print(f"Error in product table: {e}")
    connection.close()

if  __name__ == "__main__":
    show_inventory()
