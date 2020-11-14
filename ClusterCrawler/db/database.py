import sqlite3
from sqlite3 import Error


class Database:
    def __init__(self, db_filepath):
        self.db_filepath = db_filepath
        self.conn = None
        self.cursor = None

        self.open_connection()

    def open_connection(self):
        try:
            self.conn = sqlite3.connect(self.db_filepath)
            self.cursor = self.conn.cursor()
            print("Database connected successfully and cursor created.")

        except Error as e:
            print(f'connect error: {e}')

    def close_connection(self):
        try:
            if self.conn:
                self.conn.close()
                print("Database closed.")
            else:
                print("Database could not close because it is not open.")

        except Exception as e:
            print(f'close error: {e}')
