#ODE solution using Dirichlet Boundary condition, RK4 method 
import library

def f1(x,y,p):                              #dy/dx=f1(x,y,p), p=dy/dx
    return p 
    
    
def f2(x,y,p):                              #dp/dx=p+1
    return p+1 
    

#Dirichlet Boundary 
def Dirichlet(x0,y0,p0,f1,f2,h,n):         #p0 is the guess of the slope
    x=x0
    y=y0
    p=p0
    i=0
    while i<=10:                            #Call RK4 from library
        arr1,arr2=library.RungeKutta_4(x0,y0,p0,f1,f2,h,n)
        i=i+1 
    return arr1,arr2
        
        
#Main function

#CASE-1 h=0.02, n=10 

print(" For h=0.02, N=10 ")
g1=input("Please enter your first guess (around 10) : ")
g1=int(g1)
arr10a,arr10b=Dirichlet(0,1,g1,f1,f2,0.02,10)       #first guess, given y(0)=1
print(arr10b[4])
r1=arr10b[4]
g2=input("Please enter your second guess (around 30) : ")
g2=int(g2)
arr10c,arr10d=Dirichlet(0,1,g2,f1,f2,0.02,10)       #second guess,  given y(0)=1 
print(arr10d[4])
r2=arr10d[4]
if r2>=3.43656 and r1<=3.43656:
    x = g1 + ((g2 - g1)/(r2 - r1)) * (3.43656 - r1) #lagrange's Interpolation, y(1)=3.43656
    arrf1,arrf2=Dirichlet(0,1,x,f1,f2,0.02,10)
    print('The value of the function at x=1 is ')
    print(arrf2[4])                                 #Calculate y value at the other boundary to check
    '''for n in (arrf1):            
        print("{}".format(n))
    for v in (arrf2):            
        print("{}".format(v))'''
elif r2<=3.43656 and r1>=3.43656:
    x = g1 + ((g2 - g1)/(r2 - r1)) * (3.43656 - r1)
    arrf1,arrf2=Dirichlet(0,1,x,f1,f2,0.02,10)
    print('The value of the function at x=1 is')
    print(arrf2[4])
    '''for n in (arrf1):            
        print("{}".format(n))
    for v in (arrf2):            
        print("{}".format(v))'''
else:
    print("Please enter some other value of secong guess and start again ")

    
#CASE-2 h=0.02, n=100

print(" For h=0.02, N=100 ")
g1=input("Please enter your first guess (around 10): ")
g1=int(g1)
arr10a,arr10b=Dirichlet(0,1,g1,f1,f2,0.02,100)       #first guess
print(arr10b[4])
r1=arr10b[4]
g2=input("Please enter your second guess (around 40) : ")
g2=int(g2)
arr10c,arr10d=Dirichlet(0,1,g2,f1,f2,0.02,100)       #second guess
print(arr10d[4])
r2=arr10d[4]
if r2>=3.43656 and r1<=3.43656:
    x = g1 + ((g2 - g1)/(r2 - r1)) * (3.43656 - r1)
    arrf1,arrf2=Dirichlet(0,1,x,f1,f2,0.02,100)
    print('The value of the function at x=1 is')
    print(arrf2[4])
    '''for n in (arrf1):            
        print("{}".format(n))
    for v in (arrf2):            
        print("{}".format(v))'''
elif r2<=3.43656 and r1>=3.43656:
    x = g1 + ((g2 - g1)/(r2 - r1)) * (3.43656 - r1)
    arrf1,arrf2=Dirichlet(0,1,x,f1,f2,0.02,100)
    print('The value of the function at x=1 is')
    print(arrf2[4])
    '''for n in (arrf1):            
        print("{}".format(n))
    for v in (arrf2):            
        print("{}".format(v))'''
else:
    print("Please enter some other value of secong guess and start again ")


    
#CASE-3 h=0.2, n=200

print(" For h=0.2, N=200 ")
g1=input("Please enter your first guess (around 10): ")
g1=int(g1)
arr10a,arr10b=Dirichlet(0,1,g1,f1,f2,0.2,200)       #first guess
print(arr10b[4])
r1=arr10b[4]
g2=input("Please enter your second guess (around -5) : ")
g2=int(g2)
arr10c,arr10d=Dirichlet(0,1,g2,f1,f2,0.2,200)       #second guess
print(arr10d[4])
r2=arr10d[4]
if r2>=3.43656 and r1<=3.43656:
    x = g1 + ((g2 - g1)/(r2 - r1)) * (3.43656 - r1)
    arrf1,arrf2=Dirichlet(0,1,x,f1,f2,0.2,200)
    print('The value of the function at x=1 is')
    print(arrf2[4])
    '''for n in (arrf1):            
        print("{}".format(n))
    for v in (arrf2):            
        print("{}".format(v))'''
elif r2<=3.43656 and r1>=3.43656:
    x = g1 + ((g2 - g1)/(r2 - r1)) * (3.43656 - r1)
    arrf1,arrf2=Dirichlet(0,1,x,f1,f2,0.2,200)
    print('The value of the function at x=1 is')
    print(arrf2[4])
    '''for n in (arrf1):            
        print("{}".format(n))
    for v in (arrf2):            
        print("{}".format(v))'''
else:
    print("Please enter some other value of secong guess and start again ")

    

#CASE-4 h=0.5, n=10 

print(" For h=0.5, N=10 ")
g1=input("Please enter your first guess (around 10): ")
g1=int(g1)
arr10a,arr10b=Dirichlet(0,1,g1,f1,f2,0.5,10)       #first guess
print(arr10b[4])
r1=arr10b[4]
g2=input("Please enter your second guess (around -10) : ")
g2=int(g2)
arr10c,arr10d=Dirichlet(0,1,g2,f1,f2,0.5,10)       #second guess
print(arr10d[4])
r2=arr10d[4]
if r2>=3.43656 and r1<=3.43656:
    x = g1 + ((g2 - g1)/(r2 - r1)) * (3.43656 - r1)
    arrf1,arrf2=Dirichlet(0,1,x,f1,f2,0.5,10)
    print('The value of the function at x=1 is')
    print(arrf2[4])
    '''for n in (arrf1):            
        print("{}".format(n))
    for v in (arrf2):            
        print("{}".format(v))'''
elif r2<=3.43656 and r1>=3.43656:
    x = g1 + ((g2 - g1)/(r2 - r1)) * (3.43656 - r1)
    arrf1,arrf2=Dirichlet(0,1,x,f1,f2,0.5,10)
    print('The value of the function at x=1 is')
    print(arrf2[4])
    '''for n in (arrf1):            
        print("{}".format(n))
    for v in (arrf2):            
        print("{}".format(v))'''
else:
    print("Please enter some other value of secong guess and start again ")

    
    



''' 
For h=0.02, N=10 
Please enter your first guess (around 10) : 10
1.8345847314416226
Please enter your second guess (around 30) : 30
3.4974660613354818
The value of the function at x=1 is 
3.43656
 For h=0.02, N=100 
Please enter your first guess (around 10): 10
1.8345847314416226
Please enter your second guess (around 40) : 40
4.328906726282411
The value of the function at x=1 is
3.43656
 For h=0.2, N=200 
Please enter your first guess (around 10): 10
13.385435349559266
Please enter your second guess (around -5) : -5
-4.5947037634760965
The value of the function at x=1 is
3.436560000000001
 For h=0.5, N=10 
Please enter your first guess (around 10): 10
63.96704104798846
Please enter your second guess (around -10) : -10
-54.15485176653601
The value of the function at x=1 is
3.436560000000004



'''
        
    
    

    
    
    
    
    
    
    
    