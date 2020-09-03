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






text = """
>Rosalind_9045
ATGAAGGTTCAGACCCATGCATACGAGGCAGAGAATTCATCGTGTGGGGCAACAGTAAAG
ATACATTGCATACCATGGTCAAATAAACTCAGGTTTGGTCTATTACGGGCGGTCGAGATG
GAAAGTAGTTGCGCCCCATCCGCGATGGCGCAGTACGGATAATCTCCGGCTGCGGGTACC
ATTACTGGCAGGGTCGGGTCACGGATGATAGGGACCGTATCCACCTGCATCAACTATGAA
CGTGACACGTGCGGACACTAAATTGAAAACGACATCAGTCTCTCGCGGCGCGCCCTAACT
GGAGCCTATATCCGCGCCAATTCCTTTATTAGGCCAAATTTCTAATAATCCACTGTTGCA
TAAAATCCCAAGTTACACATAATGTGAAGCCATCGTTCAGTGTAGACTTAGGTACCACAT
TGGTACCTCTCTCTTACCTACAGCACGTCCCAAATGTCAGCTTGAAATTCTAAACGTATG
AGTTCAATGGACAGGCACCAAGCCCGTCTCGCAGGGCACGCTTGGACAATCATCCCGAGC
ATTAGATGCGCTGAACTACCACCATGTTCATAACCTTCCGCGAGATCGCGGAAAGATAGA
GGGGGTGCTGCAGACATCAGCAACTTACGGTACGTTCGAACTAGTCAGAAATGCGTTTAT
CCGTGCGATTTGTGGACCGAACCAGGCCGAACGTACGGATGAGCGCTCCGCCGGATGCAT
TTGGTAAGTTCGACTGGACTTACTAAACGACGCTAGGGTTGAGACGACAGATGCTACGGT
CTATAGTACGAGATAACACCGCTTCTCTCCTCTCGTTAAGCGCACGACTGACAGTTCAAT
TCGCCGGACAAGAAGGTTAAAGGCCCCGCTTCAGGGAGCTATTGTTTTGGGTATGGGGGA
TGGTGCTCTGCCCAAAGGGTTAACTCCAGCAGGGCCACAGTCCAAACCTAACGGTCCTGC
GATCGAAAATTTTAAGCAAGAAGAGTGTCATGTGA
>Rosalind_6975
AGTACGGATAAT
>Rosalind_5722
GAAGGTTAAAGGCCCCGCTTCA
>Rosalind_6613
CATGTTCATAACCTTCCGCGAGATCGCGGAAAGATAGAGGGGGTGCTGCA
>Rosalind_7535
CGAGATAACACCGCTTCTCTC
>Rosalind_3496
CGCTAGGGTTGAGACGACAG
>Rosalind_5345
ATCCCGAGCA
>Rosalind_8635
GGACACTAAATTGAAAACGA
>Rosalind_8409
TATGGGGGATGGTGCTCTGCCCAAAGGGTTAACTCCAGCAG
>Rosalind_4127
CCCAAATGTCAGCTTGAAATTCTAAACGTATGAGTTCAATGGACAGGCAC
>Rosalind_1022
GTAAAGATACATTGCATACCATGGTCAAATAAACTCAGGT
>Rosalind_9112
GCAGGGTCGGGTCACGGATGATAGGGACCGTATCCACCTGCATCAAC
>Rosalind_7857
CAGAAATGCGTTTATC
>Rosalind_4496
ACGGATGAGCGCTCCGC
>Rosalind_3030
GTGAAGCCATCGTTCAGTGT
>Rosalind_8827
GTCCTGCGATCGAAAATTTTA
>Rosalind_3104
GCGCGCCCTAACTGGAGCCTATATCCGCGCCAATTCCTTTATTAG
"""



def FASTA_just_data(text):
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
    return(data)

data = FASTA_just_data(text)
for i in data[1:]:
    data[0] = data[0].replace(i,"")


text = data[0]
array = []
tally = 0
store = ""
for i in text:
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
    
print(store)
