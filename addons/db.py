import psycopg2
import os

class DbConnection():
    def __init__(self):
        try:
            # connect to the PostgreSQL server
            print('😨 Connecting to the PostgreSQL database...')
            self.conn =  psycopg2.connect( 
                host=os.getenv("db_host"),
                database=os.getenv("db_name"),
                user=os.getenv("db_user"),
                password=os.getenv("db_password"))
        except (Exception, psycopg2.DatabaseError) as error:
            print('😡 ', error)
        finally:
            if self.conn is not None:
                print('📖 PostgreSQL database connected ')
                self.cur = self.conn.cursor()

    def version(self):
        self.cur.execute('SELECT version()')
        db_version = self.cur.fetchone()
        print('💬 Version PostgreSQL database: ', db_version)

    def query(self, query):
        print('⏩ Database query : "',query,'"')
        try:
            self.cur.execute(query)
            print('✅ Succès !')
        except (Exception, psycopg2.DatabaseError) as error:
            print('😡 ', error)

    def close(self):
        self.cur.close()
        self.conn.close()
        print('📕 Database connection closed.')


def setup(client):
    db = DbConnection()
    db.query("SELECT * FROM progression;")
    db.close()