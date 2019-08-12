subs = open("big.txt")

data= subs.read()

a=50
data=data.split('\n')
print(len(data))
#print(data)
full=""
trans=[]
for k in range(0, a):
    for i in range((k * len(data)) // a, ((k + 1) * len(data)) // a):
        full = full + data[i]
    trans.append(full)
    #print("###",full,"############")
    full = ""
    
#full = full_trans.split('\n\n')
print(len(trans))
'''
with open("duh.txt","w") as f:
    for i in range(len(data)):
        f.write(data[i])
'''
subs.close()
