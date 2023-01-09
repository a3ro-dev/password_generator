import random
import string
import sqlite3

def generate_db():
    
    conn = sqlite3.connect("db\passwords.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE passwords (password text)")
    conn.commit()
    conn.close()

def generate_password(length):
    # generate a random password with the specified length
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return password

def insert_password(password):
    # insert the password into the database
    conn = sqlite3.connect("db\passwords.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO passwords (password) VALUES (?)", (password,))
    conn.commit()
    conn.close()

def check_password(password):
    # check if the password already exists in the database
    conn = sqlite3.connect("db\passwords.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM passwords WHERE password=?", (password,))
    result = cursor.fetchone()
    conn.close()
    if result:
        # password already exists in the database
        return True
    else:
        # password does not exist in the database
        return False

def main():
    # get the desired password length from the user
    length = int(input("Enter the desired password length: "))

    # generate a random password
    password = generate_password(length)

    # check if the password already exists in the database
    while check_password(password):
        # if the password already exists, generate a new one
        password = generate_password(length)

    # password is unique, insert it into the database
    insert_password(password)

    # output the generated password to the user
    print("Your generated password is:", password)

def table_exists(table_name):
    conn = sqlite3.connect("db\passwords.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return True
    else:
        return False

if __name__ == "__main__":
    if table_exists("passwords"):
       print()
    else:
        generate_db()
    main()
