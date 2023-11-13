"""
------------------------------------------
@File       : sqlite_utils.py
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

    def fetchall(self, sql):
        self.execute(sql)

        return self.cur.fetchall()

    def exist_table(self, table_name):
        """检查表是否存在"""
        sql = f"SELECT count(*) FROM sqlite_master WHERE name='{table_name}'"
        return self.fetchone(sql)[0] == 1

    def close(self):
        self.cur.close()
        self.conn.close()

    def __del__(self):
        self.close()
