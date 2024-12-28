"""
Expected Output
_______________________________
*************************
OS: Linux
Cpu Count: 4
Total Memory: 7799 MB
Current Load: 6
*************************

**********Mount Point Details**********
Device Name: /dev/loop36, Mount Point: /snap/wine-platform-runtime/392, FileSystem: squashfs
Device Name: /dev/loop8, Mount Point: /snap/firefox/5437, FileSystem: squashfs
Device Name: /dev/loop19, Mount Point: /snap/kubectl/3446, FileSystem: squashfs
Device Name: /dev/loop1, Mount Point: /snap/core18/2829, FileSystem: squashfs
Device Name: /dev/loop0, Mount Point: /snap/bare/5, FileSystem: squashfs
Device Name: /dev/loop38, Mount Point: /snap/wine-platform-runtime-core20/144, FileSystem: squashfs
Device Name: /dev/loop5, Mount Point: /snap/core22/1663, FileSystem: squashfs
Device Name: /dev/loop32, Mount Point: /snap/wine-platform-7-devel-core20/20, FileSystem: squashfs
Device Name: /dev/loop16, Mount Point: /snap/go/10748, FileSystem: squashfs
Device Name: /dev/loop40, Mount Point: /snap/wine-platform-runtime-core22/96, FileSystem: squashfs
Device Name: /dev/sda19, Mount Point: /, FileSystem: ext4
Device Name: /dev/loop28, Mount Point: /snap/snapd/23258, FileSystem: squashfs
Device Name: /dev/sda2, Mount Point: /boot/efi, FileSystem: vfat
Device Name: /dev/sda19, Mount Point: /var/snap/firefox/common/host-hunspell, FileSystem: ext4
Device Name: /dev/loop26, Mount Point: /snap/snap-store/1216, FileSystem: squashfs
Device Name: /dev/loop12, Mount Point: /snap/gnome-3-38-2004/143, FileSystem: squashfs
Device Name: /dev/loop10, Mount Point: /snap/gnome-3-28-1804/198, FileSystem: squashfs
Device Name: /dev/loop23, Mount Point: /snap/postman/206, FileSystem: squashfs
Device Name: /dev/loop11, Mount Point: /snap/gnome-3-38-2004/140, FileSystem: squashfs
Device Name: /dev/loop29, Mount Point: /snap/snapd-desktop-integration/178, FileSystem: squashfs
Device Name: /dev/loop31, Mount Point: /snap/wine-platform-6-stable/19, FileSystem: squashfs
Device Name: /dev/loop17, Mount Point: /snap/gtk-common-themes/1534, FileSystem: squashfs
Device Name: /dev/loop41, Mount Point: /snap/wine-platform-runtime-core22/97, FileSystem: squashfs
Device Name: /dev/loop7, Mount Point: /snap/firefox/4848, FileSystem: squashfs
Device Name: /dev/loop9, Mount Point: /snap/gnome-3-28-1804/161, FileSystem: squashfs
Device Name: /dev/loop14, Mount Point: /snap/gnome-42-2204/176, FileSystem: squashfs
Device Name: /dev/loop2, Mount Point: /snap/core20/2379, FileSystem: squashfs
Device Name: /dev/loop39, Mount Point: /snap/wine-platform-runtime-core20/149, FileSystem: squashfs
Device Name: /dev/loop18, Mount Point: /snap/gtk-common-themes/1535, FileSystem: squashfs
Device Name: /dev/loop24, Mount Point: /snap/postman/233, FileSystem: squashfs
Device Name: /dev/loop13, Mount Point: /snap/gnome-42-2204/141, FileSystem: squashfs
Device Name: /dev/loop3, Mount Point: /snap/core18/2846, FileSystem: squashfs
Device Name: /dev/loop37, Mount Point: /snap/wine-platform-runtime/397, FileSystem: squashfs
Device Name: /dev/loop21, Mount Point: /snap/notepad-plus-plus/411, FileSystem: squashfs
Device Name: /dev/loop35, Mount Point: /snap/wine-platform-9-devel-core22/33, FileSystem: squashfs
Device Name: /dev/loop27, Mount Point: /snap/snapd/21759, FileSystem: squashfs
Device Name: /dev/loop4, Mount Point: /snap/core20/2434, FileSystem: squashfs
Device Name: /dev/loop6, Mount Point: /snap/core22/1722, FileSystem: squashfs
Device Name: /dev/loop34, Mount Point: /snap/wine-platform-9-devel-core22/30, FileSystem: squashfs
Device Name: /dev/loop25, Mount Point: /snap/snap-store/1113, FileSystem: squashfs
Device Name: /dev/loop22, Mount Point: /snap/notepad-plus-plus/412, FileSystem: squashfs
Device Name: /dev/loop20, Mount Point: /snap/kubectl/3482, FileSystem: squashfs
Device Name: /dev/loop30, Mount Point: /snap/snapd-desktop-integration/253, FileSystem: squashfs
Device Name: /dev/loop33, Mount Point: /snap/wine-platform-7-devel-core20/24, FileSystem: squashfs
Device Name: /dev/loop15, Mount Point: /snap/go/10743, FileSystem: squashfs

*************************
Do you want to check disk percent usage of any mountpoint..: y
please enter the mount point e.g "/" ...: / /boot/efi
*************************
Details about : /
Total Size : 103467.73 MB, Percent used: 95.2
*************************
Details about : /boot/efi
Total Size : 256.0 MB, Percent used: 13.8
"""
#Author: Kunal Sharma
#Scrip to check system details (Mounts and asked mount point space)
import psutil
import os
import platform


class Mymachine():
    
    
        
        
    def sys_info(self):
        system_details=platform.system()
        print("*"*25)
        print(f'OS: {system_details}')
        print(f"Cpu Count: {os.cpu_count()}")
        print(f"Total Memory: {round(psutil.virtual_memory().total /1024/1024)} MB")
        cur_load,past_load_5min,past_10min=psutil.getloadavg()
        print(f"Current Load: {round(cur_load)}")
        print("*"*25)
        print()
        dev_tuple=()        
        dev_set=set({})        # To create uniqness
        for i in psutil.disk_partitions():
            
            dev_tuple=i[0],i[1],i[2]        #Asinging vaues to tuple
        
            dev_set.add(dev_tuple)
        print(f'{"*"*10}Mount Point Details{"*"*10}')
        for i in dev_set:
            print(f"Device Name: {i[0]}, Mount Point: {i[1]}, FileSystem: {i[2]}")    
        print()    
        print("*"*25)
        while True:
            check_input=input("Do you want to check disk percent usage of any mountpoint..: ")
            if check_input.isalpha() and check_input.lower()=='y' or check_input.isalpha() and check_input.lower()=='yes':
                mountpoint_ask=input('please enter the mount point e.g "/" ...: ')
                disk_mount_percent=mountpoint_ask.split()       #Converting string to list
                for i in disk_mount_percent:
                    print("*"*25)
                    print(f"Details about : {i}")
                    print(f"Total Size : {round(psutil.disk_usage(i).total/1024/1024,2)} MB, Percent used: {psutil.disk_usage(i).percent}")
                break    
            else:
                print('Thanks, Bye!!!')
                break
    
                
            
 
show_details=Mymachine()
show_details.sys_info()    
