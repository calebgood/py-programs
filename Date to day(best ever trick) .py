day=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]    #some database numbers and strings
mdoom=[3,28,14,4,9,6,11,8,5,10,7,12]
while True:
    entry=input('\nEnter a date in DD/MM/YYYY format:')           #Input date in a specified format
    date,month,year = map(int,entry.split('/'))                 #Get the date,month and year
    centdoom=[3,2,0,5]
    a=centdoom[((year//100)%4)-3]
    b=(year%100)//12
    c=(year%100)%12
    d=c//4                                                      #Random calculations for doomsday :)
    e=a+b+c+d

    if year%4==0:                                               #Checks for leap year
        mdoom[0],mdoom[1]=4,29

    ddoom=e%7                                                   #finds a date in the 1st week which has the same day as the doomsday    
    r=mdoom[month-1]                                            #Gives the doomsdate in the input month 
    r=r%7
    r=ddoom-r                                                   
    date=date%7                                                 #finds a date in the 1st week which has the same day as the input date
    print('\n',day[(r+date)%7])                                      #prints the output
    k=input('\nTry again?(y/n)')
    if k=='y':
        continue
    else:
        break
    
