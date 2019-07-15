import os
import time
space=' '
column='|'
def cls():
        os.system('cls')
key1=input("ENTER 'S' FOR STOPWATCH OR 'T' FOR TIMER OR PRESS 'ENTER' TO QUIT: ")
cls()
while key1 not in ['S','T','t','s','']:
    key1=input("ENTER A VALID INPUT,S FOR STOPWATCH OR T FOR TIMER:")
    cls()
if key1 in ['s','S']:
    def clock():
        hour =0
        minute=0
        second=0
        day=0
        while True:
  # FOR SPACING OF TOP PORTION
            for i in range(24):
                print(space.rjust(167,' '))
                
  # FOR PRINTING OF MATTER(CLOCK),PRINTING IT IN CENTER OF THE SCREEN              
            print(space.rjust(80,' '),"THE TIME IS:", day ,':',  hour , ":",  minute ,":", second)
            print(space.rjust(80,' '),' '.rjust(10,' '),"D   H   M   S")
            print(space.rjust(80,' '),"D=Day,H =Hour,M=Minute,S=Second")
            
  # FOR SPACING OF BOTTOM PORTION
            for i in range(24):
                print(space.rjust(167,' '))

            time.sleep(0.93)            #TO MAKE PRINTING DELAY BY 1 SEC,WHICH WOULD MAKE IT MORE OF A PRACTICAL TIMER
            cls()                       #CALLING OF FUNCTION WHICH CAUSES TO REPLACE IT IN ITSELF
            second +=1                  #FOR REDUCING SECOND BY 1 

  #CONVERSION FACTORS OF SECOND,MINUTE,HOUR AND DAY                    
            if second == 60:
                  minute += 1
                  second = 0
            if minute == 60:
                  hour += 1
                  minute = 0
            if hour == 24:
                  day += 1
                  hour =0
                  
    clock()
                  
if key1 in ['t','T']:
    def clock():    
        space = ' '
        column = '|'          
        
  # INITIALISING THE PARAMETERS OR INPUT
    while True:
       try:     
        day=    int(input('ENTER DAY       :'))
        cls()
        break
       except:
               print('ENTER VALID INPUT')
               time.sleep(2)
               cls()
    while True:
       try:
        hour =  int(input('ENTER HOUR      :'))
        cls()
        break
       except:
               print('ENTER VALID INPUT')
               time.sleep(2)
               cls()
    while True:
       try:
        minute= int(input('ENTER MINUTE    :'))
        cls()
        break
       except:
               print('ENTER VALID INPUT')
               time.sleep(2)
               cls()
    while True:
       try:
        second= int(input('ENTER SECOND    :'))
        cls()
        break
       except:
               print('ENTER VALID INPUT')
               time.sleep(2)
               cls()
 
          
    while True:
  # FOR SPACING OF TOP PORTION
            for i in range(24):
                print(space.rjust(167,' '))
                
  # FOR ENDING OF TIMER,INCLUDING BREAK AND DISPLAY OF END
            if day==0 and second==0 and minute==0 and hour==0:
                 for i in range(1):
                      print(space.rjust(167,' '))    #space=' ',column='|'
                 print(space.rjust(80,' '),space+space.rjust(6,'-'),'',
                       space.rjust(3,'-'),'  ',space+space,space.rjust(6,'-'))
                 time.sleep(0.4)
                 for i in range(3):
                      print(space.rjust(80,' '),column,'     ',column,'|',' '
                            ,column,' ',column,'   ',column)
                      time.sleep(0.4)
                 print(space.rjust(80,' '),space+space.rjust(6,'-'),column,column
                       ,space,column,space,column,column.rjust(5,' '))
                 time.sleep(0.4)
                 for i in range(3):
                      print(space.rjust(80,' '),column,'     ',column,'|',' '
                            ,column,' ',column,'   ',column)
                      time.sleep(0.4)
                 print(space.rjust(80,' '),space+space.rjust(6,'-'),space,
                       space+space.rjust(4,'-'),'  ',space.rjust(6,'-'))
                 time.sleep(10)
                 break
  # FOR PRINTING OF MATTER(CLOCK),PRINTING IT IN CENTER OF THE SCREEN                        
            print(space.rjust(80,' '),"THE TIME IS:", day ,':',  hour , ":",  minute ,":", second)
            print(space.rjust(80,' '),' '.rjust(10,' '),"D   H   M   S")
            print(space.rjust(80,' '),"D=Day,H =Hour,M=Minute,S=Second")

  # FOR SPACING OF BOTTOM PORTION
            for i in range(24):
                print(space.rjust(167,' '))
            
            time.sleep(1)   #TO MAKE PRINTING DELAY BY 1 SEC,WHICH WOULD MAKE IT MORE OF A PRACTICAL TIMER
            cls()           #CALLING OF FUNCTION WHICH CAUSES TO REPLACE IT IN ITSELF
            second -=1      #FOR REDUCING SECOND BY 1 

  #CONVERSION FACTORS OF SECOND,MINUTE,HOUR AND DAY
            if second == -1:
                  minute -= 1
                  second = 59

            if minute == -1:
                  hour -= 1
                  minute = 59

            if hour == -1:
                  day -= 1
                  hour = 0
    clock()
if key1 =='':
    print('OKAY,THANK YOU')
    time.sleep(10)
