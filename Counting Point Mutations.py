text1 = "TACGCAACCCAATTGTCAGCCGTAAGGGTAACATGGGCATGACTCACACGACCACATCGCAACGATGTCGCGTCATGTCCAATTTAGCATAAAGTTAGGACCGTAGTGTCTCTCTTAAACCCGTTATCGGAAACCCCCTCTCGCGAGATGGGAAGACGGGTCCTGTAGGTTGTCAAAGAATCATTGCGGACCCGGGAAGTCGTTTATTGCGAGCCATCCGTCTTTTCGTTCAACAGCAGTATTATATCAGGCGTTGTCGGCCTTCGAACATGCATCGCCTTTGAGGCCGCAGGGGTGAAAAGTCCGCCGCGAGCTACCCTCCAGCAGTGTCATTTACTAACACCTTGACCCTTAGACGCCTTAGGTCCGGCGTAGTCGGCGAGCTCTGTCTTTGAACGCAGCTATTACTACCCAGACTTAGTTGAGGACGCATAGCCCCGACACTGTGATCTTCATGCGCAAAGACGTCACTGGAGTTACATGCAATAAGAAGAAAAAAATCTACGATGAAATACCGACTATTTTTCATTTGCCAGGACAAGTCATAACTACTGTAAGGAATTGAGCGCGTTGAACGTTAATCGATTGCCCCTTCCTTCCGGCGTCTCTTGCTACCGGCACACGCGTACCGCCGTCTACCTAGAGGTGAACAGGTCAGAAATAGGTTGGTTAAGTGTAGGTCCACCAAAGCATTAGTTCGCTCGTAGCGACCCGGACGATAAGCATAAAGGTACCCGAAGAATTGCAATAAGAGCCTTGCGGCCATGGGCGCCTGTTAATAAACACCTGAGCGGCCGCGTAGCACATTGTATGTATATGCTGCGCTTTCATGCGGCGTACTGGTGTACAATTGCCAGTTCATTGCGCAACAACTCCGAGATTATTGGTAGGATATTGTCTCCATAAGAATTAAGCTTGATCAGTCTC"
text2 = "AGATGATTGCCTGAGGAGGATGTAGGGGTAACGTGGGGTCGAGTAATACGCCCGTGCAGCAAGGTCATATGCTGCCTTAGAGTTGCGTTTGAAAAGAGGCCCGGATAGTCTACTGGGAACCGGCCTTCGGAACCCCACTCTCGTCAAGCATAGCCACCTGTGCTTCAGGCTAATATATAGCCCCTTCCGAACAGAGAAAGAGTCTTTACCGGCCGATGGACGTTACATTTCGTCAGCGGTGGCATACACTCTCACGTCGTGCTTGGAGCCTGCTGCCACTTTCTAGACGGGGATCTCCCAGCATCGGCAGTATGTCTTAACCGCTCTCGCTATTTGCTGCCCCCCAGACCGATTCACTGTTAGAGGACGGTTTAGTAAGCACGCTCACTCACTGTCCTTATCAATATTTGTTCCGTTACTGTTTAGAACTTCGAAACCCGGCACGGGGATCCGAACCAGTAAATACCTTAATCTTAATACATTGAACAATAAGTTTACAATCTCCTTTGTAACAGAGACGAATTGAATTGCGCCAAGGGTAGGCATAACTGAAGGGCCGATCGGACCACATAAAAAGTTCAGGCTTGGCTGTAGTCTGCCGGAATTACGTCCTGGAACCACCCGCGATGGGCCTAATCGATTTGGACGGACTGGCTTCGCATAGCTATGTGCACTCGGTGTCCTCCAGCTCCAATGGTAACGGGCTGAGGCGTAGATTAGAGCAATAATACGACGCCAGGGATAAAGCGAAGAGTCGAGTGACGAAGGATGCCTGTTAGTTATTTCCTGAGCGGTTGCAACGCCCTTTGATAGCATCTTCGGGGCATTCATCGCGGTCACTAGCGTACAATTGCAAGTTCTTTGTCCAGTTAGATGCTTAGTACTGAGTGCAACTGCCCACATCACGATATGACAGGGATCCGTCTG"
total = 0

for x,y in zip(text1,text2):
    if x != y:
        total += 1
print(total)
