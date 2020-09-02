my_list = []


text = 5

for i in range(1,text+1):
    my_list.append(i)

print(str(my_list).replace("[","").replace("]","").replace(",",""))

def nextPermutation(my_list):
    for i in range(len(my_list)-1,0,-1):
        if my_list[i-1] < my_list[i]:
            if i - 1 >= 0:
                for j in range(len(my_list)-1,0,-1):
                    if my_list[j] > my_list[i-1]:
                        if j >= i:
                            spare = my_list[j]
                            my_list[j] = my_list[i-1]
                            my_list[i-1] = spare
                            my_list = my_list[:i] + my_list[i:][::-1]
                            return(my_list)
            else:
                return(None)
total = 0
while my_list != None:
    my_list = nextPermutation(my_list)
    total += 1
    print(str(my_list).replace("[","").replace("]","").replace(",",""))
print(total)
