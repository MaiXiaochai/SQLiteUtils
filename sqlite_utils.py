"""
------------------------------------------
@File       : sqlite_utils.py
@CreatedOn  : 2023/9/27 10:34
------------------------------------------
"""
import sqlite3


class SQLiteUtils:

    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()

    def execute(self, sql):
        self.cur.execute(sql)
        self.conn.commit()

    def executemany(self, sql, args=None):
        self.cur.executemany(sql, args)
        self.conn.commit()

    def fetchone(self, sql):
        self.execute(sql)
        return self.cur.fetchone()

    def close(self):
        self.cur.close()
        self.conn.close()

    def __del__(self):
        self.close()
