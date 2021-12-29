import mysql.connector
from mysql.connector import Error

def write_file(data, filename):

    with open(filename, 'wb') as file:
        file.write(data)

def readBLOB(booking_id, photo, bioData):
    print("Reading BLOB data from LBRS database")

    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='ums_lbrs'',
                                             user='root',
                                             password='akar')

        cursor = connection.cursor()
        sql_fetch_blob_query = """SELECT * from booking where id = %s"""

        cursor.execute(sql_fetch_blob_query, (emp_id,))
        record = cursor.fetchall()
        for row in record:
            print("ID = ", row[0], )
            print("Room = ", row[1])
            image = row[2]
            file = row[3]
            write_file(image, photo)
            write_file(file, bioData)

    except mysql.connector.Error as error:
        print("Failed to read BLOB data from MySQL table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
