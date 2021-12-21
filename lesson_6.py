# Import necessary Libraries and Classes
import sqlite3
from sqlite3 import Error

#************ Create Query Strings  *************#

# Staff Table
create_staff_member_table_query = """
CREATE TABLE IF NOT EXISTS staff (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  cell TEXT NOT NULL,
  position TEXT NOT NULL
);
"""

# Staff Members
add_staff_members_query = """
INSERT INTO
  staff (name,cell,position)
VALUES
  ('Baba','510.205.0980','Senior Innovation Educator'),
  ('Brandon','111.111.1111', 'Executive Director'),
  ('Hodari','(510) 435-2594','Curriculum Lead'),
  ('Akeeem','(415) 684-0505','Programs Director');
"""

# Select Statement
display_staff_query = "SELECT * from staff"

#******** Function Definitions *****************#

# Connect to Database
def create_connection(pathToDatabase):
    connection = None
    try:
        connection = sqlite3.connect(pathToDatabase)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
        
    return connection

# Execute Queries
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
        
#************ End Function Definition *******************

        
#************ Program Starting Point ********************
        
# Connect to Existing or Create the Sqlite3 Database File
connection = create_connection("toDatabase")

# Execute query to create table
execute_query(connection, create_staff_member_table_query) 

# Execute Query to Insert Data
execute_query(connection, add_staff_members_query)

# Return results from select query
staff_members = execute_read_query(connection, display_staff_query)

# Print each employee's info
for employee in staff_members:
  print(employee)

# Delete the Staff Table
#execute_query(connection,'drop table staff')
