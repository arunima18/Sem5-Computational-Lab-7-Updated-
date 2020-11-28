import math
import random


# First Derivative of a Function
def d1(f, x):
    h = 10 ** (-5)
    return (f(x + h) - f(x - h)) / (2 * h)


#partial pivoting
def partial_pivot(Mat1,n,Mat2):
    
    i=0
    j=0
    while i<=(n-1):
        if Mat1[i][i]==0:
            j=i
            
            while j <= n:
                
                if Mat1[j+1][i]!=0:
                    Mat2[j]=Mat1[j+1]
                    Mat1[j+1]=Mat1[i]
                    Mat1[i]=Mat2[j]
                    j=(n+2)
                else:
                    j=j+1
        i=i+1
    return Mat1 
   
   
   
#crout's method
def crout(MatA):
    i=0
    j=0
    k=0
    sum1=0
    sum2=0
    U=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    L=[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
    
    while j<=3:
        
        i=0
        while i<=3:
            sum1=0
            sum2=0
            k=0
            if i ==0:
                U[i][j]=MatA[i][j]
                i=i+1
                
            elif i>j:
                #if k<=(j-1):
                while k<=(j-1):
                    sum1=sum1-(L[i][k]*U[k][j])/U[j][j]
                        #L[i][j]=(MatA[i][j]-L[i][k]*U[k][j])/U[j][j]
                    k=k+1
                L[i][j]=(MatA[i][j]/U[j][j])+sum1
                
                   
                #else:
                 #   L[i][j]=MatA[i][j]/U[j][j]
                i=i+1
            elif i<=j and i !=0:
               
                while k<=(i-1):
                    sum2=sum2-(L[i][k]*U[k][j])
                   
                        #L[i][j]=(MatA[i][j]-L[i][k]*U[k][j])/U[j][j]
                    k=k+1
                U[i][j]=(MatA[i][j])+sum2
                
                i=i+1
                   
               
        j=j+1
    return L ,U 
    
    
    
#Solution for Ly=b: forward substituion 
def forward_sub(L,y,b):
    i=0
    j=0
    
    sumf=0
    while i<=3:
        j=0
        sumf=0
        while j<=(i-1):
            sumf=sumf-L[i][j]*y[j]
            j=j+1 
        y[i]=b[i]+sumf 
        #print('***')
        #print(y[i])
        #print('***')
        i=i+1 
        
    return y 
            
        
    
#Solution for Ux=y:backward substitution 
def backward_sub(U,x,y,n):
    i=2 
    j=0
    sumb=0
    while i>=(-1):
        sumb=0
        j=i+1 
        while j<=(n-1):
            sumb=sumb-(U[i+1][j+1]*x[j+1])/U[i+1][i+1]
            j=j+1 
        x[i+1]=(y[i+1]/U[i+1][i+1]) + sumb
        
        i=i-1 
    return x 
    

#matrix multiplication    
def multi(Mat1,Mat2,arr,n):
    i=0
    k=0
    j=0
    sum=0
    #arr=[[0,0,0],[0,0,0],[0,0,0]]
    while i<=n:
        j=0
        while j<=n:
            k=0
            sum=0
            while k<=n:
                sum=sum+ Mat1[i][k]*Mat2[k][j]
                k=k+1
                arr[i][j]=sum
            j=j+1
        i=i+1
    return arr    


#Rectangle method for integration
def Rect_(a,b,f,N):
    i=1
    x=0
    y=0
    sum1=0
    h=(b-a)/N
    while i<=N:
        
        x=a+((2*i-1)*(h/2))
        y=f(x)
        sum1=sum1+(h*y) 
        #print(sum1)
        i=i+1 
    return sum1 
    
    
    
def trapezium(a,b,f,N):
    # f = integrand, lowr_lim = lower limit, uppr_lim = upper limit, N = no. of partitions

    
    sum2 = 0

    h = (b - a) / N

    for i in range(1, N):
        
        sum2 = sum2 + h * f(a + i * h)
        #print(h/2 * (f(a) + f(b)) + sum2)

    return h/2 * (f(a) + f(b)) + sum2
    
    
#Simpson's Method 
def simpson(a,b,f,N):
    h = (b - a) / N
    sum3 = 0
    x = a + h
    for i in range(1, int(N / 2) + 1):
        
        
        sum3 += 4 * f(x)
        #print(h/3 * (f(a) + f(b) + sum3))
        x += 2 * h
    x = a + 2 * h
    for i in range(1, int(N / 2)):
        
        
        sum3 += 2 * f(x)
        #print(h/3 * (f(a) + f(b) + sum3))
        x += 2 * h

    return h/3 * (f(a) + f(b) + sum3)
    

#Monte Carlo method
def montecarlo(f,a,b,N):
    x=[]
    sum=0.0

    for i in range(N):
        n=random.random()       #random number in the range (0,1)
        r=a+((b-a)*n)           #random number in range (a,b)
        x.append(r)

    for i in range(N):
        sum+=f(x[i])

    value=((b-a)*sum)/N

    return value
    

#Euler's method for solving D.E    
def Euler(f,h,x_0,y_0,n):
    y=y_0
    x=x_0
    i=1 
    arr1=[x_0]
    arr2=[y_0]
    while i<=n:
        y=y+(h*f(x,y))
        x=x+h
        arr1.append(x)
        arr2.append(y)
        i=i+1 
    return arr1,arr2
    

#Runge Kutta-4 Method for solving DE- second order   
def RungeKutta_4(x0,y0,p0,f1,f2,h,n):
    x=x0 
    y=y0 
    p=p0
    arr1=[]
    arr2=[]
    i=0
    while i<=n:
        K1y=f1(x,y,p)
        K1p=f2(x,y,p)
        K2y=f1((x + (h/2)),(y + h * (K1y/2)),(p + h * (K1p/2)))
        K2p=f2((x + (h/2)),(y + h * (K1y/2)),(p + h * (K1p/2)))
        K3y=f1((x + (h/2)),(y + h * (K2y/2)),(p + h * (K2p/2)))
        K3p=f2((x + (h/2)),(y + h * (K2y/2)),(p + h * (K2p/2)))
        K4y=f1((x + (h/2)),(y + h * (K3y/2)),(p + h * (K3p/2)))
        K4p=f2((x + (h/2)),(y + h * (K3y/2)),(p + h * (K3p/2)))
        arr2.append(y)
        y=y + h/6 * (K1y + 2 * K2y + 2 * K3y + K4y)
        p=p + h/6 * (K1p + 2 * K2p + 2 * K3p + K4p)
        arr1.append(x)
        x=x+h
        i=i+1 
    return arr1,arr2 
    