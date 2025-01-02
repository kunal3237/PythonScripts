"""
Expected Output
____________________________
Welcome to Mysql kunal database 
('mysql', '2.64Mb', '-137.36Mb', '140.00Mb', Decimal('-5201.78'))
('sys', '0.02Mb', '0.02Mb', '0.00Mb', Decimal('100.00'))
('kunal', '0.02Mb', '0.02Mb', '0.00Mb', Decimal('100.00'))
('information_schema', '0.00Mb', '0.00Mb', '0.00Mb', Decimal('0.00'))
('performance_schema', '0.00Mb', '0.00Mb', '0.00Mb', Decimal('0.00'))
"""
#Author: Kunal Sharma
#To interact with databases 
import mysql.connector
import os
import getpass

class DatabaseCheck:

            def __init__(self):
                print(f"Welcome to Mysql {os.getenv('db_name')} database ")
            
            def select(self):

                        with mysql.connector.connect(host='localhost',user=os.getenv('dbuser'),password=os.getenv('psd'),database=os.getenv('db_name')) as connection:
                            with connection.cursor() as mycon_cur:
                                insert_query="INSERT INTO customers (name, address) VALUES( %s, %s)"
                                select_query="select * from customers" # where name= %s"
                                mycon_cur.execute(select_query) #select_var
                                myresult=mycon_cur.fetchone()
                                while myresult:
                                    print(myresult)
                                    myresult=mycon_cur.fetchone()
                                connection.commit()
                                
            def insert(self):
                        with mysql.connector.connect(host='localhost',user=os.getenv('dbuser'),database=os.getenv('db_name'),password=os.getenv('psd')) as connection:
                            with connection.cursor() as mycon_cur:
                                insert_query="insert into customers(name,address)  values(%s,%s)"
                                insert_var=('Iphone','America')
                                mycon_cur.execute(insert_query,insert_var)
                                connection.commit()
                                print("Data Added")
                        connection.commit()    
                            
            def delete(self):
                        with mysql.connector.connect(host="localhost",user=os.getenv('dbuser'),password=os.getenv('psd'),database=os.getenv('db_name')) as connection:
                            with connection.cursor() as mycon_cur:
                                delete_query="delete from customers where name=%s"
                                delete_var=["Kunal"]
                                mycon_cur.execute(delete_query,delete_var)
                                connection.commit()
                                print("Data Deleted..")  
                            connection.commit()                  
                    
            def database_usage(self):
                        with mysql.connector.connect(host="localhost",user=os.getenv('dbuser'),password=os.getenv('psd'),database=os.getenv('db_name')) as connection:
                            with connection.cursor() as mycon_cur:
                                database_query="""SELECT s.schema_name,
                                CONCAT(IFNULL(ROUND((SUM(t.data_length)+SUM(t.index_length))/1024/1024,2),0.00),"Mb") total_size,
                                CONCAT(IFNULL(ROUND(((SUM(t.data_length)+SUM(t.index_length))-SUM(t.data_free))/1024/1024,2),0.00),"Mb") data_used,
                                CONCAT(IFNULL(ROUND(SUM(data_free)/1024/1024,2),0.00),"Mb") data_free,
                                IFNULL(ROUND((((SUM(t.data_length)+SUM(t.index_length))-SUM(t.data_free))/((SUM(t.data_length)+SUM(t.index_length)))*100),2),0) pct_used
                                FROM INFORMATION_SCHEMA.SCHEMATA s, INFORMATION_SCHEMA.TABLES t
                                WHERE s.schema_name = t.table_schema
                                GROUP BY s.schema_name
                                ORDER BY total_size DESC"""
                                mycon_cur.execute(database_query)
                                result=mycon_cur.fetchone()
                                while result:
                                    print(result)
                                    result= mycon_cur.fetchone()               
                        

database_check=DatabaseCheck()
# database_check.delete()
# database_check.insert()
# database_check.select()
database_check.database_usage()

