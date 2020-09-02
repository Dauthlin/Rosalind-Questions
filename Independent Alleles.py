k = 2 #generation number
n = 1 #prob of that number of AaBb at that generation

#0 aAbB_per = 100	
#1 AAbB_per = 0		
#2 aABB_per = 0		
#3 aAbb_per = 0		
#4 aabB_per = 0		
#5 AABB_per = 0	
#6 AAbb_per = 0	
#7 aaBB_per = 0	
#8 aabb_per = 0	
#9 AABb_per = 0
genes_current = [1,0,0,0,0,0,0,0,0,0,0,0,0]



ex0 = [.25,.125,.125,.125,.125,.063,.063,.063,.063]
# aAbB = {
# "aAbB"	:	25,
# "AAbB"	:	12.5,
# "aABB"	:	12.5,
# "aAbb"	:	12.5,
# "aabB"	:	12.5,
# "AABB"	:	6.3,
# "AAbb"	:	6.3,
# "aaBB"	:	6.3,
# "aabb"	:	6.3,
# }
ex1 = [.25,.25,.25,.25]
# AABB = {
# "AABB"5	:	25,
# "AAbB"1	:	25,
# "aABB"2	:	25,
# "aAbB"0	:	25,   
# }
ex2 = [.25,.25,.125,.125,.125,.125,.125]
# _totalAAbB = {
# "AAbB"1	:	25,
# "aAbB"0	:	25,
# "AABB"5	:	12.5,
# "aABB"2	:	12.5,
# "AAbb"6	:	12.5,
# "aAbb"3	:	12.5,
# }

# AAbb = {
# "AABb"9	:	25,
# "AAbb"6	:	25,
# "aABb"10	:	25,
# "aAbb"3	:	25,   
# }

# AaBB = {
# "aABB"2	:	25,
# "aAbB"0	:	25,
# "AABB"5	:	12.5,
# "AAbB"1	:	12.5,
# "aaBB"7	:	12.5,
# "aabB"4	:	12.5,
# }

# Aabb = {
# "aABb"10	:	25,
# "aAbb"3	:	25,
# "AABb"9	:	12.5,
# "AAbb"6	:	12.5,
# "aaBb"14	:	12.5,
# "aabb"8	:	12.5,
# }

# aaBB = {
# "AaBB"11	:	25,
# "AabB"13	:	25,
# "aaBB"7	:	25,
# "aabB"4	:	25,
# }

# aaBb = {
# "AabB"13	:	25,
# "aabB"4	:	25,
# "AaBB"11	:	12.5,
# "aaBB"7	:	12.5,
# "Aabb"12	:	12.5,
# "aabb"8	:	12.5,
# }

# aabb = {
# "AaBb"15	:	25,
# "Aabb"12	:	25,
# "aaBb"14	:	25,
# "aabb"8	:	25,
# }

#9 ex2#1,0,5,2,6,3 


#10 ex0#13,11,4,12,1,7,8,5,6


#11 ex2#2,0,5,1,7,4


#12 ex2#10,3,9,6,14,8


#13 ex0#10,9,3,2,14,6,5,8,7


#14 ex2#13,4,11,7,12,8

#15 ex0#15,12,










for i in range(k):
    genes_nextyear = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    for gene_number in range(len(genes_current)):
        if gene_number == 0:
            genes_nextyear[0] += aAbB[0] * genes_current[0]
            genes_nextyear[1] += aAbB[1] * genes_current[1]
            genes_nextyear[2] += aAbB[2] * genes_current[2]
            genes_nextyear[3] += aAbB[3] * genes_current[3]
            genes_nextyear[4] += aAbB[4] * genes_current[4]
            genes_nextyear[5] += aAbB[5] * genes_current[5]
            genes_nextyear[6] += aAbB[6] * genes_current[6]
            genes_nextyear[7] += aAbB[7] * genes_current[7]
            genes_nextyear[8] += aAbB[8] * genes_current[8]   
        if gene_number == 1:
            genes_nextyear[5] += aAbB[0] * genes_current[5]    
            genes_nextyear[1] += aAbB[1] * genes_current[1]    
            genes_nextyear[2] += aAbB[2] * genes_current[2]    
            genes_nextyear[0] += aAbB[3] * genes_current[0]    
        if gene_number == 2:


        if gene_number == 3:
        if gene_number == 4:
        if gene_number == 5:
        if gene_number == 6:
        if gene_number == 7:
        if gene_number == 8:









# PAaBb = 1
# PAaAa = 0 
# PBbBb = 0

# for i in range(k):
#     AaBb = 0
#     AaAa = 0 
#     BbBb = 0
#     for j in range(PAaBb):
#         AaBb += 1
#         AaAa += .5
#         BbBb += .5
#     for j in range(PAaAa):
#         AaAa += 1
#         AaBb += 1
#     for j in range(PBbBb):
#         BbBb += 1 
#         AaBb += 1
#     PAaBb += AaBb
#     PAaAa += AaAa 
#     PBbBb += BbBb  

#print(PAaBb,PAaAa,PBbBb)

