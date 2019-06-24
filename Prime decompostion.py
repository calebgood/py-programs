x=int(input("Enter number:"))
for num in range(2, int(x ** 0.5) + 1):
    i=0
    while x % num == 0:
        i+=1
        x=x//num         
    if i>0:
        print(num,i)
if x>2:
    print(num,1)


