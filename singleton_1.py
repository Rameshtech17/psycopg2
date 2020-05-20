import psycopg2


class DBconnect():
    __instance = None

    def __new__(cls, database, user, password, host, port):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        cls.__instance.database = database
        cls.__instance.user = user
        cls.__instance.password = password
        cls.__instance.host = host
        cls.__instance.port = port
        return cls.__instance

    def __call__(cls, *args, **kwargs):
        try:
            con = psycopg2.connect(database=cls.__instance.database, user=cls.__instance.user,
                                   password=cls.__instance.password, host=cls.__instance.host,
                                   port=cls.__instance.port)

            print("DataBase connected  success")
            cur = con.cursor()
            cur.execute("SET search_path to Psycopg")
        except psycopg2.DatabaseError as error:
            print(error)
        finally:
            return cur

class DBclose():
    __instance=None
    def __new__(cls, database, user, password, host, port):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        cls.__instance.database = database
        cls.__instance.user = user
        cls.__instance.password = password
        cls.__instance.host = host
        cls.__instance.port = port
        return cls.__instance


conn = DBconnect("postgres", "postgres", "test123", "127.0.0.1", "5432")
conn1 = DBconnect("postgres", "postgres", "test123", "127.0.0.1", "5432")

curr = conn()
curr1 = conn1()

# CTE
# curr.execute("WITH testCTE(id,title,old) AS(SELECT id,name,city FROM test_1) SELECT * FROM testCTE;")
# curr.close()
# curr1.execute("WITH testCTE(id,title,old) AS(SELECT id,name,city FROM test_1) SELECT * FROM testCTE;")

# Normal Select Query
curr.execute("SELECT * FROM test_1 ORDER BY id")
curr1.execute("SELECT * FROM test_1 ORDER BY id")

res = curr.fetchall()
# con.commit()
for i in res:
    print(i)

curr.close()

print("###################################################")
res1 = curr1.fetchall()
# con.commit()
for i in res1:
    print(i)
