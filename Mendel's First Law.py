
pop = "18 21 18".split(" ")

def sum_array(arr):
    total = 0
    for i in arr:
        total += int(i)
     
    return(total)


total = sum_array(pop)
kper = int(pop[0])/total
mper = int(pop[1])/total
nper = int(pop[2])/total
kper2 = max((int(pop[0])-1),0)/(total-1)
mper2 = max((int(pop[1])-1),0)/(total-1)
nper2 = max((int(pop[2])-1),0)/(total-1) 
kper3 =  int(pop[0])/(total-1)
mper3 = int(pop[1])/(total-1)
nper3 = int(pop[2])/(total-1)




kk = kper * kper2
mm = mper * mper2
nn = nper * nper2

km = kper * mper3 
mk = mper * kper3

kn = kper * nper3 
nk = nper * kper3

mn = mper * nper3 
nm = nper * mper3


print(kk+km+kn+mk+nk+(mm)*.75+(mn+nm)*.5)

