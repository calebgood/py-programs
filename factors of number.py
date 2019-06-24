import time
c=0
x=int(input("Enter number:"))
t1=time.time()
for i in range(1,x+1):
    if x%i==0:
        print("factor",c+1,":",i)
        c=c+1
print("Total number of factors:",c)
t2=time.time()
print(t2-t1)
