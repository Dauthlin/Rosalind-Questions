n = 33
k = 3



        
def Fibonacci(n): 
    if n==1: 
        return 1
    elif n==2: 
        return k +1 
    else: 
        return (Fibonacci(n-1)+Fibonacci(n-2)*k)


print(Fibonacci(n-1))


