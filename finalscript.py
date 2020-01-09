import RPi.GPIO as GPIO
import sqlite3
from datetime import datetime
counter=0


def sql_connection():
    try:
        con = sqlite3.connect('more.db')
        return con
    except Error:
        print(Error)
def sql_table(con):
        x = con.cursor()
        x.execute("CREATE TABLE IF NOT EXISTS akash1(id PRIMARY KEY AUTOINCREMENT ,COUNTER INTEGER, DATE)")
        con.commit()
        print("X")
def sql_insert(con, timestamp,counter):
        x = con.cursor()
        x.execute('''INSERT INTO akash1(COUNTER,DATE) values(?,?)''',(counter,timestamp,))
        con.commit()
def button_callback(channel):
        global counter
        con=sql_connection()
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        counter=counter+1
        sql_insert(con,timestamp,counter)
        print("data saved To Database")
        con.close()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.OUT)
con=sql_connection()
sql_table(con)
con.close()

GPIO.add_event_detect(23,GPIO.RISING,callback=button_callback)
print("press the button to store data")
message = input("Press enter to quit\n")
GPIO.cleanup()
