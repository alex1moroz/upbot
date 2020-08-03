import psycopg2


class Database:

    def cur(self, task):
        connect = psycopg2.connect(
            database="df0b31na5sq5g1",
            user="zdbkddrjcbayyh",
            password="41423ae124efcd6d5ecfb904a1bbab37980bcb18781e83736c5fb93f73da7f61",
            host="ec2-34-192-173-173.compute-1.amazonaws.com",
            port="5432"
        )
        cur = connect.cursor()


        return cur

        cur.execute(task)
        connect.commit


    li = "SELECT sitename FROM site"

    def count(self):
        db = Database.cur((), task=Database.li)
        fe = db.rowcount
        return fe

    def all(self):
        db = Database.cur((), task=Database.li)
        db.fetchall()
        db.close()


    def add(self, value):
        sql = f"INSERT INTO site(sitename) VALUES('{value}');"
        db = Database.cur((), task=sql)


add = 'https://t.fits.agency/'
# Database.add((), value=add)

print(Database.count(()))