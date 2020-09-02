codon_dic = {
    "TTT": "F",      
    "CTT": "L",      
    "ATT": "I",      
    "GTT": "V",
    "TTC": "F",      
    "CTC": "L",      
    "ATC": "I",      
    "GTC": "V",
    "TTA": "L",      
    "CTA": "L",      
    "ATA": "I",      
    "GTA": "V",
    "TTG": "L",      
    "CTG": "L",      
    "ATG": "M",      
    "GTG": "V",
    "TCT": "S",      
    "CCT": "P",      
    "ACT": "T",      
    "GCT": "A",
    "TCC": "S",      
    "CCC": "P",      
    "ACC": "T",      
    "GCC": "A",
    "TCA": "S",      
    "CCA": "P",      
    "ACA": "T",      
    "GCA": "A",
    "TCG": "S",      
    "CCG": "P",      
    "ACG": "T",      
    "GCG": "A",
    "TAT": "Y",      
    "CAT": "H",      
    "AAT": "N",      
    "GAT": "D",
    "TAC": "Y",      
    "CAC": "H",      
    "AAC": "N",      
    "GAC": "D",
    "TAA": "Stop",   
    "CAA": "Q",      
    "AAA": "K",      
    "GAA": "E",
    "TAG": "Stop",   
    "CAG": "Q",      
    "AAG": "K",      
    "GAG": "E",
    "TGT": "C",      
    "CGT": "R",      
    "AGT": "S",      
    "GGT": "G",
    "TGC": "C",      
    "CGC": "R",      
    "AGC": "S",      
    "GGC": "G",
    "TGA": "Stop",   
    "CGA": "R",      
    "AGA": "R",      
    "GGA": "G",
    "TGG": "W",      
    "CGG": "R",      
    "AGG": "R",      
    "GGG": "G", 
}





#M is the start codon, ATG
text = """
>Rosalind_8755
CGGAGCAACCATATCACATTCCGTGACGGGCCACACTTACCCCCTTGACAACGCCATAAG
GACGGCCACTGGGAGGCAACGTGTTGACGCTAGCCGCGACCATGGCGACCGTTTTTATGC
CTGCTCTGACTACATCGCCTGCTACGTCATGCATGGGGTCGTTCTCGATGATTCTCATCC
TATCCAGTTTCCGAGTGTGCCAAGATAAGGGTGTACAAGCTCGCAGCACCGAGGGGGTAC
TAGAGCCGACGCTTTCATTGAGCGTAGACCTCTGTTCTTCCATAGTCCCGAATGTGGGGG
ACCGCCTCGGCAGGTGACTCTTGCAGCCTAAGGCTACTACAGTATGCCTCAGCGCCCACG
ACGCCAGTGAGTTATGTGCAGTCGCACTATCTTGGGATCATACAGGTACCAGTCTCGTAC
CTTGGCGCGCTCGCAGAGATTTCCGATGCCAATTACGGTTGATGTAGTAAAAGCTTAGCT
AAGCTTTTACTACATCAACCGTAATTGGCATGATCAAGCCTGTCTATCCAAGTGCCGGTA
CCAAATACACACCGCCTTTGGGGTCATACACGTAGACATCTTAAATCTATATGAAAGTTC
CCCGAACGATGTAACGCACATCTTTAGAACTGCCTATGGTGCAGGGATGCGCATACTAAT
ACTTTTTGGACAAAGCTGTTTCATCATGGTGTGCCTACGTCCCGTGGTCGGCGAGAATCT
CGTCTCTTCATACCAAGTGCAAGGGCTCTAGCAAGTAGTTCTGAAATGGATCATGGGTAA
ATGGTAGCACTTTGTTAGACGTGGCACTCTCATGGACCAGTGGACACGGTTATTCCCGCC
TAATGACACACCTACGAAATGGTCCCGCTGTAGGAAGATCCCCTCATGAGCGTAATTAAA
GGCTGGAACTGAGGCGAACACATACTAACTGTAACGTCAGTTATATATCAGCATTA
"""

array_of_ros = text.split(">")[1:]
array_of_ros_split = []
data = []
for i in range(len(array_of_ros)):
    array_of_ros[i] = (array_of_ros[i].split("\n"))

for i in range(len(array_of_ros)):
    count = 0
    store = ""
    for j in range(len(array_of_ros[i])):
        count += 1
        if count != 1:
            store += array_of_ros[i][j]
    data.append(store)




text_reverse = text[::-1]
text_reverse_result = ""
for i in text_reverse:
    if i == "A":
        text_reverse_result = text_reverse_result + "T"
    if i == "T":
        text_reverse_result = text_reverse_result + "A"
    if i == "C":
        text_reverse_result = text_reverse_result + "G"
    if i == "G":
        text_reverse_result = text_reverse_result + "C"

output_array = []
data.append(text_reverse_result)
for k in data:
    for i in range(len(k)):
        tally = 2
        store = ""
        if k[i:i+3] == "ATG":
            #print(range(i,len(k)))
            for j in range(i,len(k)):
                #print(i,j)
                tally += 1
                store = store + k[j]
                if tally == 3:
                    tally = 0
                    if (k[j:j+3] == "TGA") or (k[j:j+3] == "TAG") or (k[j:j+3] == "TAA"): 
                        #print(store, "                 ",k)
                        output_array.append(store)
                        break

protein_array = []
for j in output_array:
    array = []
    tally = 0
    store = ""
    for i in j:
        tally += 1
        store = store + i
        if tally == 3:
            tally = 0
            array.append(store)
            store = ""
    store = ""
    for i in array:
        if codon_dic[i] != "Stop":
            store = store + codon_dic[i]
    protein_array.append(store)  

#print(protein_array)

protein_array_unique = []
for i in protein_array:
    if i not in protein_array_unique:
        protein_array_unique.append(i)
output = ""
for i in protein_array_unique:
    output += i + "\n"
print(output)
