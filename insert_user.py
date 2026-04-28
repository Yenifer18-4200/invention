import sqlite3

def register_user():
    #1. Conexión: conectamos a la base de datos
    connection = sqlite3.connect("tienda_virtual.db")

    #2. Cursor: The messenger that executes SQL commands
    cursor = connection.cursor()

    print("**** User Registration ****")
    full_name = input("Enter your full name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    role = input("Enter your role (customer/admin): ")

    try:
        # 3. Execution: Using the exact table and column names from the ERD
        cursor.execute('''INSERT INTO user (name, email, password, role) 
        VALUES (?, ?, ?, ?)''', (full_name, email, password, role))

        # 4. Commit: Save the changes to the database
        connection.commit()
        print(f"\nSucessfully registered user: {full_name} with email: {email} and role: {role}")

    except sqlite3.IntegrityError:
        # This error occurs if the email is not unique (violating the unique constraint)
        print("\nError: The email you entered is already registered. Please use a different email.")

    finally: 
        # 5. Close: Always close the connection to free up resources
        connection.close()

if __name__ == "__main__":
     register_user()    
