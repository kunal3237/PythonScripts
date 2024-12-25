"""
Expected Output
________________________________________
***** Checking the landing directory *****
***** Changing current directory to /home/kunal *****
***** Good to go for the backup, Backup Drectory aleady exists *****
***** Listing the backupfolder---> /home/kunal *****
total 16
-rw-rw-r-- 1 kunal kunal 310 Dec 24 14:53 Try-py-2024-12-24-14-53-4.zip
-rw-rw-r-- 1 kunal kunal 312 Dec 24 14:53 Try-py-2024-12-24-14-53-15.zip
-rw-rw-r-- 1 kunal kunal 109 Dec 25 20:51 Try-py-2024-12-25-20-51-51
-rw-rw-r-- 1 kunal kunal 312 Dec 25 20:51 Try-py-2024-12-25-20-51-51.zip

Zipping file /home/kunal/backupwithpython/Try-py-2024-12-25-20-52-3 to /home/kunal/backupwithpython/Try-py-2024-12-25-20-52-3.zip
***** Zip Process is complete *****
Do you want to delete unzipped files...y
entering the loop
Deteing...,Try-py-2024-12-25-20-52-3
Deteing...,Try-py-2024-12-25-20-51-51

"""

import os
import os.path
import subprocess
import shutil
import datetime
import zipfile
import time

time_with_file=datetime.date.today()
hour_to_add=datetime.datetime.today().hour
min_to_add=datetime.datetime.today().minute
sec_to_add=datetime.datetime.today().second

print('*'*5,'Checking the landing directory','*'*5)

def check_directory():
    if os.path.abspath(os.curdir)=='/home/kunal':
        print('*'*5,'You are in the correct directory','*'*5)
    else:
        print('*'*5,'Changing current directory to /home/kunal','*'*5)
        change_dirctory=os.chdir('/home/kunal')
    
backup_folder=os.path.join('/home/kunal','backupwithpython')

def check_backupdir():
    if os.path.exists('./backupwithpython'):
        print('*'*5,'Good to go for the backup, Backup Drectory aleady exists','*'*5)
        command=['ls','-ltr', './backupwithpython']
        dir_content=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
        out,err=dir_content.communicate()
        print('*'*5,f'Listing the backupfolder--->',os.path.abspath(os.curdir),'*'*5)
        print(out)
        backup_folder=os.path.join(os.getcwd(),'backupwithpython')
        new_name=backup_folder+'/'+'Try-py-'+str(time_with_file)+'-' +str(hour_to_add)+'-'+str(min_to_add)+'-' +str(sec_to_add)
        shutil.copy('Try.py',new_name)
        zip_filename=new_name+'.zip'
        print(f"Zipping file {new_name} to {zip_filename}")
        with zipfile.ZipFile(zip_filename,'w',compression=zipfile.ZIP_BZIP2) as myzip:
            myzip.write(new_name)
            print('*'*5,'Zip Process is complete','*'*5)
        

        
    else:
        os.mkdir('./backupwithpython')
        print('Created New directory for the backup')
        print('Running the backup Process')
        backup_folder=os.path.join(os.getcwd(),'backupwithpython')
        new_name=backup_folder+'/'+'Try-py-'+str(time_with_file)+'-' +str(hour_to_add)+'-'+str(min_to_add)+'-' +str(sec_to_add)
        shutil.copy('Try.py',new_name)
        print('*'*5,'Zipping file to save space','*'*5)
        zip_filename=new_name+'.zip'
        with zipfile.ZipFile(zip_filename,'w',compression=zipfile.ZIP_BZIP2) as myzip:
            myzip.write(new_name)
            print('*'*5,'Showing info about zipped file','*'*5)
            
 
check_directory() 
check_backupdir()    
collect_input=input('Do you want to delete unzipped files...')   

while True:
     
     if collect_input.isalpha() and collect_input.lower()=='y' or collect_input.isalpha() and collect_input.lower()=='yes':
        print('entering the loop') 
        os.chdir(backup_folder)
        for file_name in os.listdir(backup_folder):
            
            if  not file_name.endswith("zip"):
                
                print(f'Deteing...,{file_name}')     
                subprocess.Popen(['rm',' -rf',file_name], stderr=subprocess.PIPE,stdout=subprocess.PIPE,text=True)
                time.sleep(3)
        
        
        
        break    
                
     else:
         print('Good Bye, Thanks for using the Script')
         break               
# command=['ls','-ltr', 'backupwithpython']
# subprocess.run(command,capture_output=True,text=True)






    
