import sqlite3

def crear_tablas():
    # Creamos la conexión y el archivo de la base de datos
    conexion = sqlite3.connect("tienda_virtual.db")
    cursor = conexion.cursor()

    # Tabla User
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS User (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(100) NOT NULL,
        email VARCHAR(150) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL,
        role VARCHAR(20) NOT NULL
    )
    ''')

    # Tabla Product
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Product (
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(100) NOT NULL,
        price DECIMAL(10,2) NOT NULL,
        stock INTEGER NOT NULL
    )
    ''')

    # Tabla Order
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS "Order" (
        order_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        total_amount DECIMAL(10,2) NOT NULL,
        status VARCHAR(20) NOT NULL,
        FOREIGN KEY (user_id) REFERENCES User (user_id)
    )
    ''')

    # Tabla Order_items
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Order_items (
        order_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id INTEGER NOT NULL,
        product_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        FOREIGN KEY (order_id) REFERENCES "Order" (order_id),
        FOREIGN KEY (product_id) REFERENCES Product (product_id)
    )
    ''')

    conexion.commit()
    print("¡Base de datos y tablas creadas con éxito siguiendo el ERD!")
    conexion.close()

if __name__ == "__main__":
    crear_tablas()