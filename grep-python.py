
"""
Script to search for partiular word in specified file 

OutPut
****************************************************************************************************
Please enter the name of the directory, where logs are present.... : /var/log/postgresql
****************************************************************************************************
Checking if there is any log file with log extension
****************************************************************************************************
/var/log/postgresql/postgresql-14-main.log
/var/log/postgresql/postgresql-17-main.log

****************************************************************************************************
Please enter the file name to check for the error,Choose from above list..: /var/log/postgresql/postgresql-14-main.log
********** Searching 'database system was shut down in below file' **********

/var/log/postgresql/postgresql-14-main.log
19) 2024-12-16 09:28:03.107 IST [1480] LOG:  database system was shut down at 2024-12-15 20:05:59 IST
29) 2024-12-17 09:18:45.367 IST [1492] LOG:  database system was shut down at 2024-12-16 19:36:02 IST
39) 2024-12-18 10:19:16.702 IST [1487] LOG:  database system was shut down at 2024-12-17 19:18:37 IST
49) 2024-12-18 11:35:53.370 IST [164231] LOG:  database system was shut down at 2024-12-18 11:35:41 IST
59) 2024-12-19 10:28:06.626 IST [1477] LOG:  database system was shut down at 2024-12-18 19:56:07 IST
69) 2024-12-20 09:18:51.813 IST [1489] LOG:  database system was shut down at 2024-12-19 20:03:33 IST
89) 2024-12-23 09:42:11.619 IST [1518] LOG:  database system was shut down at 2024-12-21 21:28:46 IST
99) 2024-12-24 09:07:43.663 IST [1489] LOG:  database system was shut down at 2024-12-23 20:55:39 IST
109) 2024-12-25 09:42:08.155 IST [1524] LOG:  database system was shut down at 2024-12-24 20:42:46 IST
"""        


import os.path 
import subprocess
import sys
print("*"*100)
dir_ask_check=input("Please enter the name of the directory, where logs are present.... : ")
def dir_ask():
    dir_ask_check_split=dir_ask_check.split()
    for i in dir_ask_check_split:
        if os.path.exists(i):
            os.chdir(i)
            dir_ask_files=os.getcwd()
            return dir_ask_files
        else:
            pass
    
dir_ask=dir_ask()  
print("*"*100)
def grep_python():
    if dir_ask==None:
        sys.exit('No such Directory, Thanks!!')
    else:
        print(F"Checking if there is any log file with log extension")
        print("*"*100)
        dir_check=os.listdir()
        if len(dir_check)!=0:
            for i in dir_check:
                if i.endswith("log"):
                    
                    log_file_name=os.path.join(os.path.abspath(os.curdir),i)
                    print(log_file_name)
            print() 
            print("*"*100)   
            file_name_input=input("Please enter the file name to check for the error,Choose from above list..: ")
            for i in file_name_input.split():
                command=['ls', '-ltr',file_name_input]
                process_check=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True) 
                out,err= process_check.communicate()
                #print(process_check.returncode)    
                if  process_check.returncode!=0:
                    print("File does not exist, Please check the name ...")
                else:
                    print('*'*10,f"Searching 'database system was shut down in below file'",'*'*10)  
                    print()  
                    print(i)       
                    with open(i) as f:
                        line_count=1
                        for i in f.readlines():
                            if 'database system was shut down' in i or 'error' in i:
                                print(f"{line_count}) {i}",end='')
                                line_count+=1
                            else:
                                line_count+=1
        else:
            print("No file with log exention")        

   
grep_python()
