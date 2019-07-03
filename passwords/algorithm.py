#Sample Chunks of code
#Rough work for a few functions 

name='sam '
passw='mo vo'
comp='gish it '
def writer():
    with open('Password.txt','a') as file:
        file.write(comp+':\n\nUsername:'+name+'\nPassword:'+passw+'\n\n')
        
def count():
    #counts number of entries
    i=0
    with open('Password.txt','+r') as file:
        for line in file:
            for part in line.split():
                if "Username:" in part:
                    i+=1
    return(i)             

def checker():
    a,b,c=[],[],[]
    i=0
    with open('Password.txt','+r') as file:
        for line in file:
            i+=1
            print(line,end='')
            if i%5==1:
                print("herby:",i)
                part=line.split(":")
                a.append(part[0])
            if i%5==3:
                part=line.split(":")
                part[1]=part[1].strip('\n')
                b.append(part[1])
            if i%5==4:
                part=line.split(":")
                part[1]=part[1].strip('\n')
                c.append(part[1])
    print(a,b,c)
    print(len(k))
    for i in range(0,len(a)):
        if comp==a[i] and name==b[i] and passw==c[i]:
                print("copied already")
                
       
