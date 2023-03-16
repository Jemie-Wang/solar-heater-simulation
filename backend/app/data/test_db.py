import sqlite3
DBNAME = 'database/cityinfo.db'
def testdb():
    connection = sqlite3.connect(DBNAME)
    cursor = connection.cursor()
    sql_query = """SELECT name FROM sqlite_master
        WHERE type='table';"""
    cursor.execute(sql_query)
    print(cursor.fetchall())
    cursor.execute('SELECT COUNT(*) FROM cityinfo')
    print(cursor.fetchall())

if __name__ == '__main__':
    testdb()