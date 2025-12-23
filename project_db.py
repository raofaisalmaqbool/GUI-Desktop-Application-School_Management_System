import pymysql as mq
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME


def get_server_connection():
    return mq.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD)


def get_db_connection():
    return mq.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)


def create_db(db_name=None):
    my_obj = get_server_connection()  # crate connection with database
    cursor_obj = my_obj.cursor()  # 3 create object of cursor
    # start use of try and except
    try:
        db_to_create = db_name or DB_NAME
        db = f"create database {db_to_create}"
        cursor_obj.execute(db)
        # print(f"{db_name} database created")

    except:
        print("database error")


# ====== this function is used to create new table ===========
def create_table(table_name, labels):
    conn_obj = get_db_connection()
    cursor_obj = conn_obj.cursor()
    try:
        # cr_table = f"create table if not exists {table_name} (id INT AUTO_INCREMENT PRIMARY KEY)"
        cr_table = f"CREATE TABLE IF NOT EXISTS {table_name} ({labels})"
        cursor_obj.execute(cr_table)
        # print(f"{table_name} table created")
    except:
        print("table error")


# ========= this function will insert data in the table ==========
def insert_data(table_name, labels, input_data):
    conn_obj = get_db_connection()
    cursor_obj = conn_obj.cursor()
    try:
        placeholders = ", ".join(["%s"] * len(input_data))
        ins_data = f"INSERT INTO {table_name} {labels} VALUES ({placeholders})"
        cursor_obj.execute(ins_data, input_data)     # it will execute the command but not show data into the tabel
        conn_obj.commit()     # this command will show the data into the table
        # messagebox.showinfo("Success","Record Entered Successfully") 
        # print(f"{table_name} data inserted")
        # print(cursor_obj)
    except Exception as ex:
        print(ex)


#======= this function will fetch the all data form table ========== 
def fetch_tabel_data(table_name):
    conn_obj = get_db_connection()
    cursor_obj = conn_obj.cursor()
    try:
        cursor_obj.execute(f"select * from {table_name}")    # will execute the statment
        all_data = cursor_obj.fetchall()    # fetch all data of table
        # print(all_data)
        return all_data         # return the data 
    except Exception as ex:
        print(ex)
        
# ======== this function will fetch one record ==========
def fetch_tabel_data_one(table_name, cl_name, conndition):
    conn_obj = get_db_connection()
    cursor_obj = conn_obj.cursor()
    try:
        query = f"SELECT * FROM {table_name} WHERE {cl_name}=%s"
        cursor_obj.execute(query, (conndition,))    # will execute the statment
        one_data = cursor_obj.fetchone()    # fetch all data of table
        # print(one_data)
        return one_data         # return the data 
    except Exception as ex:
        # print(ex)
        return None
        

# ========== this function is for update data from table / row =========
def update_data(table_name, input_data):
    conn_obj = get_db_connection()
    cursor_obj = conn_obj.cursor()
    try:
        ins_data = (
            f"UPDATE {table_name} SET duration=%s, charges=%s, description=%s WHERE name=%s"
        )
        cursor_obj.execute(ins_data, input_data)     # it will execute the command but not show data into the tabel
        conn_obj.commit()     # this command will show the data into the table
        # messagebox.showinfo("Success","Record Updated Successfully") 
        # print(f"{table_name} data inserted")
        print("cursor_obj")
    except Exception as ex:
        print(ex)


# =========== this function will work for delete record form database ======
def delete_record(table_name,by_name):
    conn_obj = get_db_connection()
    cursor_obj = conn_obj.cursor()
    try:
        del_data = f"DELETE from {table_name} WHERE name=%s"
        cursor_obj.execute(del_data, (by_name,))
        conn_obj.commit()
        print("data deleted")
    except Exception as ex:
        print(ex)

# ========= this will retrive data by searching in search box ==========
def search_data(table_name, search_txt):
    conn_obj = get_db_connection()
    cursor_obj = conn_obj.cursor()
    try:
        pattern = f"%{search_txt}%"
        srch_data = f"SELECT * FROM {table_name} WHERE name like %s"
        cursor_obj.execute(srch_data, (pattern,))
        retrive_data = cursor_obj.fetchall()   # fetch all exist data / rows
        return retrive_data
    except Exception as ex:
        print(ex)


def insert_student(data):
    conn_obj = get_db_connection()
    cursor_obj = conn_obj.cursor()
    try:
        ins_data = (
            "INSERT INTO student (roll_no, name, email, gender, state, address) "
            "VALUES (%s, %s, %s, %s, %s, %s)"
        )
        cursor_obj.execute(ins_data, data)
        conn_obj.commit()
    except Exception as ex:
        print(ex)


def fetch_all_students():
    conn_obj = get_db_connection()
    cursor_obj = conn_obj.cursor()
    try:
        cursor_obj.execute(
            "SELECT id, roll_no, name, email, gender, state, address FROM student"
        )
        return cursor_obj.fetchall()
    except Exception as ex:
        print(ex)
        return []


def fetch_student_by_roll(roll_no):
    conn_obj = get_db_connection()
    cursor_obj = conn_obj.cursor()
    try:
        cursor_obj.execute(
            "SELECT id, roll_no, name, email, gender, state, address FROM student WHERE roll_no=%s",
            (roll_no,),
        )
        return cursor_obj.fetchone()
    except Exception as ex:
        print(ex)
        return None


def update_student(data):
    conn_obj = get_db_connection()
    cursor_obj = conn_obj.cursor()
    try:
        upd = (
            "UPDATE student SET name=%s, email=%s, gender=%s, state=%s, address=%s "
            "WHERE roll_no=%s"
        )
        cursor_obj.execute(upd, data)
        conn_obj.commit()
    except Exception as ex:
        print(ex)


def delete_student(roll_no):
    conn_obj = get_db_connection()
    cursor_obj = conn_obj.cursor()
    try:
        del_data = "DELETE FROM student WHERE roll_no=%s"
        cursor_obj.execute(del_data, (roll_no,))
        conn_obj.commit()
    except Exception as ex:
        print(ex)


def search_students(search_txt):
    conn_obj = get_db_connection()
    cursor_obj = conn_obj.cursor()
    try:
        pattern = f"%{search_txt}%"
        srch_data = (
            "SELECT id, roll_no, name, email, gender, state, address FROM student "
            "WHERE roll_no LIKE %s OR name LIKE %s"
        )
        cursor_obj.execute(srch_data, (pattern, pattern))
        return cursor_obj.fetchall()
    except Exception as ex:
        print(ex)

# create_db("project_lms")
# create_table("course", "cid INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), duration VARCHAR(255), charges VARCHAR(255), description TEXT")
# # insert_data("course", '''(name, duration, charges, description)''', '''("faisal","3 months","4500","abc")''')
# # fetch_tabel_data("course")
# h = "faisal"
# exname = str(h)
# fetch_tabel_data_one("course", "name", exname)
# tup = ("John",36,"jdkjf","faisal")
# update_data("course", tup)
