#interest

# Simple interest = (P*T*R)/100

def simple_interest(p,t,r):
    print('The principal is',p)
    print('The time period is',t)
    print('The rate of interest is',r)
    
    si = (p*t*r)/100
    print('The simple Interest is',si)
    return si

simple_interest(8,6,8)


#Compound interest
#A-P

def compound_interest(principle, rate, time):
    Amount = principle * (pow((1 + rate /100),time))
    CI = Amount - principle
    print("Compound interest is",CI)
    
compound_interest(10000, 10.25, 5)    