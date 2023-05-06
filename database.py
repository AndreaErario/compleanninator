import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()


class database(object):
    def __init__(self):
        self.PATH = os.environ["DATABASE_PATH"]

    def connect(self):  # connects to the database
        try:
            self.conn = sqlite3.connect(self.PATH)
            return print("Database Connected")
        except:
            return print("Database not Connected")

    def create_table(
        self,
    ):  # creates a new Compleanninator table (used manually after a reset)
        self.connect()
        cur = self.conn.cursor()
        cur.execute(
            """
        CREATE TABLE Compleanninator
        (
        NAME TEXT NOT NULL,
        BIRTHDAY TEXT NOT NULL,
        CHAT_ID TEXT NOT NULL
        )
        """
        )
        self.conn.commit()
        self.conn.close()
        return print("Table created")

    def insert_data(self, name, birthday, chat_id):  # insert data into the table
        self.connect()
        cur = self.conn.cursor()
        cur.execute(
            f"INSERT INTO Compleanninator (NAME, BIRTHDAY, CHAT_ID) VALUES ('{name}', '{birthday}', '{chat_id}')"
        )
        self.conn.commit()
        self.conn.close()
        return print("Data Stored")

    def delete_data(self, name, chat_id):  # delete data into the table
        self.connect()
        cur = self.conn.cursor()
        cur.execute(
            f"DELETE FROM Compleanninator WHERE (NAME, CHAT_ID) = ('{name}', '{chat_id}')"
        )
        self.conn.commit()
        self.conn.close()
        return print("Data deleted")

    def extract_data(self):  # get all the data from the table
        self.connect()
        cur = self.conn.cursor()
        cur.execute("SELECT NAME, BIRTHDAY, CHAT_ID FROM Compleanninator")
        rows = cur.fetchall()
        self.conn.close()
        print(f"Data extracted: {rows}")
        return rows

    def get_list(self, chat_id):  # get the data stored from a user
        self.connect()
        cur = self.conn.cursor()
        cur.execute(f"SELECT NAME, BIRTHDAY FROM Compleanninator WHERE CHAT_ID = '{chat_id}'")
        list = cur.fetchall()
        self.conn.close()
        return list


db = database()
