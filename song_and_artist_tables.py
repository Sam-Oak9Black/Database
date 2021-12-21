# Import necessary Libraries and Classes
import sqlite3
from sqlite3 import Error

#************ Create Query Strings  *************#

# Song List Table
create_song_table_query = """
CREATE TABLE IF NOT EXISTS song_list(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  artist TEXT NOT NULL,
  year TEXT NOT NULL
);
"""

# Songs
add_song_list_query = """
INSERT INTO
  song_list (name,artist,year)
VALUES
  ('Down Under','Men At Work','1981'),
  ('ONE LIFE','The Pillows','1998'),
  ('Catch Your Dream','Mouse Rat','2012'),
  ('I Can See It In Your Eyes','Men At Work','1981'),
  ("Runner's High","The Pillows","1999"),
  ('The Way You Look Tonight','Mouse Rat','2010');
"""

# Artist List Table
create_artist_table_query = """
CREATE TABLE IF NOT EXISTS artist_list(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  artist TEXT NOT NULL,
  record_label TEXT NOT NULL
);
"""

# Artists
add_artist_list_query = """
INSERT INTO
  artist_list (artist,record_label)
VALUES
  ('Men at Work','Sony Music Entertainment'),
  ('The Pillows','King Records'),
  ('Mouse Rat','Dualtone Records');
"""

# Select Statement
display_song_list_query = "SELECT * from song_list"
display_artist_list_query = "SELECT * from artist_list"

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
execute_query(connection, create_song_table_query)
execute_query(connection, create_artist_table_query) 

# Execute Query to Insert Data
execute_query(connection, add_song_list_query)
execute_query(connection, add_artist_list_query)

# Return results from select query
songs = execute_read_query(connection, display_song_list_query)
artists = execute_read_query(connection, display_artist_list_query)

# Print each song's info
for song in songs:
  print(song)

# Print each artist's info
for artist in artists:
  print(artist)

# Delete the Song List Table
execute_query(connection,'drop table song_list')

# Delete the Artist List Table
execute_query(connection,'drop table artist_list')
