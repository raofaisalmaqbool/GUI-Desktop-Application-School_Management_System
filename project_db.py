from logging import root
import pymysql as mq
from tkinter import ttk, messagebox

def create_db(db_name=None):
    my_obj = mq.connect(host="localhost", user="root", password="")  # crate connection with database
    cursor_obj = my_obj.cursor()  # 3 create object of cursor
    # start use of try and except
    try:
        # db = f"create database if not exists {db_name}"
        db = f"create database {db_name}"
        cursor_obj.execute(db)
        # print(f"{db_name} database created")

    except:
        print("database error")

def create_table(table_name, labels):
    conn_obj = mq.connect(host="localhost", user="root", password="", database="project_lms")
    cursor_obj = conn_obj.cursor()
    try:
        # cr_table = f"create table if not exists {table_name} (id INT AUTO_INCREMENT PRIMARY KEY)"
        cr_table = f"create table {table_name} ({labels})"
        cursor_obj.execute(cr_table)
        # print(f"{table_name} table created")
    except:
        print("table error")

def insert_data(table_name, labels, input_data):
    conn_obj = mq.connect(host="localhost", user="root", password="", database="project_lms")
    cursor_obj = conn_obj.cursor()
    try:
        ins_data = f"INSERT INTO {table_name} {labels} VALUES {input_data}"
        cursor_obj.execute(ins_data)     # it will execute the command but not show data into the tabel
        conn_obj.commit()     # this command will show the data into the table
        # messagebox.showinfo("Success","Record Entered Successfully") 
        # print(f"{table_name} data inserted")
        # print(cursor_obj)
    except Exception as ex:
        print(ex)

def fetch_tabel_data(table_name):
    conn_obj = mq.connect(host="localhost", user="root", password="", database="project_lms")
    cursor_obj = conn_obj.cursor()
    try:
        cursor_obj.execute(f"select * from {table_name}")
        all_data = cursor_obj.fetchall()
        return all_data
    except Exception as ex:
        print(ex)

create_db("project_lms")
create_table("course", "cid INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), duration VARCHAR(255), charges VARCHAR(255), description TEXT")
# insert_data("course", '''(name, duration, charges, description)''', '''("faisal","3 months","4500","abc")''')