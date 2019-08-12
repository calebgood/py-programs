import numpy as np
import matplotlib.pyplot as plt

np.random.seed(2)

wt=np.zeros((3,))
error=[]
cs=[]
pred=[]
def err(h,yl):
    return((yl-h)**2)
'''
def derv(x):
    return()
'''
def curve(x,weight):
    return(np.dot(np.array([x**2,x,1]),weight))

ip=np.array([[1,1],[2,4],[3,9],[4,16]])

x=np.array([i[0] for i in ip])
y=np.array([i[1] for i in ip])

while True:
    for i in ip: 
        h=curve(i[0],wt)
        #print(i,h)
        error.append(err(h,i[1]))
        #print(err(h,i[1]))
        pred.append(h)
    cost=np.sum(error)/len(y)
    print('cost:',cost)
    cs.append(cost)
    pred=np.array(pred).reshape(4,)
    error=np.array(error).reshape(4,)
    print('shapes:',error.shape,pred.shape,y.shape,x.shape,wt.shape)
    wt=wt+(pred-y)
    error=[]
    print(wt,'\n\n\n',cs)
    if cost>=144:
        break
    pred=[]
    

plt.plot(x,pred)  
plt.xlabel('x')
plt.ylabel('y') 
plt.scatter(x,y, s = 30, c = 'b')
plt.show()
