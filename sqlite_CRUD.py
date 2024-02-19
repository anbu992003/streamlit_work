import sqlite3

# Connect to SQLite database (creates a new database if it doesn't exist)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    age INTEGER
                )''')

# Function to insert data into the table
def create_user(name, age):
    cursor.execute('''INSERT INTO users (name, age) VALUES (?, ?)''', (name, age))
    conn.commit()
    print("User created successfully!")

# Function to retrieve all users
def read_users():
    cursor.execute('''SELECT * FROM users''')
    users = cursor.fetchall()
    for user in users:
        print(user)

# Function to update user details
def update_user(id, new_name, new_age):
    cursor.execute('''UPDATE users SET name = ?, age = ? WHERE id = ?''', (new_name, new_age, id))
    conn.commit()
    print("User details updated successfully!")

# Function to delete a user
def delete_user(id):
    cursor.execute('''DELETE FROM users WHERE id = ?''', (id,))
    conn.commit()
    print("User deleted successfully!")

# Example usage
create_user("John Doe", 30)
create_user("Jane Smith", 25)

read_users()

update_user(1, "John Updated", 35)

delete_user(2)

read_users()

# Close the connection
conn.close()