import psycopg2

def connect():
    conn = psycopg2.connect(database="postgres",
                            user="postgres",
                            password="postgres",
                            host="localhost",
                            port=5432)
    return conn

connection = connect()
cursor = connection.cursor() 

def create_user():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    gender = input("Enter gender: ")
    query = f"insert into users(name, age, gender) values ('{name}', {age}, '{gender}')"
    cursor.execute(query) 
    connection.commit()
    
def create_magazine():
    name = input("Enter name: ")
    query = f"insert into magazines(name) values ('{name}')"
    cursor.execute(query)
    connection.commit
    
def magazine_distribution():
    user_id = int(input("Enter user id: "))
    magazine_id = int(input("Enter magazine id: "))
    query = f"insert into magazine_distribution(user_id, magazine_id) values ({user_id}, {magazine_id})"
    cursor.execute(query)
    connection.commit
   
   
    
def read_all_users():
    query = "select * from users" 
    cursor.execute(query) 
    cursor.fetchall()
    
def read_one_user():
    id = int(input("Enter id you want to read: ")) 
    query =  f"select from users where user_id = {id}" 
    cursor.execute(query) 
    row = cursor.fetchone() 
    print(row) 
    
def read_all_magazines():
    query = "select * from magazines" 
    cursor.execute(query) 
    cursor.fetchall()
    
def read_one_magazine():
    id = int(input("Enter id you want to read: ")) 
    query =  f"select from magazines where magazine_id = {id}" 
    cursor.execute(query) 
    row = cursor.fetchone() 
    print(row) 
    
def read_magazine_distributions():
    query = "select * from magazine_distribution"
    cursor.execute(query) 
    cursor.fetchall()
    
def read_one_magazine_distribution():
    id = int(input("Enter id you want to read: ")) 
    query =  f"select from magazine_distribution where id = {id}" 
    cursor.execute(query) 
    row = cursor.fetchone() 
    print(row) 
    
 
    
def update_user():
    id = int(input("Enter id you want to update: "))
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    gender = input("Enter gender: ")
    query = f"update users set name = '{name}', age = '{age}', gender = '{gender}' where user_id = {id}"
    cursor.execute(query)
    connection.commit()
    
def update_magazine():
    id = int(input("Enter id you want to update: "))
    name = input("Enter name: ")
    query = f"update magazines set name = '{name}' where magazine_id = {id}"
    cursor.execute(query)
    connection.commit()
    
def update_magazine_distribution():
    id = int(input("Enter id you want to update: "))
    user_id = int(input("Enter user id: "))
    magazine_id = int(input("Enter magazine id: "))
    query = f"update magazine_distribution set user_id = {user_id}, magazine_id = {magazine_id} where id = {id}"
    cursor.execute(query)
    connection.commit()
    
    
    
def delete_user():
    id = int(input("Enter id you want to delete: "))
    query = f"delete from users where user_id = {id}"
    cursor.execute(query)
    connection.commit()
    
def delete_magazine():
    id = int(input("Enter id you want to delete: "))
    query = f"delete from magazines where magazine_id = {id}"
    cursor.execute(query)
    connection.commit()
    
def delete_magazine_distribution():
    id = int(input("Enter id you want to delete: "))
    query = f"delete from magazine_distribution where id = {id}"
    cursor.execute(query)
    connection.commit()
    
while True:
    table_name = input("Enter table name: ")
    if table_name == "users":
        action = input("Select an action: ")
        if action == "Create" or "create":
            create_user()
        elif action == "Read" or "read":
            one_or_all = input("Read one or all rows?")
            if one_or_all == "Read one":
                read_one_user()
            elif one_or_all == "Read all":
                read_all_users()
        elif action == "Update" or "update":
            update_user()
        elif action == "Delete" or "delete":
            delete_user()
            
    elif table_name == "magazines":
            action = input("Select an action: ")
            if action == "Create" or "create":
                create_magazine()
            elif action == "Read" or "read":
                one_or_all = input("Read one or all rows?")
            if one_or_all == "Read one":
                read_one_magazine()
            elif one_or_all == "Read all":
                read_all_magazines()
            elif action == "Update" or "update":
                update_magazine()
            elif action == "Delete" or "delete":
                delete_magazine()
                
    elif table_name == "magazine_distribution":
            action = input("Select an action: ")
            if action == "Create" or "create":
                magazine_distribution()
            elif action == "Read" or "read":
                one_or_all = input("Read one or all rows?")
            if one_or_all == "Read one":
                read_one_magazine_distribution()
            elif one_or_all == "Read all":
                read_magazine_distributions()
            elif action == "Update" or "update":
                update_magazine_distribution()
            elif action == "Delete" or "delete":
                delete_magazine_distribution()