import MySQLdb
import sys

def list_states():
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    
    db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=db_name, port=3306)
    cursor = db.cursor()
    
    cursor.execute("SELECT * FROM states ORDER BY id ASC;")

    for row in cursor.fetchall():
        print(row)
    
    cursor.close()
    db.close()

if __name__ == "__main__":
    list_states()
