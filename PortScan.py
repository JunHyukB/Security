
#-*- coding:utf-8 -*-

import os
import threading
import time

#threads = list()
#threads1 = list()
sem = threading.Semaphore(5)

def A_class(ip, dir):
    for i in range(0,255):
        ip_edit = ip + '.'+str(i)
        for j in range(0,255):
            ip_edit2 = ip_edit + '.'+str(j)
            threads=[]
            for k in range(0,255):
                ip_edit3 = ip_edit2+'.'+str(k)
                threads.append(threading.Thread(target=Default_Ip, args=(ip_edit2, dir)))
        for thread in threads:
            time.sleep(1)
            thread.start()
                
        for thread in threads:
            thread.join()    
       
def B_class(ip, dir):
    for i in range(0,255):
        ip_edit = ip + '.'+str(i)
        print(ip_edit)
        threads=[]
        for j in range(0,255):
            ip_edit2 = ip_edit + '.'+str(j)
            print(ip_edit2+'Comfirm')
            print(str(j)+'Thread 1')
            threads.append(threading.Thread(target=Default_Ip, args=(ip_edit2, dir)))
        for thread in threads:
            time.sleep(1)
            thread.start()
                
        for thread in threads:
            thread.join()    
            

def C_class(ip, dir):
    ip_class = ip.split('.')
    temp = ''
    if '-' in ip_class[2]: 
        test = ip_class[2].split('-')
        
        for i in range(int(test[0]), int(test[1])):
            ip_test2 = ip_class[0]+'.'+ip_class[1]+'.'+str(i)
            threads=[]
            print(ip_test2)
            time.sleep(1)            
            for j in range(0,256):
                ip_edit = ip_test2 + '.' + str(j)
                
                print(str(j)+'Thread 1')
                threads.append(threading.Thread(target=Default_Ip, args=(ip_edit, dir)))
                    
            for thread in threads:
                time.sleep(1)
                thread.start()
                
            for thread in threads:
                thread.join()
            '''
            elif threads != [] or temp != ip_test2:
                for thread in threads1:
                    thread.start()
                for thread in threads1:
                    thread.join()
            temp = ip_class[0]+'.'+ip_class[1]+'.'+str(i)
            '''
    else:
        threads=[]
        for i in range(0,256):
            ip_edit = ip + '.' + str(i)  
            
            print(str(i)+'Thread 1')
            threads.append(threading.Thread(target=Default_Ip, args=(ip_edit, dir)))
        for thread in threads:
            time.sleep(1)
            thread.start()  
        for thread in threads:
            thread.join()
       
            
    
    
            
def Default_Ip(ip, dir):
    Split = ip.split('.')
    Dir_name = Split[0]+'.'+Split[1]+'.'+Split[2]
    test = Split[3].split('-')
    #디렉터리 네임 생성
    file_path = dir+'\\'+Dir_name
    #디렉터리 확인 및 생성
    if not os.path.isdir(file_path):
        os.mkdir(os.path.join(file_path))
    #nmap 명령어 설정
    nmap1 = 'nmap -sS -sV -O -vv -p1-1024,22222,33389,3389,53389,7001,7003,8080,8888,8090,9090,9099,8629,1521,1522,3306,1433,1434 '
    nmap2 = ' '+'-oN '+file_path+'\PORTSCAN_'+ip+'.txt'
    
    if '-' in Split[3]:
        for i in range(int(test[0]), int(test[1])):
            test_1 = Split[0] + '.' + Split[1] + '.' +Split[2] + '.' + str(i)
            nmap2 = ' '+'-oN '+file_path+'\PORTSCAN_'+test_1+'.txt'
            nmap = nmap1 + test_1 + nmap2
            sem.acquire()
            print(nmap)
            os.system(nmap)
            time.sleep(2)
            sem.release()
        
    else:
        nmap2 = ' '+'-oN '+file_path+'\PORTSCAN_'+ip+'.txt'
        nmap = nmap1 + ip + nmap2
        sem.acquire()
        print(nmap)
        os.system(nmap)
        time.sleep(2)
        sem.release() 
    
   
class Main:
    #ip 설정
    #ip = ['10.19.6.222', '10.19.6.223', '10.19.6.224','10.19.6.225','10.19.6.226','10.19.6.227','10.19.6.228','10.19.6.229','10.19.6.230','10.19.6.231','10.19.6.232','10.19.6.233','10.19.6.234','10.19.6.235','10.19.6.236','10.19.6.237','10.19.6.238','10.19.6.239','10.19.6.240','10.19.6.241','10.19.6.242','10.19.6.243','10.19.6.244','10.19.6.245','10.19.6.246','10.19.6.247','10.19.6.248','10.19.6.249','10.19.6.250','10.19.6.251','10.19.6.252','10.19.6.253','10.19.6.254','10.19.6.255']
    
    
    #ip = ['10.1.63','10.1.64','10.1.66','10.1.67'] 
    
    #사용자대역
    #ip = ['10.19.96-101']
    #ip = ['10.19.254-256']    
    #ip=['10.19.10']
    #2번 확인
    #ip = ['10.19.19.19']
    
    #1번 확인
    #ip = ['20.19.190-200']
    #ip = ['20.19.59']    
    #3번 완료
    ip = ['10.1']
    #ip = ['10.1.101-106','10.1.109']
    
    #4번 확인
    #ip = ['20.19.214']
    #ip = ['10.1.55.105',10.1.55.106]
    #ip = ['10.1.55.225','10.1.55.55','10.1.59.11','10.1.60.110','10.1.60.15','10.1.60.29','10.1.60.31','10.1.60.32','10.1.60.33','10.1.60.40','10.1.60.41','10.19.10.33','10.19.12.151','10.19.16.252','10.19.16.253','10.19.18.3','10.19.18.4','10.19.18.5','10.19.18.6','10.19.19.19','10.19.2.0','10.19.20.253','10.19.30.0','10.19.6.221','10.19.6.36','10.19.6.84','10.19.6.88','10.19.7.0','10.19.8.0','10.2.57.249']
    Dir = 'C:\\Users\\SMS\\Desktop\\PORTSCAN'
    nmap = ''
    for ip_test in ip:
        ip_class=ip_test.split('.')
        if len(ip_class)==4:
            Default_Ip(ip_test, Dir)
        elif len(ip_class)==3:
            '''
            if '-' in ip_class[2]: 
                test = ip_class[2].split('-')
                for i in test:
                    ip_test2 = ip_class[0]+ip_class[1]+str(i)
                    C_class(ip_test2, Dir)
            else:
                C_class(ip_test, Dir)
            '''
            C_class(ip_test, Dir)
        elif len(ip_class)==2:
            B_class(ip_test, Dir)
        elif len(ip_class)==1:
            A_class(ip_test, Dir)
        else:
            print('error')
