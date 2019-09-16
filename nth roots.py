#Last digit is arbitary and may vary
'''
The solve function finds the nth root of the given number
By default the sqrt function is activated

The function has a time complexity O(log(n))
Args:
	b:The number to find the nth root
	n:nth power	eg:n=2 implies sqrt function
	iter:A boolean function to print the number of iterations or not
'''
def solve(b,n=2,iter=False):
  a=0
  num=b
  i=0
  while True:
    i+=1
    m = (a + b)/2
    if abs(m**n-num)<=0.000000001:
      m=float('%.8f'%m)
      if (m*10)%10==0:
        if iter:
        	print("Number of iterations:",i)
        return int(m)
      else:
        if iter:
        	print("Number of iterations:",i)
        return m
    elif m**n-num<=0:
      a = m
    else:
      b = m
	 

if __name__=='__main__':
  num=int(input('Enter a number:'))
  print(solve(num,iter=True))
  print('By default the sqrt function is activated.\nYou can change that by changing the arguments')
  
