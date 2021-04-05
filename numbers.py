#Armstrong numbers

def power(x,y):
    
    if y == 0 :
        return 1
    if y % 2 == 0:
        return power(x,y //2)*power(x,y //2)
    
    return x * power(x,y //2)*power(x,y //2)

def order(x):
    
    n = 0
    while(x != 0):
        n = n + 1
        x = x //10
    return n

def isArmstrong(x):
    n = order(x)
    temp = x
    sum1 = 0
    
    while(temp != 0):
        r = temp %10
        sum1 = sum1 + power(r,n)
        temp = temp //10
    return (sum1 == x)

x = 153
print(isArmstrong(x))


#Prime numbers

start = 11
end = 25

for i in range (start,end+1):
    if i>1:
        for j in range (2,i):
            if (i % j == 0):
                break
            else:
                print(i)
                
                
                
#numberisprimeornot

num = 11
if num > 1:
    for i in range (2, int(num/2)+1):
        
        if(num % i) == 0:
            print(num,"is not a prime number")
            break
        else:
            print(num,"is a prime number")
else:
    print(num,"is not a prime number")
    

#n-thfibonacci number(recursion)

def Fibonacci(n):
    if n<0:
        print("Incorrect input")
        
    elif n == 1:
        return 0
    elif n ==2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

print(Fibonacci(9))

#Fibonacci(dynamic)

FibArray = [0,1]
def fibonacci(n):
    if n<0:
        print("incorrect inpırt")
    elif n <= len(FibArray):
        return FibArray[n - 1]
    else:
        temp_fib = fibonacci(n - 1) + fibonacci (n - 2)
        FibArray.append(temp_fib)
        return temp_fib

print(fibonacci(9))

#Fibonaccidynamic(space optimization)

def fibonacci(n):
    a = 0
    b = 1
    if n < 0 :
        print("incorrect input")
        
    elif n == 0:
        return a
    
    elif n == 1:
        return b
    else:
        for i in range (2,n):
            c = a + b
            a = b
            b = c
        return b
print(fibonacci(9))

#fibonacciwitharrays

def fibonacci(n):
    arr = [0] * (n+1)
    arr [1] = 1
    for i in range (2,n+1):
        arr[i] = arr[i - 1] + arr[i - 2]
    return arr[n]

if __name__ == " __main__":
    print(fibonacci(int(input("Enter the term:"))))
    
    
    
#fibonacciisnot
import math
def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x
def isFibonacci(n):
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n -4)

for i in range(1,11):
    if(isFibonacci(i) == True):
        print(i,"is a Fibonacci Number")
    else:
        print(i,"is a not Fibonacci Number")
        
#natural numbers

def squaresum2(n):
    return (n*(n+1)*(2*n+1))//6

n = 4
print(squaresum2(n))

#method2

def squaresum3(n):

    return (n*(n+1)/2)*(2*n+1)/3

n = 4 
print(squaresum3(n))    

#cube sum of first n natural numbers

def sumOfSeries(n):
    sum = 0
    for i in range(1, n+1):
        sum += i*i*i
    return sum

n = 5
print(sumOfSeries(n))

#method2

def sumOfSeries2(n):
    x = (n*(n+1)/2)
    return (int)(x * x)

n = 5
print(sumOfSeries2(n))

#method3

def sumOfSeries3(n):
    x = 0
    if n % 2 == 0:
        x = (n/2) * (n+1)
    else:
        x = ((n+1)/2) * n
        return (int)(x * x)
    
n = 5
print(sumOfSeries3(n))
