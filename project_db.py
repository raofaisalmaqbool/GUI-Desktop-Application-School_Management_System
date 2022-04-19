import pymysql as mq

def create_db(db_name):
    my_obj = mq.connect(host="localhost", user="root", password="")  # crate connection with database
    cursor_obj = my_obj.cursor()  # 3 create object of cursor
    # start use of try and except
    try:
        db = f"create database {db_name}"
        cursor_obj.execute(db)
        print(f"{db_name} database created")

    except:
        pass

create_db("project_lms")

