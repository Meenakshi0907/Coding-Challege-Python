import mysql.connector

class DBConnUtil:
    def __init__(self, host="localhost", user="root", password="root", database="Loan"):
        self.conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
        self.cursor = self.conn.cursor()

    def execute_query(self, query, values=None):
        try:
            self.cursor.execute(query, values) if values else self.cursor.execute(query)
            self.conn.commit()
            print("Successful!!!")
        except mysql.connector.Error as e:
            print(f"Error executing query: {e}")

    def fetch_query(self, query, values=None):
        try:
            self.cursor.execute(query, values) if values else self.cursor.execute(query)
            result = self.cursor.fetchall()
            if result:
                print("Data retrieved successfully!")
            else:
                print("No records found.")
            return result
        except mysql.connector.Error as e:
            print(f"Error fetching data: {e}")
            return []

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
