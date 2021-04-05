#sumofarray

def _sum(arr):
    sum = 0
    for i in arr:
        sum = sum + i
        return sum + sum

arr = []
arr = [12,3,4,15]
n = len(arr)
ans = _sum(arr)
print("Sum of the array is",ans) 









#method2
arr = []
arr = [12,3,4,15]

ans = sum(arr)
print("Sum of the array is",ans)   

#largestelementin an Array

def largest(arr,n):
    max = arr[0]
    
    for i in range(1,n):
        if arr[i] > max :
            max = arr[i]
    return max

arr = [10,324,45,90,9808]
n = len(arr)
Ans = largest(arr, n)
print(Ans)

#rotatearray

def rotateArray(arr,n,d):
    temp = []
    i = 0
    while(i < d):
        temp.append(arr[i])
        i = i + 1
    i = 0
    while(d < n):
        arr [i] = arr [d]
        i = i + 1
        d = d + 1
    arr[:] = arr[: i] + temp 
    return arr

arr = [1,2,3,4,5,6,7]
print(rotateArray(arr ,len(arr) , 2))

#method2

def leftRotate(arr,d,n):
    for i in range(d):
        leftRotatebyOne(arr,n)

def leftRotatebyOne(arr,n):
    temp = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp

def printArray(arr,size):
    for i in range(size):
        print("%d"% arr[i],end="")

arr = [1,2,3,4,5,6,7]
leftRotate(arr, 2, 7) 
printArray(arr, 7)

#slicing
def rotateList(arr,d,n):
    arr[:] = arr[d:n] + arr[0:d]
    return arr
arr = [1,2,3,4,5,6]
print(arr)
print(rotateList(arr, 2, len(arr)))

#split array
def splitArr(arr, n, k):
    for i in range (0, k):
        x = arr[0]
        for j in range (0, n-1):
            arr[j] = arr[j + 1]
            
        arr[n - 1] = x
        
arr = [12,10,5,6,52,36]
n = len(arr)
position = 2

splitArr(arr, n, position)

for i in range (0,n):
    print(arr[i], end ="")
    
#another split

def splitArr(a,n,k):
    b = a[:k]
    return (a[k::]+b[::])

arr = [12,10,5,6,52,36]
n = len(arr)
position = 2
arr = splitArr(arr, n,position)
for i in range(0,n):
    print(arr[i], end = "") 

#findremainder
def findRemainder(arr, lens, n):
    mul = 1
    for i in arr:
        mul = mul * (i%n)
        
    return mul % n 

arr = [100,10,5,25,35,14]
lens = len(arr)
n = 11
print("\n",findRemainder(arr, lens, n))

#monotonic
def isMonotonic(A):
    return (all(A[i] <= A[i+1] for i in range (len(A)-1)) or all(A[i] >= A[i+1] for i in range(len(A)-1)))

A = [6,5,4,4]
print(isMonotonic(A))    
        
        
           


       