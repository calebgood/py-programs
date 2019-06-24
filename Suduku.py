tup = input("enter list:")[1:-1].split(',')
x = input('Enter mapping valid Sudoku eg. 3 for 9 x 9:')
e = input('Enter 9 for 9 x 9 ...12 for 12 x 12:')
f = input('Enter 3 if its a 9 x 9 ... n^2 x n^2:')
x = int(x)
e = int(e)
f = int(f)
squares = []
for i in range(len(tup)):
    squares.append(tup[i:] + tup[:i])

    #Everything below here is just printing
for s in range(x):
      for d in range(0,e,f):
        for si in range(s,e,f):
          for li in range(d,d+f):
            print(squares[si][li], end = '')
        print('')
