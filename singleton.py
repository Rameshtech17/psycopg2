import psycopg2
class connect():
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
        con = psycopg2.connect(database=cls.__instance.database, user=cls.__instance.user,
                               password=cls.__instance.password, host=cls.__instance.host, port=cls.__instance.port)

        print("DataBase connected  success")
        cur = con.cursor()
        cur.execute("SET search_path to Psycopg")
        return cur


conn = connect("postgres", "postgres", "test123", "127.0.0.1", "5432")

curr = conn()

curr.execute("SELECT * FROM test_1 ORDER BY id")

res = curr.fetchall()
# con.commit()
for i in res:
    print(i)
