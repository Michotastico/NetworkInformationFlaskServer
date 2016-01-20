import psycopg2

class Database():
    def __init__(self, user, password):
        self.db = psycopg2.connect(database='adkintun_web', user=user, password=password)

    def insert(self, value):
        cursor = self.db.cursor()
        value = value.replace("[", "{")
        value = value.replace("]", "}")
        value = value.replace("{", "-S-")
        value = value.replace("}", "-E-")

        value = value.replace(":", "---")
        value = value.replace("(", "-SS-")
        value = value.replace(")", "-EE-")
        value = value.replace(" ", "")
        #val = "INSERT INTO json_table (json_value) VALUES ("+value+")"
        #val = "INSERT INTO json_table (json_value) VALUES ("+str(value)+")"
        cursor.execute("INSERT INTO json_table (json_value) VALUES (%s)", value)

        self.db.commit()