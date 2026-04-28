import sqlite3

def add_items_to_order():
    connection = sqlite3.connect("tienda_virtual.db")
    cursor = connection.cursor()

    print("**** Add Items to Order ****")
    order_id = int(input("Enter the Order ID to add items to: "))
    product_id = int(input("Enter the Product ID to add: "))
    quantity = int(input("Enter the quantity: "))

    try:
        cursor.execute('''
            INSERT INTO Order_items (order_id, product_id, quantity) 
            VALUES (?,?,?)
            ''', (order_id, product_id, quantity))
        connection.commit()
    
        print(f"\nSuccess! Added {quantity} units of Product  {product_id} to Order {order_id}.")
    
    except Exception as e:
        print(f"\nAn error occurred: {e}")

    finally:
        connection.close()

if __name__ == "__main__":
    add_items_to_order()