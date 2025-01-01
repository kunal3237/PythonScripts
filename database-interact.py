"""
Expected Output
____________________________
Data Deleted..
Data Added
('John', 'Highway 21')
('Peter', 'Lowstreet 4')
('Iphone', 'America')
('Iphone', 'America')
('Iphone', 'America')
"""

#Author: Kunal Sharma
#To interact with databases 
import mysql.connector
import os
import getpass

def select():

            with mysql.connector.connect(host='localhost',user=os.getenv('dbuser'),password=os.getenv('psd'),database=os.getenv('db_name')) as connection:
                mycon_cur=connection.cursor()
                insert_query="INSERT INTO customers (name, address) VALUES( %s, %s)"
                select_query="select * from customers" # where name= %s"
                mycon_cur.execute(select_query) #select_var
                myresult=mycon_cur.fetchone()
                while myresult:
                    print(myresult)
                    myresult=mycon_cur.fetchone()
                    
def insert():
            with mysql.connector.connect(host='localhost',user=os.getenv('dbuser'),database=os.getenv('db_name'),password=os.getenv('psd')) as connection:
                mycon_cur=connection.cursor()
                insert_query="insert into customers(name,address)  values(%s,%s)"
                insert_var=('Iphone','America')
                mycon_cur.execute(insert_query,insert_var)
                connection.commit()
                print("Data Added")
                
def delete():
            with mysql.connector.connect(host="localhost",user=os.getenv('dbuser'),password=os.getenv('psd'),database=os.getenv('db_name')) as connection:
                mycon_cur=connection.cursor()
                delete_query="delete from customers where name=%s"
                delete_var=["Kunal"]
                mycon_cur.execute(delete_query,delete_var)
                connection.commit()
                print("Data Deleted..")                
                        
delete()
insert()            
select()            
