import psycopg2


class PostgresConnection(object):

    def __init__(self):
        pass

    def _create_connection(self):
        try:
            conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='password'")
            cur = conn.cursor()
            conn.autocommit = True
            return cur
        except:
            print 'I am unable to connect to the database'

    def get_login_data(self):
        cur = self._create_connection()
        cur.execute("""SELECT * from userlogin""")
        rows = cur.fetchall()
        return rows

    def insert_user(self, first_name=None, last_name=None, user_name=None, password=None):
        cur = self._create_connection()
        try:
            query = """INSERT INTO userlogin(username, firstname, lastname, password) VALUES('%s', '%s', '%s', '%s')"""%(user_name, first_name, last_name, password)
            cur.execute(query)
        except:
            print 'I failed to add values to the database'

    def check_user_login(self, user_name, password):
        cur = self._create_connection()
        try:
            query = """select count(*) from userlogin where username='%s' and password='%s'""" % (user_name, password)
            cur.execute(query)
            result = cur.fetchone()
            return result[0] if result else 0

        except:
            print 'I failed in the database call'