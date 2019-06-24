from pyautogui import position as mousepos
import time

def full_box():
   def box_find():
      x=[]
      c=0
      while True:
         for i in range(4):         #reads mouseposition 4 times with 0.3s gap
             x.append(mousepos())
             time.sleep(0.3)
         for i in range(4):         #checks whether all 4 readings are same
             if x[0]==x[i]:
                 c+=1
         if c==4:                   #if all four are same then break loop
             break
         else:
             x=[]                   #else restart the function
             c=0
      return(x[0])

   def splitting(x):
      x=x.strip('Point')
      x=x.split(',')   
      x[0]=x[0].strip('(x=')
      x[1]=x[1].strip(' y=')
      x[1]=x[1].strip(')')
      return(x)

   print("starting...")
   time.sleep(.5)
   x=str(box_find())
   l,u=splitting(x)   
   print("waiting..")
   time.sleep(1)
   print("restart for bottom right")
   x=str(box_find())
   r,d=splitting(x)
   return(l,u,r,d)

print(full_box())
