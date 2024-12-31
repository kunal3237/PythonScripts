"""
list.txt
__________________
/U01/SYSTEM/system01.dbf 24000
/U01/SYSTEM/system02.dbf 28000
/U01/SYSTEM/system03.dbf 25000
/U01/SYSTEM/system04.dbf 23000
/U01/SYSTEM/system05.dbf 27000
/U01/SYSTEM/system06.dbf 29000
/U01/SYSTEM/system06.dbf 27000
/U01/SYSTEM/system098.dbf 27000
/U01/SYSTEM/system-99.dbf 27000
/U01/SYSTEM/system95t.dbf 27000
/U01/SYSTEM/system089.dbf 27000

______________________________
mount.txt
___________________________
/boot/efi
/

Output So far:
/ 4474.5078125
Adding new file
/U01/SYSTEM/system100.dbf

"""

#Author: Kunal Sharma
# To automate the file addition in te tablespace based on the space available on the mount points----Working
import os.path
import psutil

class TablespaceCheck:

                    def directory_name(self):
                            dirname_set=set({})
                            file_name=set({})
                            with open('list.txt','r') as file:
                                    for i in file.readlines():
                                        if not i.isspace():
                                            inner_lst=i.rstrip('\n').split()
                                            dirname_set.add(os.path.dirname(inner_lst[0]))
                                            file_name.add(os.path.basename(inner_lst[0].removesuffix('.dbf')))
                            new_var_check=[]             
                            for i in file_name:
                                file_num_check=[]
                                file_num_check_new=[]
                                capture_name=[]
                                for j in i:
                                    if not j.isalpha():
                                       file_num_check.append(j)
                                    else:
                                       capture_name.append(j)
                                capture_name="".join(capture_name)

                                if file_num_check[0]=='0' or file_num_check[0]=='-' or file_num_check[0]=='_':
                                    del(file_num_check[0])
                                    file_num_check="".join(file_num_check)
                                    new_var_check.append(int(file_num_check))
                                else:
                                    file_num_check="".join(file_num_check)
                                    new_var_check.append(int(file_num_check))
  
                            new_file_max=max(new_var_check)

                            for i in dirname_set:
                                print(f"{i}/{capture_name}{new_file_max+1}.dbf")                
                                    
                    def os_space_check(self):

                            mount_point=set({})
                            mount_fs=()
                            for i in psutil.disk_partitions():
                                mount_fs=i[0],i[1],i[2],i[3]
                                rw_mount_check=mount_fs[3].split(',')

                                for j,k in enumerate(rw_mount_check):
                                    if j==0 and k=='rw':
                                        final_mount_fs=i[0],i[1],i[2],k
                                    
                                        with open('mount.txt','r') as f:
                                            for line in f.readlines():
                                                fs_to_check=line.rstrip('\n')

                                                if mount_fs[1]==fs_to_check:
                                                    
                                                    if psutil.disk_usage(fs_to_check).free/1024/1024>=4000:
                                                        print(fs_to_check ,psutil.disk_usage(fs_to_check).free/1024/1024)
                                                        with open('list.txt','r') as file:

                                                            line_count=0
                                                            space_above_25=0
                                                            for innerline in file.readlines():
                                                                if not innerline.isspace(): 
                                                                    line_count+=1 
                                                                    space_to_check=innerline.rstrip().split()
                                                                    
                                                                    
                                                                    if int(space_to_check[1])>=23000:
                                                                        space_above_25+=1

                                                        
                                                        if space_above_25 == line_count:
                                                            
                                                            if psutil.disk_usage(fs_to_check).free/1024/1024>3000:
                                                                print("Adding new file")
                                                                
                                                                
                                                            else:
                                                                print("Not suffient space in fs_to_check ")    
                                                        else:
                                                            print('Still files have sufficient space to accomodate the data')    
                                                            

                                                    else:
                                                        pass    
                                    else:
                                        pass

first_check=TablespaceCheck() 
first_check.os_space_check()
first_check.directory_name()                       
