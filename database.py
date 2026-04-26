import psycopg2 #psycopg2 is a library that lets us connect to PostgreSQL databases and run SQL commands from Python. We will use it to create tables and insert data into our database. 
import os   #we need os to read from files and environment variables.
from dotenv import load_dotenv

#.env stands for "environment variables" and is a common convention for storing sensitive information like API keys and database credentials. 
load_dotenv()

#this is a reusable function. Anytime any file in our project needs to talk to the database, it calls this function instead of rewriting the connection details every time. 
def get_connection():
    conn = psycopg2.connect( #connect is a function from psycopg2 that establishes a connection to the database. It takes several parameters that specify how to connect to the database.
        dbname="nasa_archive", #this is the name of the database we created in PostgreSQL
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),  #this is blank by default because it's not required for local PostgreSQL databases
        host="localhost",   #localhost means the database is running on our own computer. If we were connecting to a remote database hosted on a server, we would put the server's IP address or domain name here instead.
        port="5432" #always the default port that PostgreSQL listens on for incoming connections
    )
    return conn

#The whole thing is basically a reusable "open a door to the database" function. 
#Every other file will import and call this instead of rewriting those connection details repeatedly.


#The SQL database was ALREADY created from terminal before this database.py file was created. But it is on one side we don't see, while Python is on the other side. psycopg2.connect() is the handshake in the middle.
#In a sense, psycopg2 library is like a translator that allows Python to speak the language of SQL and understand the responses from the database. 
#psycopg2 abstracts away the complexities of SQL database communication and provides a simple interface for us to interact with our PostgreSQL database using Python code.
#It allows a 1-to-1 connection/translation between Python variables and SQL. Our Python code can now send SQL commands.

conn = get_connection()
print("Connected to database successfully")
conn.close()