#-*- coding:utf-8 -*-


import csv
import os
import time
import re

ip=['10.1.55']
Dir = 'C:\\Users\\USER\\Desktop\\PORTSCAN\\'
def dir_parsing():
    Dir_names = os.listdir(Dir)
    #print(Dir_names)
    with open('Result.csv','wb') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(['IP Address', 'Host' , 'OS', 'TCP Ports', 'C_Class','Confirm','Port_Service'])
        for Dir_name in Dir_names:
            full_name_0 = Dir + Dir_name + '\\'
            file_names = os.listdir(full_name_0)
            compare = '/tcp'
            state = 'open'
            
            print(Dir_name)
            for file_name in file_names:
                full_name = full_name_0 + file_name
                print(full_name)
                #full_name_dir=os.listdir(full_name)
                #print(full_name_dir[0])
                result_1 = 'Read data files from: C:\Program Files (x86)\Nmap'
                confirm_os_1 ='OSs:'
                confirm_os_2 ='OS details:'
                confirm_os_3 ='OS:'
                confirm_Host ='Host:'
                OS = ''
                HOST = ''
                
                with open(full_name,'r') as nmap_scan:
                    confirm_test = 'reset'
                    ip_Clear = full_name.split('_')
                    #print(ip_Clear[1])
                    ip_Clear2 = ip_Clear[1].split('.')
                    ip_result = ip_Clear2[0] +'.' + ip_Clear2[1] +'.' + ip_Clear2[2] +'.' + ip_Clear2[3]
                    ip_C_class = ip_Clear2[0] +'.' + ip_Clear2[1] +'.' + ip_Clear2[2] + '.0/24'
                    #print(ip_result)
                    port_list=''    
                    serviceInfo = ''
                    
                    while True:
                        line = nmap_scan.readline()
                        if not line : 
                            break
                        if compare in line and state in line:
                            port = line.split('/')
                            #print(port[0])
                            #print(type(port[0]))
                            if port_list != '':
                                test =2
                                port_list +=','+port[0].rstrip('\r\n')
                                #print(port_list)
                            else:
                                port_list = port[0].rstrip('\r\n')
                            service_test = line.split('ttl')
                            service_info1 = re.sub('(^[0-9]+)',"",service_test[1].lstrip())
                            service_info2 = port[0]+"/"+service_info1.lstrip()
                            service_info2 = service_info2.rstrip('\r\n')
                            if serviceInfo != '':
                                serviceInfo += ','+ service_info2
                            else:
                                serviceInfo = service_info2
                        else:
                            test = 1
                        if result_1 in line:
                            confirm_test='confirm'
                        if confirm_os_2 in line:
                            OS_1 = line.split(':')
                            if len(OS_1) == 2:
                                #print(OS_1[1])
                                OS_1[1] = OS_1[1].lstrip()
                                OS_1[1] = OS_1[1].rstrip('\r\n')
                                OS = OS_1[1]
                        if confirm_os_1 in line and OS == '':
                            OS_11 = line.split(';')
                            #print(OS_11[0])
                            if len(OS_11) == 2:
                                OS_22 = OS_11[0].split(':')
                                #print(OS_22[2])
                                OS = OS_22[2]
                            elif len(OS_11) == 3:
                                OS_22 = OS_11[1].split(':')
                                #print(OS_22[1])
                                OS = OS_22[1]
                        if 'Service Info:' in line and OS == '':
                            OS_111 = line.split(';')
                            #if len(OS_1)==1:
                            OS_111[0] = OS_111[0].lstrip()
                            if 'OS:' in line:
                                OS_222 = OS_111[0].split('OS:')
                                #OS = OS_222[1]
                                if len(OS_222) == 2:
                                    print("TEST!!!!!!")
                                    OS = OS_222[1].rstrip('\r\n')
                                #print(OS)    
                                #print('1')
                            elif 'OSs:' in line:
                                OS_222 = OS_111[0].split('OSs:')
                                OS = OS_222[1].rstrip('\r\n')
                                #print('2')
                            
                            #print(OS_222)
                            #OS = OS_2[1]
                            #elif len(OS_1)==2:
                            #    OS_2 = OS_1[0].split('OS:')
                                
                        if confirm_Host in line:
                            HOST_1 = line.split(';')
                            HOST_2 = HOST_1[0].split(':')
                            HOST = HOST_2[2].rstrip('\r\n')
                            if "1" in HOST :        
                                HOST = ''
                            elif "x20" in HOST:
                                test = HOST.split("\r")
                                HOST = test[0].strip('\x20'+'\r\nServer'+'\r\nSer'+'\r\nServ'+'\r\nSe'+'"\x20')
                                 
                           #print(HOST_1[0])
                        #if port_list =='':
                        #    test_ = 2
                        #    #print(full_name_all+':TEST')
                        #elif port_list != '':
                        #    test=2              
                #writer.writerow([ip_result,HOST,OS, port_list, ip_C_class, confirm_test, serviceInfo])                    
                        print(OS)
                if port_list !='':
                    writer.writerow([ip_result,HOST,OS, port_list, ip_C_class, confirm_test, serviceInfo])                    
                else:
                    print("no Port")
dir_parsing()
