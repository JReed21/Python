import math

def solution(n):
    y = 1
    z = 10
    m = [1,5,10,50,100,500,1000]
    rom = {1 : 'I', 5 : 'V', 10 : 'X', 50 : 'L', 100 : 'C', 500 : 'D', 1000 : 'M'}
    ret = []
    if(n == 1):
      return 'I'
    while(n != 0):
        if(n % z != 0):
            x = (n % z)
            if(x == 1):
                ret.insert(0,rom[y])
                x = 0
            if(x == 9):
                ret.insert(0,rom[y*10])
                ret.insert(0,rom[y])
                x = 0
            if(x < 4):
                while(x > 0):
                    ret.insert(0,rom[y])
                    x = x - 1
            if(x == 5):
                ret.insert(0,rom[y*5])
                x = 0
            if(x == 4):
                ret.insert(0,rom[y*5])
                ret.insert(0,rom[y])
                x = 0
            if(5 < x < 9):
                while(x > 5):
                    ret.insert(0,rom[y])
                    x = x - 1
                ret.insert(0,rom[y*5])
        n /= z
        y *= 10
    return ''.join(ret) 
h = input()
print solution(h)