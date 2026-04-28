import os
import sqlite3
from generate_invoice import generate_invoice

def clear_screen():
    """Clears the terminal screen based on the operating system."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_inventory():
    """Displays the summary of the inventory from the database."""
    
    try:
        conn = sqlite3.connect("tienda_virtual.db")
        cursor = conn.cursor()

        print("\n" + "-"*15 + " [ CURRENT USERS ] " + "-"*15)
        cursor.execute("SELECT user_id, name, role FROM User ")
        users = cursor.fetchall()
        if not users:
            print("No users found . ")
        for row in users:
            print(f"ID: {row[0]} | Name: {row[1]} | Role: {row[2]}")

        print("\n" + "-"*15 + " [ CURRENT PRODUCTS ] " + "-"*15)
        cursor.execute("SELECT product_id, name, price, stock FROM Product")
        products = cursor.fetchall()
        if not products:
            print("No products found. ")
        for row in products:
            print(f"ID: {row[0]} | Name: {row[1]} | Price: ${row[2]:.2f} | Stock: {row[3]}")
        
        conn.close()

    except sqlite3.OperationalError:
        print("\n[!] Database not found. Please run database.py first")

def main():
    while True:
        print("\n" + "="*45)
        print("     VIRTUAL STORE: ORDER MANAGEMENT")
        print("="*45)
        print("1. View inventory (Users and Products)")
        print("2. Create a new order (insert_order.py)")
        print("3. Add products to an order (insert_order_items.py)")
        print("4. Generate and print an invoice (generate_invoice.py)")
        print("5. Exit ")
        print("="*45)

        #using try-except to handle non- integer input for the option selection
        try:
            user_input = input("Select an option (1-5): ")

            #  If the user does not write anything, so jump to the next cicle
            if not user_input.strip():
                continue

            option = int(user_input)

            if option == 1:
                show_inventory()
            
            elif option == 2:
                print("\nExecuting order creation...")
                os.system("python insert_order.py")

            elif option == 3:
                print("\nExecuting item addition")
                os.system("python insert_order_items.py")

            elif option == 4:
                order_id = input("\nEnter the Order ID to generate the invoice: ")
                if order_id.isdigit():
                    generate_invoice(order_id)
                else:
                    print("[!] Invalid ID format.")
            
            elif option == 5:
                print("\nClosing the application. Goodbye!")
                break

            else:
                print("\n[!] Invalid option. Please try again.")

        except ValueError:
            print("\n[!] Invalid input. Please enter a number between 1 and 5.")
            
if __name__ == "__main__":
     main()
