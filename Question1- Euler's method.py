#Euler's Method 
import math
import library

#Function 1 
def f_1(x,y):
    return (y*math.log(y))/x 
    
#Function 2 
def f_2(x,y):
    return 6-((2*y)/x)
    

#Analytical solution for first differential equation
def fxn1(x,y):
    arr1=[]
    arr2=[]
    h=0.2
    i=0 
    while i<=10:
        arr1.append(x)
        arr2.append(y)
        y=math.exp(0.5*x)
        x=x+h
        i=i+1 
    return arr1,arr2 


#Analytical solution for second differential equation 
def fxn2(x,y):
    arr1=[]
    arr2=[]
    h=0.2 
    i=0  
    while i<=10:
        arr1.append(x)
        arr2.append(y)
        y=2*x - (45/(x**2))
        x=x+h
        i=i+1 
    return arr1,arr2 

    
    
#main function 

#CASE-1 h=0.2, N=10

print("For h=0.2, N=10 ")
arr1,arr2=library.Euler(f_1,0.2,2,2.71828,10)  #Call function 1 and compute the data points
print("Tabular representation of x vs y for function 1 through Euler's method")
for n, v in zip(arr1, arr2):        #Table for function 1
        print("{} |---> {}".format(n, v))
print(" ")
        
arr11,arr12=fxn1(2,2.71828)         #Compute the analytical solution
print("Tabular representation of x vs y for function 1 through analytical method")
for n, v in zip(arr11, arr12):      #table for analytical solution        
        print("{} |---> {}".format(n, v))

print(" ")       
arr3,arr4=library.Euler(f_2,0.2,3,1,10)        #Call function 2 and compute the data points
print("Tabular representation of x vs y for function 2 through Euler's method")
for n, v in zip(arr3, arr4):        #table for function 2 
        print("{} |---> {}".format(n, v))

print(" ")        
arr21,arr22=fxn2(3,1)               #Compute the analytical solution
print("Tabular representation of x vs y for function 1 through Analytical method")
for n, v in zip(arr21, arr22):      #table for analytical solution       
        print("{} |---> {}".format(n, v))
        
        
#CASE-2 h=0.2, N=50

print("For h=0.2, N=10 ")
arr1,arr2=library.Euler(f_1,0.2,2,2.71828,50)  #Call function 1 and compute the data points
print("Tabular representation of x vs y for function 1 through Euler's method")
for n, v in zip(arr1, arr2):        #Table for function 1
        print("{} |---> {}".format(n, v))
print(" ")
        
arr11,arr12=fxn1(2,2.71828)         #Compute the analytical solution
print("Tabular representation of x vs y for function 1 through analytical method")
for n, v in zip(arr11, arr12):      #table for analytical solution        
        print("{} |---> {}".format(n, v))

print(" ")       
arr3,arr4=library.Euler(f_2,0.2,3,1,50)        #Call function 2 and compute the data points
print("Tabular representation of x vs y for function 2 through Euler's method")
for n, v in zip(arr3, arr4):        #table for function 2 
        print("{} |---> {}".format(n, v))

print(" ")        
arr21,arr22=fxn2(3,1)               #Compute the analytical solution
print("Tabular representation of x vs y for function 1 through Analytical method")
for n, v in zip(arr21, arr22):      #table for analytical solution       
        print("{} |---> {}".format(n, v))
        
        
#CASE-3 h=0.05, N=10

print("For h=0.2, N=10 ")
arr1,arr2=library.Euler(f_1,0.05,2,2.71828,10)  #Call function 1 and compute the data points
print("Tabular representation of x vs y for function 1 through Euler's method")
for n, v in zip(arr1, arr2):        #Table for function 1
        print("{} |---> {}".format(n, v))
print(" ")
        
arr11,arr12=fxn1(2,2.71828)         #Compute the analytical solution
print("Tabular representation of x vs y for function 1 through analytical method")
for n, v in zip(arr11, arr12):      #table for analytical solution        
        print("{} |---> {}".format(n, v))

print(" ")       
arr3,arr4=library.Euler(f_2,0.05,3,1,10)        #Call function 2 and compute the data points
print("Tabular representation of x vs y for function 2 through Euler's method")
for n, v in zip(arr3, arr4):        #table for function 2 
        print("{} |---> {}".format(n, v))

print(" ")        
arr21,arr22=fxn2(3,1)               #Compute the analytical solution
print("Tabular representation of x vs y for function 1 through Analytical method")
for n, v in zip(arr21, arr22):      #table for analytical solution       
        print("{} |---> {}".format(n, v))
        
        
#CASE-4 h=0.5, N=10

print("For h=0.2, N=10 ")
arr1,arr2=library.Euler(f_1,0.5,2,2.71828,10)  #Call function 1 and compute the data points
print("Tabular representation of x vs y for function 1 through Euler's method")
for n, v in zip(arr1, arr2):        #Table for function 1
        print("{} |---> {}".format(n, v))
print(" ")
        
arr11,arr12=fxn1(2,2.71828)         #Compute the analytical solution
print("Tabular representation of x vs y for function 1 through analytical method")
for n, v in zip(arr11, arr12):      #table for analytical solution        
        print("{} |---> {}".format(n, v))

print(" ")       
arr3,arr4=library.Euler(f_2,0.5,3,1,10)        #Call function 2 and compute the data points
print("Tabular representation of x vs y for function 2 through Euler's method")
for n, v in zip(arr3, arr4):        #table for function 2 
        print("{} |---> {}".format(n, v))

print(" ")        
arr21,arr22=fxn2(3,1)               #Compute the analytical solution
print("Tabular representation of x vs y for function 1 through Analytical method")
for n, v in zip(arr21, arr22):      #table for analytical solution       
        print("{} |---> {}".format(n, v))