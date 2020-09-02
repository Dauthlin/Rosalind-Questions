n = 6
k = 3
total_dead = 0
loop_depth = 0
live = []


        
def Fibonacci(n,life): 
   
    if n==1:  
        return 1
    elif n==2:
        return 2
    else:
        return Fibonacci(n-1)+Fibonacci(n-2) 
  

print(Fibonacci(n))



# for i in range(n-1):
#     live.append(Fibonacci(i+1))

# for i in range(k):
#     total_dead = total_dead + live[i]
# print(live)

# total = live[n-2]
# print(total-total_dead)


