import psycopg2

con = psycopg2.connect(database="postgres", user="postgres", password="test123", host="127.0.0.1", port="5432")

print("Database opened successfully")

cur = con.cursor()
cur.execute("SET search_path to Psycopg")
# cur.execute("CREATE TABLE Test_1(id int primary key , name varchar(50),address varchar(100),city varchar(50))")

# cur.execute("INSERT INTO test_1(id ,name ,address,city) VALUES (1,'kavi','salem','salem')")
cur.execute("SELECT * FROM test_1 ORDER BY id")
# cur.execute("SELECT * FROM test_1 WHERE age>25")
# cur.execute("SELECT * FROM test_1 ")

res = cur.fetchall()
# con.commit()
for i in res:
    print(i)
