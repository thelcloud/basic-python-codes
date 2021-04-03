class Calc(object):
    def __init__(self,a,b):
        "initialize values"
        
        #attribute
        self.value1=a
        self.value2=b
        
    def add(self):
        "addition a+b = result -> return result"
        return self.value1 + self.value2
    def subs(self):
        "substraction a-b = result -> return result"
        return self.value1 - self.value2
    
    def multiply(self):
        "multiply a*b = result -> return result"
        return self.value1 * self.value2
    
    def division(self):
        "division a/b = result -> return result"
        return self.value1 / self.value2
    
    
    
print("Choose add(1), subs(2), multiply(3), division(4)")
selection = input("select 1 or 2 or 3 or 4")

v1 = int(input("First value"))
v2 = int(input("Second value"))

c1=Calc(v1, v2)
if selection == "1":
    add_result = c1.add()
    print("Add: {}".format(add_result))
elif selection == "2":
    subs_result = c1.subs()
    print("Subs: {}".format(subs_result))
    
elif selection == "3": 
    multiply_result = c1.multiply() 
    print("Mutiply: {}".format(multiply_result))

elif selection == "4":
    division_result=c1.division()
    print("Div: {}".format(division_result))
else:
    print("Error there is no proper selection")
