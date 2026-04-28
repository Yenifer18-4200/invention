
import sqlite3

def register_product():
    # Brigde to the database
    connection = sqlite3.connect("tienda_virtual.db")
    cursor = connection.cursor()

    print("//// Product Registration ////")
    # collecting data from the terminal
    name = input("Enter the product name: ")
    # using float() beacause price has decimals
    price = float(input("Enter the product price: "))
    # using int() because stock is a whole number
    stock = int(input("Enter the product stock: "))

    try:
        #SQL command  to insert the data into the products table
        cursor.execute('''
            INSERT INTO Product (name, price, stock)
            VALUES (?, ?, ?)
        ''', (name, price, stock))
        
        connection.commit()
        print(f"\nSuccessfully registered the product: '{name}' has been added to the catalog.")
    
    except Exception as e:
        print(f"\nAn error occurred: {e}")

    finally:
        connection.close()

if __name__ == "__main__":
    register_product()


        
        




