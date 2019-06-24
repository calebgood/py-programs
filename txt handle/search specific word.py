import mmap

#path=str("C:\Users\Sam\Desktop\Tensorflow (deep learning)\pixelBot")
var=b'tfgh'
with open('test.txt', 'rb', 0) as file, \
    mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
        #print(s.read())
        print("\n\n\n")
        if s.find(var) != -1:
            print('true')
        else:
            print("false")
        print(s.find(var))


