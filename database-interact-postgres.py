"""
Expected Output
__________________________

Welcome, We are working on test_erp database
1 Lion
2 Tiger
3 Wolf
4 Fox
5 Tiger
********** Tablespace Names if the database **********
pg_default
pg_global

"""

import psycopg2
import os
import psycopg2.extras          #To get the column name and data as dictionary
class PostgresCheck:
                    def __init__(self):
                        print(f"Welcome, We are working on {os.getenv('pg_db')} database")
                        
                    def postgres_select(self):
                                    with psycopg2.connect(database=os.getenv('pg_db'),user=os.getenv('pg_user'),password=os.getenv('pg_psd'),host='localhost',cursor_factory=psycopg2.extras.DictCursor) as connection:
                                        with connection.cursor() as mycon_cur:
                                            select_query="select * from zoo_1"
                                            mycon_cur.execute(select_query)
                                            result=mycon_cur.fetchone()
                                            while result:
                                                print(result['id'],result['animal'])
                                                result=mycon_cur.fetchone()
                                    
                    def postgres_insert(self):
                                    with psycopg2.connect(host="localhost",database=os.getenv("pg_db"),user=os.getenv('pg_user'),password=os.getenv('pg_psd')) as connection:
                                        with connection.cursor() as mycon_cur:
                                            insert_query=" insert into zoo_1 values ((%s), %s)"
                                            insert_variable=(5,'Tiger')        
                                            mycon_cur.execute(insert_query,insert_variable) 
                                            connection.commit()
                                            
                    def postgres_delete(self):
                                    with psycopg2.connect(host='localhost',user=os.getenv('pg_user'),database=os.getenv('pg_db'),password=os.getenv('pg_psd')) as connection:
                                        with connection.cursor() as mycon_cur:
                                            delete_query="delete from zoo_1 where id=%s"
                                            delete_var=(5,)
                                            mycon_cur.execute(delete_query,delete_var)
                                            connection.commit()
                                            
                    def postgres_tablespace(self):
                        with psycopg2.connect(database=os.getenv('pg_db'),user=os.getenv('pg_user'),password=os.getenv('pg_psd'),host='localhost',cursor_factory=psycopg2.extras.DictCursor) as connection:
                            with connection.cursor() as mycon_cur:
                                tablespace_query="select * from pg_tablespace"
                                mycon_cur.execute(tablespace_query)
                                result=mycon_cur.fetchone()                        
                                print(f"{'*'*10} Tablespace Names if the database {'*'*10}")
                                while result:
                                    print(result['spcname'])
                                    result=mycon_cur.fetchone()

postgres_inst=PostgresCheck()
postgres_inst.postgres_delete()
postgres_inst.postgres_insert()
postgres_inst.postgres_select()
postgres_inst.postgres_tablespace()
