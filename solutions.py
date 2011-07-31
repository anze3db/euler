'''
Created on Mar 9, 2011

@author: smotko
'''
import math
from random import random

#Helpers:
def _is_pol(s):
    
    for i in xrange(0, len(s)):
        if len(s) <= i:
            break
        if s[i] != s[i*(-1) - 1]:
            return False
        
    return True

def _is_prime(x):
    
    if x < 2:
        return False
    for j in xrange(2, int(math.sqrt(x))+1):
        #print x, j, x % j
        if x % j == 0:
            return False
    return True
    
def prob1(x):
    sum = 0
    for i in range(0, x):
        if i%5 == 0 or i%3 == 0:
            sum+=i
    print sum
    
def prob2(x):
    sum = 1
    f1 = 1
    f2 = 2
    for i in range(100):
        if f1 > x: 
                break
        if f1 % 2 != 0:        
            sum += f1
                    
        f1, f2 = f2, f1 + f2
    print sum

def prob3(n):
    for i in xrange(int(math.sqrt(n)), 1, -1):
        if n % i == 0:
            
            if _is_prime(i):
                print i
                return

def prob4():
    pols = []
    for i in xrange(999, 1, -1):
        for j in xrange(999, 1, -1):          
            if _is_pol(str(i*j)):    
                pols.append(i*j)
    print max(pols)
            

            
def prob5():
    
    def idev(x):
        for j in range(1, 20):
            if x % j != 0:
                return False
        return True

    for i in xrange(0, 10000000000, 20):
            if idev(i):
                print i
                
def prob6(n):
    nl = range(1, n+1)
    s = sum(nl)**2
    p = 0
    for i in nl:
        p += i**2
    print s - p, s, p
    
                
def prob7(n):
    num = 0
    print _is_prime(2)
    for i in xrange(1000000):
        if _is_prime(i):
            num += 1
            if num == n:
                print i 
                return



def prob8(str):
    #remove whitespace:
    str = ''.join(str.split())
    a = []
    xs = []
    for i in str:
        a.append(int(i))
        if(len(a) > 5):
            x = 1
            for j in a[-5:]:
                x *= j
            xs.append(x)
    print max(xs)

def prob9(n):
    for i in xrange(1, n):
        for j in xrange(i+1, n):
            c = math.sqrt(i**2 + j**2)
            if i+j+c == n:
                print int(i*j*c)
                return
            #for k in xrange(j+1, 500):
            #    if i**2 + j**2 == k**2 and  i+j+k == n:
            #        print i*j*k, i, j, k
            #        return

def prob10(n):
    sum = 2
    for i in xrange(3, n, 2):
        if _is_prime(i):
            sum += i
            #print i
    print sum
        
    
def prob11(str):
    arr = []
    max = 0
    hr = range(4)
    for i in str.split('\n'):
        arr.append(i.split(' '))
    
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if len(arr[i][j]) - j > 3:
                m = 1
                for n in hr:
                    m *= int(arr[i][j+n])
                if m > max:
                    max = m
                if len(arr[i]) - i > 3:
                    m = 1
                    for n in hr:
                        m *= int(arr[i+n][i+n])
                    if m > max:
                        max = m
                
            if len(arr[i]) - i > 3:
                m = 1
                for n in hr:
                    
                    m *= int(arr[i+n][j])
                if m > max:
                    max = m
                if j - len(arr[i][j]) > 3:
                    m = 1
                    for n in hr:
                        m *= int(arr[i+n][j-n])
                    if m > max:
                        max = m
    print max
                
            
            
def prob11v2(str):
    #product = lambda s: reduce(lambda a,b:a*b, s) 
    arr = []
    mx = 0
    ADJECENT = 4
    #parse the string and add zeros for border conditions:
    for i in str.split('\n'):        
        arr.append([0]*ADJECENT + i.split(' ') + [0]*ADJECENT)    
    arr += [[0]*len(arr[0])]*ADJECENT

    hr = range(ADJECENT)
    for i in range(len(arr)-ADJECENT):
        for j in range(len(arr[i])-ADJECENT):
            d = [1]*4          
            for n in hr:
                d[0] *= int(arr[i][j+n])
                d[1] *= int(arr[i+n][i+n]) 
                d[2] *= int(arr[i+n][j])
                d[3] *= int(arr[i+n][j-n])
            if (max(d)) > mx:
                mx = (max(d))
    
    
    print mx


def prob12(n):
    
    tri = 0
    for i in xrange(1000000):
        tri += i
        dev = 1
        if tri % 2 != 0:
            continue
        for i in xrange(1, int(math.sqrt(tri))+1):
            if tri % i == 0:
                dev += 1

        if dev*2 > n:
            print tri
            return



def prob13(str):
    # Solved this one in the shell, lol
    pass
    
def prob14(n):
    
    def _nextS(m):
        
        if m == 1: return 1
        if m % 2 == 0:
            return m/2
        return 3*m + 1
    blacklist = set()
    max = 0
    max_i = 1
    for i in xrange(1, n, 2):
        cnt = 0
        if i in blacklist:
            continue
        #print i
        j = _nextS(i)
        while(j > 1): 
            
            blacklist.add(j)            
            cnt += 1
            j = _nextS(j)
            
        
        if cnt > max: 
            max = cnt
            max_i = i
    print max_i

def prob15(x, y):
    print math.factorial(x+y)/(math.factorial(x)*math.factorial(y))
    
def prob16(x):
    sum = 0
    for i in str(2 ** x): 
        sum += int(i)
    print sum    
    
def prob17(n):
    
    def lowerthan100(i):
        
        if i < 20:
            return names[i]
        return names20[i/10] + names[i%10]

    
    names = ['', 'one', 'two', 'three', 'four', 'five',
         'six', 'seven', 'eight', 'nine', 'ten',
         'eleven', 'twelve', 'thirteen', 'fourteen',
         'fifteen', 'sixteen', 'seventeen', 'eighteen',
         'nineteen',
         ]
    names20 = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
               'eighty', 'ninety']
    
    str = ''
    for i in xrange(n):
        if i < 100:
            str += lowerthan100(i)
        else:
            str += names[i/100] + 'hundred'
            if len(lowerthan100(i%100)) > 0:
                str += 'and' + lowerthan100(i%100)
    str += 'onethousand'
    print len(str)

def prob18(str):
    arr = []
    for i in str.split('\n'):
        arr.append(i.split(' '))
    #convert chars to int:
    for i in xrange(0, len(arr)):
        for j in xrange(0, len(arr[i])):
            arr[i][j] = int(arr[i][j])
            
    for i in xrange(1, len(arr)):        
        for j in xrange(0, len(arr[i])):
            
            if j == 0:
                arr[i][j] += arr[i-1][0]
            elif j == len(arr[i])-1:
                arr[i][j] += arr[i-1][j-1]
            else:
                arr[i][j] += max([arr[i-1][j-1], arr[i-1][j]])
                      
    print max(arr[-1])

def prob19():
    
    import datetime
    sundays = 0
    d = datetime.date(1901, 1, 1)
    while(d < datetime.date(2001, 1, 1)):
        if d.weekday() == 6 and d.day == 1:
            sundays += 1
        d += datetime.timedelta(days = 1)
        
    print sundays

def prob20(x):
    sum = 0
    for i in str(math.factorial(x)):
        sum += int(i)
    print sum

def prob21(n):
    
    def sum_proper_dev(n):
        s = 0
        for i in xrange(1, n/2+1):
            if n % i == 0:
                s += i
        return s
    
    checked = set()
    s = 0
    for i in xrange(1, n):
        if i in checked:
            continue
        checked.add(i)
        dev_i = sum_proper_dev(i)
        checked.add(dev_i)
        dev_dev_i = sum_proper_dev(dev_i)
        if i == dev_dev_i and i != dev_i:
            print dev_i, i
            s += dev_i + i
    print s   
    
def prob22(arr):
    
    OFFSET = 64
    arr.sort()
    s = 0
    for i in xrange(0, len(arr)):
        score = 0
        for j in arr[i]:
            score += ord(j) - OFFSET 
        
        s += score * (i+1)
    print s

def prob23():
    STOP_HERE = 28123

    abundant = []
    abundant_pairs = set()
    def is_abundant(n):
        sum = 0
        for i in xrange(2, int(math.sqrt(n))+1):
            if n % i == 0:
                sum += i
                if i != n/i:
                    sum += n/i
        if sum > n: 
            abundant.append(n)
            for j in abundant:
                abundant_pairs.add(j + n)
            
        return False
    for i in xrange(STOP_HERE+1):
        is_abundant(i)   
    sum = 0   
    # print abundant
    for i in xrange(STOP_HERE):
        if i not in abundant_pairs:
            sum += i     
    print sum

def prob24(s):
    def lexi_permute(str):
        
         arr = []
         while True:
        
            arr.append(str)
            
            # find j
            n = len(str) - 1 
            j = n - 1
            while str[j] >= str[j+1]:
                j -= 1
                if j == -1:
                    return arr
            
            # increase str j
            l = n
            while str[j] >= str[l]:
                l -= 1
            str = swap(str, j, l)
        
            # reverse
            k = j + 1
            l = n
            while k < l:
                if k < l:
                    str = swap(str, k, l)
                k += 1
                l -= 1
            
        
        
    def swap(str, i, j):
        if i > j:
            i,j = j,i
        if i == j:
            return str
        return str[:i] + str[j] + str[i+1:j] + str[i] + str[j+1:]    
    arr = lexi_permute(s)
    print arr[1000000-1]
    
def prob25(n):
    
    a = 1
    b = 2
    i = 2
    while(True):
        i += 1
        a,b = b, a+b
        if len(str(a)) == n:
            print i
            return

def prob28(size):
    
    count = 0
    count_krog = 0
    sum = 1
    limit = 1
    
    for i in xrange(2, size*size+1):
        if count == limit:
            sum += i
            count_krog += 1
            count = 0
            if count_krog == 4:
                count_krog = 0
                limit += 2
        else: count += 1
    print sum
    
def prob29(a,b):
    s = set()
    
    for i in range(2,a+1):
        for j in range(2,b+1):
            s.add(i**j)
    
    print len(s)

def prob30(pow):
    s = 0
    for i in xrange(2, 1000000):
        sum = 0
        for j in str(i):
            sum += int(j) ** pow
        if sum == i:
            s += i
            print i
    print s
    
#lame:
def prob45(max):

    def tri(n):
        return n*(n+1)/2
    def pen(n):
        return n*(3*n-1)/2
    def hex(n):
        return n*(2*n-1)
    
    
    max += 1
    nt = np = nh = 0
    mp = mh = 1
    mt = 0 
    while( not (mt == mp == mh)):
        
        while(mt < max):
            nt += 1
            mt = tri(nt)
        max = mt
        
        while(mp < max):
            np += 1
            mp = pen(np)
        max = mp

        while(mh < max):
            nh += 1
            mh = hex(nh)
        max = mh
        
        
    print mt, np, nt, nh    
        
def prob48(n):
    s = 0
    for i in xrange(1, n+1):
        s += i**i
        print i
    st = str(s)
    print st[-10:]


def prob26():
    

    

   
if __name__ == '__main__':
    
    from params import *
    prob26()
    #prob48(1000)
    #prob45(40755)
    #prob30(5)
    #prob29(100,100)
    #prob28(1001)
    #prob25(1000)
    #prob24('0123456789')    
    #prob23()
    #prob22(param22)
    #prob21(10000)
    #prob20(100)
    #prob19()
    #prob18(param18)
    #prob17(1000)
    #prob16(1000)
    #prob15(20, 20)
    #prob15(20)
    #prob14(1000000)
    #prob13(param13)
    #prob12(500)
    #prob11v2(param11)
    #prob10(2000000)
    #prob9(1000)
    #prob8(param8)   
    #prob7(10001)
    #prob6(100)
    #prob5()
    #prob4()
    #prob3(600851475143)
    #prob2(4000000)
    #prob1(1000)
    
    
    
