import sqlite3
from sqlite3 import Error


############### Function Definitions *******************
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")


    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")




def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")




####### Connect/Create to the Sqlite3 Database File ***********
connection = create_connection("data")




###################  Create staff table variable query #####
print("create staff table variable query")
create_staff_member_table_query = """
CREATE TABLE IF NOT EXISTS staff (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  cell TEXT NOT NULL,
  position TEXT NOT NULL
);
"""
############### Executive query to create staff table #################
execute_query(connection, create_staff_member_table_query) 




################# Create insert query to add staff members to staff table #######
add_staff_members_query = """
INSERT INTO
  staff (name,cell,position)
VALUES
  ('Baba','510.205.0980','Senior Innovation Educator'),
  ('Brandon','111.111.1111', 'Executive Director'),
  ('Hodari','(510) 435-2594','Curriculum Lead'),
  ('Akeeem','(415) 684-0505','Programs Director');
"""
###############  Execute insert staff members query ############
print("execute query")
execute_query(connection, add_staff_members_query)




################## Display staff_member Query #########
print("display staff members")
display_staff_query = "SELECT * from staff"
staff = execute_read_query(connection, display_staff_query)


for user in staff:
  print(user)


execute_query(connection,'drop table staff')
