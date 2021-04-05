#Add to number
num1=5
num2=10

sum = num1 + num2
print("Sum of {0} and {1} is {2}".format(num1,num2,sum))

#Adding two number provided by user input
number1 = input("First number: ")
number2 = input("Second number: ")

sum = float(number1) + float(number2)
print("The sum of {0} and {1} is {2}".format(number1,number2,sum))


#Add two binary numbers 
a = "1101"
b = "100"

max_len = max(len(a), len(b))
a = a.zfill(max_len)
b = b.zfill(max_len)

result = ''
carry = 0
for i in range (max_len-1,-1,-1):
    r = carry
    r += 1 if a[i] == '1' else 0
    r += 1 if b[i] == '1' else 0
    result = ('1'if r%2 == 1 else '0') + result
    
    carry = 0 if r<2 else 1
    
if carry != 0:
   result = '1' + result 
print(result.zfill(max_len))    


#Add two binary numbers with functions
a = "1101"
b = "100"

sum = bin(int(a,2) + int(b,2))

print(sum[2:])

#Add two octal numbers

a = "123"
b = "456"

sum = oct(int(a,8) + int(b,8))
print(sum[2:])

#Add to hexadecimal numbers

a = "01B"
b = "378"

sum = hex(int(a, 16) + int(b, 16))

print(sum[2:])
    
    
    
    
