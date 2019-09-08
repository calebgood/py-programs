#Last digit is arbitary and may vary
def solve(a, b,n=2):
  num=b
  while True:
    m = (a + b)/2
    if abs(m**n-num)<=0.000000001:
      m=float('%.8f'%m)
      if (m*10)%10==0:
        return int(m)
      else:
        return m
    elif m**n-num<=0:
      a = m
    else:
      b = m
  

if __name__=='__main__':
  num=int(input('Enter a number:'))
  print(solve(0,num))
  print('By default the sqrt function is activated.\nYou can change that by changing the arguments')
  
