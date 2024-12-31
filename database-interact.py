"""
Expected Output
____________________________
Enter the password..: 
Enter the db_name..: 
('John', 'Highway 21')
"""

#Author: Kunal Sharma
#To interact with databases 
import mysql.connector
import os
import getpass

def database_play():
            psd=getpass.getpass(prompt="Enter the password..: ")
            db_name=getpass.getpass(prompt="Enter the db_name..: ")
            my_con=mysql.connector.connect(host='localhost',user='oscar',password=psd,database=db_name)
            mycon_cur=my_con.cursor()
            #mycon_cur.execute("select * from customers")
            insert_query="INSERT INTO customers (name, address) VALUES( %s, %s)"
            data_to_insert=( 'Kunal','Palampur')
            mycon_cur.execute(insert_query,data_to_insert)
            my_con.commit()
            select_query="select * from customers where name= %s"
            select_var=["John"]
            mycon_cur.execute(select_query,select_var)
            myresult=mycon_cur.fetchone()
            while myresult:
                print(myresult)
                myresult=mycon_cur.fetchone()
            #print(help(my_con.cursor()))
            # print(dir(mysql.connector))
            
database_play()            
