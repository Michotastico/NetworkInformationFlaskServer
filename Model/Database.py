import psycopg2

class Database():
    def __init__(self, user, password):
        self.db = psycopg2.connect(database='adkintun_web', user=user, password=password)

    def insert(self, value):
        cursor = self.db.cursor()

        cursor.execute("INSERT INTO json_table (json_value) VALUES (%s)", value)

        self.db.commit()