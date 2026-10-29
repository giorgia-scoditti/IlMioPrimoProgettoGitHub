"""
LEZIONE DEL 29/10/2026 - WEEK 06
"""
import mysql.connector

def main():
    cnx = mysql.connector.connect(option_files="db.cnf")
    query = """
            SELECT * FROM trip
            ORDER BY duration_seconds
            LIMIT 10
            """

    cursor = cnx.cursor()
    cursor.execute(query)

    for trip in cursor:
        print(trip)
main()