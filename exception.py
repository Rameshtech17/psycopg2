
import psycopg2

conn = None
try:
    conn = psycopg2.connect(database="postgres", user="postgres", password="test123", host="127.0.0.1", port="5432")
    cur = conn.cursor()
    # execute 1st statement
    cur.execute("SET search_path to psycopg")
    # execute 2nd statement
    cur.execute("SELECT * FROM test_1 ORDER BY id")
    # commit the transaction
    conn.commit()
    # close the database communication
    cur.close()
except psycopg2.DatabaseError as error:
    print(error)
finally:
    if conn is not None:
        conn.close()

