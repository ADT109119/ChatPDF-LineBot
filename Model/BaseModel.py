import os
import shutil
class BaseModel:
    def __init__(self):
        self.filed = []
        self.con = self.get_db_connection()
        self.table = ""

    def get_db_connection(self):
        import sqlite3
        if os.path.exists('./db/database.db'):
            return sqlite3.connect('./db/database.db')
        else:
            shutil.copy('./config/database_backup.db', './db/database.db')
            return sqlite3.connect('./db/database.db')
        
    def sql_query(self, query, parameters=None, get_lastrow_id = False):
        cursor = self.con.cursor()
        cursor.execute(query, parameters)
        self.con.commit()
        if get_lastrow_id:
            return cursor.lastrowid
        return cursor.fetchall()
    
    def sql_query_many(self, query, parameters=None):
        cursor = self.con.cursor()
        cursor.executemany(query, parameters)
        self.con.commit()
        return cursor.fetchall()


    def saveData(self, data):
        cursor = self.con.cursor()
        columns = ', '.join(self.filed)
        values = ', '.join(['?'] * len(self.filed))
        query = f"INSERT INTO {self.table} ({columns}) VALUES ({values})"
        cursor.execute(query, data)
        self.con.commit()

    def getData(self, conditions=None, limit=None, order=None):
        cursor = self.con.cursor()
        query = f"SELECT * FROM {self.table}"
        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        if limit:
            query += " LIMIT " + limit

        if order:
            query += " ORDER BY " + order

        cursor.execute(query)
        return cursor.fetchall()
