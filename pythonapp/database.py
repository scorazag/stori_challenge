import mysql.connector
import csv
from datetime import datetime

def insert_transacctions_from_csv():
    try:
        connection = mysql.connector.connect(host='mysql',
                                             port='3306',
                                             database='Stori',
                                             user='root',
                                             password='root')
        cursor = connection.cursor()

        with open('txns.csv',mode ='r') as file:
            next(file)
            txns = csv.reader(file)
            for txn in txns:
                mySql_insert_query = """INSERT INTO transactions (id, fecha, amount) 
                                        VALUES (%s, %s, %s) """
                

                fecha = txn[1] + '/24'
                fecha_f = datetime.strptime(fecha, '%m/%d/%y').date()
                formatted_date = fecha_f.strftime('%Y-%m-%d')

                record = (txn[0], formatted_date, txn[2])
                cursor.execute(mySql_insert_query, record)
                connection.commit()
                print("Record inserted successfully into Transactions table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def insert_varibles_into_summary(credit, debit, balance, month_resume):
    try:
        connection = mysql.connector.connect(host='mysql',
                                             port='3306',
                                             database='Stori',
                                             user='root',
                                             password='root')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO summary (credit, debit, balance, month_resume) 
                                VALUES (%s, %s, %s, %s) """

        record = (credit, debit, balance, month_resume)
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print("Record inserted successfully into Summary table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

