import itertools       

alphabet= "A B C D E F"
length = 3
alphabet = alphabet.split(" ")                                                   
permutation = itertools.product(alphabet, repeat=length)        
  
for i, j in enumerate(list(permutation)):  
    print(str(j).replace("(","").replace(")","").replace("'","").replace(",","").replace(" ",""))




