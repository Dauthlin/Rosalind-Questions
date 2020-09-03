text = """
>Rosalind_5382
GCGCGTGTCTCCTCCCGCTTGAAAAAGGTTGGCTGCGTAATCAATAGGGAGGCACCATGG
TACGAACTGCCCTAACGACAACTCGGCGGCTCCGATCTACTTACTAAACGTTTTTGCCTT
ATATAGATGAAAGGACTAATTCTAGCCGAGTCCCGTAAATACGGAGGAGTTCGGAGCCGA
CCAGGGGCGACCGCACCGTGCATCCGCACCTGGTGGTACCTATCGGCTCCTGGGTATGGA
GAGAGTAAATGTGAGGACTCGAGGGATTTCGTCTTCATCAATTTTTTGCTATGACCGTAT
AGAGCTAAATCCCGTATATCTTGCTAGGGGAGGCTATCGAAGGGCGAACTGTACTTCCTG
TGCGGTAGTCGAATACCGAAATCCCATCGACTTCGATCACCACAGCGTATTTATGCATCC
TGCGCGCTTCATCATCTGCTTGACCTCAACTGATAGCAACAGACATATACGGTAAGTCCC
AATCGCTCACTGACAAGCGCGCGCTTAAAAGGGGTAAAAGTAGGTGCCGATGTAAGTATC
CGTTCGAGTCTCAGGCTGCCTTGGAATAGCTGGTAACGGCGCTCCCAGTGTAAGGAGGCG
TATATTTAGACTGACATGCCTCTTTGTTGCTGACTCATCTGACAGACTTGAGCATAGGAT
GGTGTAGTCTAACATCTGAGTGTGCTCGTTAAGTCATCCCAATACATTTGAGAATCGATA
GCACTCCAGTCTCTCGGTCGGAAGTTCCGTCTCACCTTAGGTTTTTTTGTGCTGTAGTTC
GAAAACAAGACCGAGTTGCCTGTTGACCTCGGCCTGATAGGCCATATGACGAGGGCGGCA
CTATACTCCGCAAAGCCGAAATTACTAAAGACAATGAAGTGGCCAGCGGCAGGGTCCAAA
CGGGCTATATAGGCAGTAGTGCGGCCTACAATCGTCCTCTCATGTATAATCCCCCCCTCC
AAAGGGTACCCGAGACCGTAATGCTGAAAGGCCTCAGCGC
"""


array_of_ros = text.split(">")[1:]
array_of_ros_split = []

for i in range(len(array_of_ros)):
    array_of_ros[i] = (array_of_ros[i].split("\n"))

for i in range(len(array_of_ros)):
    count = 0
    store = ""
    for j in range(len(array_of_ros[i])):
        count += 1
        if count != 1:
            store += array_of_ros[i][j]
    

text = store
def reverse_complement(text):
    text_reverse = text[::-1]
    output = ""
    for i in text_reverse:
        if i == "A":
            output = output + "T"
        if i == "T":
            output = output + "A"
        if i == "C":
            output = output + "G"
        if i == "G":
            output = output + "C"
    return(output)


output = ""
for i in range(len(text)):
    for j in range(4,13,+2):
        if text[i:i+j] == reverse_complement(text[i:i+j]):
            if len(text[:i])+j <= len(text):
                output += str(i+1) +" "+ str(j) + "\n"


print(output)

   