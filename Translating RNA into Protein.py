codon_dic = {
    "UUU": "F",      
    "CUU": "L",      
    "AUU": "I",      
    "GUU": "V",
    "UUC": "F",      
    "CUC": "L",      
    "AUC": "I",      
    "GUC": "V",
    "UUA": "L",      
    "CUA": "L",      
    "AUA": "I",      
    "GUA": "V",
    "UUG": "L",      
    "CUG": "L",      
    "AUG": "M",      
    "GUG": "V",
    "UCU": "S",      
    "CCU": "P",      
    "ACU": "T",      
    "GCU": "A",
    "UCC": "S",      
    "CCC": "P",      
    "ACC": "T",      
    "GCC": "A",
    "UCA": "S",      
    "CCA": "P",      
    "ACA": "T",      
    "GCA": "A",
    "UCG": "S",      
    "CCG": "P",      
    "ACG": "T",      
    "GCG": "A",
    "UAU": "Y",      
    "CAU": "H",      
    "AAU": "N",      
    "GAU": "D",
    "UAC": "Y",      
    "CAC": "H",      
    "AAC": "N",      
    "GAC": "D",
    "UAA": "Stop",   
    "CAA": "Q",      
    "AAA": "K",      
    "GAA": "E",
    "UAG": "Stop",   
    "CAG": "Q",      
    "AAG": "K",      
    "GAG": "E",
    "UGU": "C",      
    "CGU": "R",      
    "AGU": "S",      
    "GGU": "G",
    "UGC": "C",      
    "CGC": "R",      
    "AGC": "S",      
    "GGC": "G",
    "UGA": "Stop",   
    "CGA": "R",      
    "AGA": "R",      
    "GGA": "G",
    "UGG": "W",      
    "CGG": "R",      
    "AGG": "R",      
    "GGG": "G", 
}


text ="AUGUCCAGUCGUUACUAUUGCGCCCAAACACUGCCGAUGUGUCUUUUACGUAUCCGGUUGCCUAAUCUGAUCACUCACUGGGUUCCAUGGACCACACGCAAUGCACGAGCAGCACGGGUCGGAGGGGGAUUGGUUUGGUCUCAAUUAACAAAGCGUCCCUUUCUUUUAGACCCAAGAAGGACGGUAGGUGGGGCAGUUCAUUCCAUGGGAUGUCUGACCCGAAAUAUUUGGGGGCACCGAUCCCCAGAGUUCCCACCCGUUCGUAGCCAGCUGUACACCGCUGCUGGGUUUCCCUCAAUGUGGACUAGCUGGCUCAUCAACCAGAGUCUUUUUAACUCACAUACUCGAAACGUUCUCAUUCUCCCCGCCGUCAUCAGCGUAUUAGACGGAACCGCGAUGAUGGUCCACGAAGUAAGUUAUUCCAGCCAAGGCACAGCAUCGACAGUGGCGGGAGCUAGUAUAAAGGACAAGGGGCAGGCGAUGGUCUUCCGGCAGGUUCGUGAUAAGCAUAUGGGGCGACCCCCCGUAGCCAUUGGCACUGCGGGCGGUUAUUUGUGGGUGUCUGUUUUCGGAGUCUUAGAUGGCCUUGACAUUUCACUCGGCACCCGAGUGAGAAAUCAGUCAUUGUUUGUUGCAGGUCGGAAUCUCGUUACCAACAUUCCGCUUGCCUACCUUCCAGAAAACACGAUGAAGGCGGGCGGACCCGGGCAGGUUCCGAACUGCAUAUCGGAACCUCCCCAAUGUCCCUUGAAUAAUCUACAGAUUUAUUAUACCCUUUAUACUGAACCGGAACGAGCAUUGCCAAGGAAAAUCCUUACCUGGGACGGGGCGAUGGUUAGACGCUCGGUCGUAUAUCGGGCUACGAAUGCCUGGAACUGGUGUGACGUUUGCGCCCUGCGGUCCACGGCCCCAAUCUUAACCUUACCAAUGACACACUGGCUCAAACCCACGUGGGUUCCUCAAGAUUUUUUGAUCCACUCGAGUGGAUCUCAUGGACCAGCUGCUGAACUCAGGUGGAGUCGAUCACCAGCCCAGCCAGCUGAUGACCACGACCUAGACCUUGAAAGCUUCUCAUGUCCCGCCCAAGAGGGAAACGCCUAUCUAUGCGUACGUAAUGCACGUCAUCCGCAACACGUCGCAUUGACGUGCGCUCAGUAUAUCAUCCCGACGACUCCUAACCCGCCUAUCCUCAUUCGUUCUGCAAGGAGUACUGCGCGAAUUGAGUUCAGUCCUGAAGCGCAAUCGAUGUGCCCGCAGACAGACGCCUGCGACGCAGUUGGGGUCACUGAUCCAUGGCGGCGGUUUGCUAGACUCAAGCCAUGCAAUGAAUCGUCGUGGUCAACUCGGGUAGCCAAGUUUUUGCAGUUACAUGCUAAAGGUAGCUUAUCUCACGGAGUGGCAAAAUCCCAAUCGCCAAUCCUGUUGCGCAUCAGGACCAGAGUAUCAAAUUACGUCAUUAAGUUUGGAGUGCGAGACACGCCACGGCCGGCUGGCCUCGUCGUCCUCUCGCCGAAUUUCGCAUAUAGUGCGUCCGGACAAUCUGGCCAAUGCGCUCCUUUGAGGGGAGACAACAGGGUCUAUGAGAGCGUAAUGGGCUUAGCCCAAAUUAAACCGAGUGGACUCAUGUCCCCCAGUGGGUUGCCAGUGGUACAGCGAUUGACAAGUCCUAUAACAUGCAAGGCUCUUCAUGUCAGCGGGGAACCCGAACAAACGCCAGGUAAAGAUGUCAGACGAAAGCACUUUAAGUUUGUGCUCGCCAAGGGUACGCGGCUUUUUAAAGACGGGGUCUUCAUUCCUGAUCUUCGAAGUCCUGAAACGCAAUCAAAACUAUGUAAUCCACGAGCAAGACAUCCAAGGGCAAAAUGGCGCCUUACGCCACGGAGUCCCCGUAUAGACAGAGGAGCUACUGCCAAGCUGCCAUCGCGACGCCGCGUAUGGAUGCUCGUUUUGGGGGGGCUAUUAAUCAGCCCCGGAGCGGGUACCUAUGUCCGACACCCAAGGUGGCCAGCCACCCUUAUGCUGAGAGGCUCAGCGAGUUCUCCGAGCUGUUGGUGCAUAAUAACUACGCUGGCAGAGCUUGUAGUAGCGGCUGUAGGACGGUCUGCUAAUCCCACACAUUACAGUCAUACCAAAGGCUGCGCAGGGCCUGCUGAUGCCCACAUAAUCGCUGCUAAAUUACCCACAAGCACCUUUAGCCCACCGUCCCACCACCAACAUUCGUUCGUUCUCGCGCGAAGGGCUAUGCGCGCUCCUCAUUACCGAGCAUUCAGAAGGAGACAGGCGGGUUCUACCUCAACUCCCCCACUGUCGGCCCCCCCAGGCCAGGUAGGGGUGCAACAUAACGGCCAUGGUCCCGCGGUAGCAGGUACUAUGGCCAAUCUACAUAGUUUCCCACCCCGCCGAACGUCAGGUGAGAUAUGCCGCCAUUGUGGAAAGCAUUUAAGACAGACAUCAGUUUGGAACAUCGUCGGGAGUGUAACUACCCCUCGGAUUUCCCAAGCGGGCCUUUGCCAAUCCAGGACCUUCGGCACUAAUGUUGUGCCUGCAAGCCAAUGGGUCACGCAAACUUUGGGCUCGCGGGCUCUUGCGGGUCUAGACCCAUGUCCUGUCCAUUCAUCAGAACUCCUACCGACACUCUCCCAGCUCCCCAUGAGUGACAACCCCAAUUCCAGCGUCUCGUCGAGGUUCUGGGCAAGACCCUCAGUCAGAAAGUAUCUGGAAAUUCGCACAUGUGACAAGAAGGUCAUGAGCGUGAUUCCCCCCUUGGUGGUGCUUUUAGAAUCGUUCUCCCGUCUGAGAUCAUAUUGGCCAGAAAUCCGUCUCCUGUCGCCUUUGCAAAUAUGCCGACGGGACGUUUGCAAUCUGAGAACUUGCCGGACGAUACUAUUGAAUUAUAGAUUAUUCCCUGACGUGGUAUUCGGCAUUUAUAACGCAAGUCGAAUUCCAAACAGACCCGGAGGCCAUUUGCAAAAGGUGGCUGUCUUUAGUGAUAUACCAUGCAGCUGCGAUGCAGAAGACAUAAGGCGCAAUGUUGCCAACAGCCCCAAUGGUGGUAAGGGUACCGUCGGGAUGGGGGGAAUCCGAUCAGUAAGACUUCGGCAUUGCGUGCCGUAUCCACGGUAUCUUUGUCCAGUUACGAGGUCCCAGGCAAUGGCCUGGAUUCUCGUGCCCCUUGGCCUAGCAGAAAUGAGAGUGUAUAUAGUUUUUAUAAUUAAGGGGUGGAAUGGACCUCAGGAGACUCGUGGGUGUAAAAGAGCCAUAGAAGACACAUCUACCGGUUGGUUAGCCUAUCCUGGUCGCUUAAUUUCCCGGAUUUUAGAAAACAGUGGAACGGAGGUCUAUUUAUGUAAGUCGGCGAUCAGUAUCAGUAGCACAGGCGUUUCGUGGCGCUCGCGCCACGGCGCAUCUUCUAUAGAGCGGGUACAGGAAAUAAGCGUCAUUCCAGUAGGAUAUUGUAUCAUAACCGUCUUUGACUGUGUGUCCCAGGUUGUCCCACCCUCACGACUGCGAAUUAGUUAUGUUGGCUCAGUCAAUCAACCCGCCUGGCAGUUUCCUACUCGGUCAGUAUCCAGUUUCCACAAGGCAGUUAACAGUACCGCUUAUGACACCGACCUUGGACUGGUCGGGACACGUUGCUAUCCUAUAAUCCUGAAUGGCCCUAAAGUUGCACUACAAUACGCGCAACACACAAAAGGGUACCGGAAGGAUCUUUAUGACCGCCAGAAUACGAGGUGCAAACUUGUUCCCCCCUAUCACCCCCUCGAGCGGGGUUCGGCAAACGUUUUUAAUCCUAGACUAGCGAUCCGUACACUCAAUAGACUCACCGCUAAUACGGCUACACGAGCUGGCUACGGGGCUGGAUCCCUUUACCAUCGACAGAAGGAUCCUUGGGGGGAUGCGGCAUUCCCUUUGCCGCUUGGGGGCUGCGAGAAUACACUUUCGCAAGUCUUUGGCACUCUCGUUAACGUCGUCAGUAUACCCUACGCGGUACGCCGGGACCCAAUGGGGGCGAUGAGUGUCGUAUGUCGGCGACAGCUAGCACACAGUCACCACCCGGCUCGUGGUGUCCCUGUCUGCAGCGUCCGCACGUUGAGCUUCGGGUAUAAGGUGCGUGAAUCCCAGCCUUCUUUUAGAGGGAGCCUAUGCACGAUUUGUUUUCUAGUCAACCGGCCAUGUUGCAAGCGCUUACUCGGAGGCUCCGCGGGACGUAGCAUUAAGAUUAAUUUGAAGAGGACCCCGACGGUUUAUAGGAAGAACCACCAAAACAUGGGGAGGGUAGCUCGGAGCUCCCACAGCAUGGCAAACCUGGAUACUUUACGGGCACCCGGCCCACAACCACGACAGAAUACUAGAUGUGAAGGAACCCGCUUUGUCGAGCCCCUCCAAGCAUCACAUUCCCACCAACUAGGGUCGGGUUGUGAUAGCCAGGCCGUUUAUCAUCUGAUAGACGAUUACAUUGAACGUAUUGGACUCCCGAGAUGUGCCGCAAGAAAUUUGCAGCUACGCCCCCCGACGUUUUUUACACGGUUUUCUAUGAUGGUUAAGGCCAAACAAAUGUGGUGCUGCCACUUCACGCUUUACUUGAGUGUCGCCUCGCAUUCUGCCAAGCCGUGGAAGAAGGCUGCGGUGUGCACUUUUGCCAGUGGUUUGCGUGGAAUUGUCUUCUACAACACUCAUUUUGUCCAGUUUGGAGCAUGCGUGCGUGACACGGCCCACGGGGCCAUCCUAUACGAGCCUUCAUAUGCGGGGCUCGGCACACACACUUUAUGCAUGUCGCUGGCUGUAAGGUCUAAAUCGGACGUUCCGACGCAGUCAGUCUUUUGGAAGGGGUUCUUCGAAGACCCGGGGCCUUUUGAACGGGAGAUCUUCUUUUGUCCGGCAGUUUCCCAGGGACUGGCUCCAUUACGUACCUGGUAUGAACGGCCGCAAAUGGAUAUAAUGGCCUUCACUAAUGACAUAAUUGUAACUUCAACGAUAGAGCUACCGGGCAUUCAACUAUUGCUUACCCCACUCCCCGGGCCACGGUCAUCUGGACUGGUAAUGGCCGUGUGGGCCUUAGAGGUGGAAUUGUCGGACGUGUCAAGUCCAUUCGGACAUGCAUUACAGAGUGCAGCGCGACAGUGGGACAAGGCACGCCAUCCAGGACUGUCUAAAGACAGAUGCUCUCAAACGUUCCCUGGUAAUCAGAGGGCGGCGUUUAAACAAAUAGAAUGGCCUUGGCUUACGUGCCCUGGCCCGCAUAUGUUCCCGUACAGGUCCCUCACCGGCGAGAUGCCCUAUUCCGGGCGGAACACCCCCAGACUCCACACCGAGCGCCCGAUAGUCCAUGCCAUUGAUCAGCUACCUGCAAGUAGAGUCAGAACCGCCUUACUCUGUUCCGCAUUGUUCAGGACCCAUACUUGGGUGGUAUGUCAGUUUUACCCUCAGUCAAACCGAGAGCACUUGGGUACCGCGAAACUGUGCACAUGUUGCCGCAUAUGUGCAAUGCCCCGAUACCCUCUGUUCUCUAUCCACUUACCCAGAGACCAGGGUCCGCAUCACGGCAAUAGCUUGUCCCGCUGCCGCCGGGUCUCUGGUUUAAUGUGCCGUUCCGGGUGCAUACAGCAAGGUGACGUCAACAAGGUGUACCAAAGCAAAUCGAAGGUUGGCAUAUGCAACGUUUGGAUGCAUGACGGAACCGCGCUGGCGCCCCGUUCAACCGGUCACGGCCCUUUCGCAACAACUCCUAGAACCGCCACCCAUGAUGGCCACGGGCGGUGGGAUACGUCUCCUCAUGCCCGAUCGGUACCCGUGCAAGAAGUCUCCUCGCAUGGACCCAGUAGGAAAUUAGGAUGCCCUCCAGUCGGCAGCAGCUUCAAGAGGCCAGGCCUGCACUUACAUGCGUUGAAUCCUUCUGACCAAACUCCUCCUUCGCAUCGGCUAAAGGGUCGUUCGCGUCCCCCGUUUAAACUUUAUGCUUGGAAUUCGCCGCAUCCUCACAUCCGCAGAGAUCAAGUCGAAGACGUGCGGCGUGUGGUGUGGCGGGAGCCUGAACGACAUUACAGCUUGUAUGUUCCGUACGCCGGUCAUAGACCAAACGGGGUGGCUAGUCACUUUCUUUUACACCCAAGGGUGUUACACGCUUGCUCUGGGGCCGCUCAUCCGCGAAAAAGCAAAUCAAUCGACUUACAGGUAGUCUGUUGGUCUAUAAGGAAUGGGGAGAUUCUUCCGGUCUUUUCGGGCAUCGGUCGUAGCCUAGCGACCCAUGGCGCGGAAGCUCCCAGAGGCAGACUGAACACGUCUCGUUUAUAUGUACUUAUCGGGAACGGACCACUAAGUAGGGGACAGAGUCAAAGCUGGUCAGGCUCCGUUCACCUGAGUUGGUGGAUACAGUCUUUCACUUUUUUCUGCAAAGAGCGUCCCCUCCAUACCUCUGCCUCGCCCGGUUGCCCUCGAGUAUGUAGUAACCUGUACCAGACGUUAUACGAUGUCACGAGCGUCUAUUUCACAUGUGUGACGGAGCUACUCUGCAGACCCACUCAAGUGAGUUGGAUAAGCCCGUCGUCUGGGAUUCGUGGCAGUCUACUACGUAAAAGUAAUUGUAACAAAUAUAGUGAACGUGGUGUCCACAGCUACCUCGCGACGUUUCUGGGCCACAGUAUCACUACACGACGGCGCGUCUACGGUUGUGCGAAGGGGGGUGGAUCUGUUAUCGCUCGGGAACGUGUGAGAUGGCCGUGCACUAUGCAUUAUACAUACACUAGCUGGUGCCAAUGCCGCGCUGUCCGAUUACUCGUAUUUGUUGAAUUCGGCAUUACCAAUCGGACGACACGGACGUGCCCGCUCUUUGACACGUGCUGCGCACAAUCUCGCUCGGGUCGGUACCCUACUAAUUACCAUAGAAGGGUAUCUCAAUCCACUGCCGGGACGACCGUCCUAAAGGUGGCGGCGCUUCUACACAGCCUGGGCUACAAGGAAGGAGCCAAGAGGGUACUUUUCUUCCAAAGCCAGUGUUGCGACCAAAACGGCUGUCGUAGGUUCGUAUUGCCUAAGCGAAAGGAUAGUUAUUCUCGAGUGACAGGCACAGCGAUAACGCCGGCCGGUGAGAUCGGUGAAGUUACAGCUGUGACAGUUCCGUCUUGCGAACACUGCUACGCCAACCACUUCGUCGUUGACAUAUUGUUAGCCGGUGCAGUCAUAUGUAUUAUCGUUACGCCCAGGAUACUGAACCAUCAUUACUGGUCACAGCCUUCACCAUCCCAACACGUUCGCACUGUUCACCGAUAUCGCGAUCUCACGAUGGGACCUGCGGGGUUGGAGUUCUGUCGGUCAUACCGUCUUUAUGCACGUUACCCUGGGAUCAUCAACGGGAGCAUCAUCAUUCGGCUCAUUGAUGGGAUCGUCGGAGACCAUCCGUCCAUGUCUGCUCUGGACGGCUGCAGGUCGAUUACAGAUAUCGCGCAGACCACACUGGAUUGUUCGUCAUGGACAUGUCAAAUUGUUCUGUUAACAAAACUGGUAUGUACAUGCUCUCGUUCGCGGCAGGCAUCAUCCGUGGCAAAAGAUCAAGUGUCUGCUGGCGACCUUACGCGGUUGCUUGAGACUCGGACACCGACUCAGGGGGAGAGCCGGUGUUCACAGGAGUUUAGGAAGAGCCCCAACGUUAUGCUCGCGCUACUACACUUCGCAAAGUGCGCAUUCCAUGCUGAUAUUUUAUAUGAAAACACUAGCAAUGCUGGCUAUCUGUGGGGGCCCCAGCCGCUUCCACUUAUCGAUAUAGUUUGCUCUUCUCGGUCUCGCGACCGCGAGAGCGUGAUGAGGUUGCCUCGCACAAAGGGGCACAAUCUACUAGAAAUUCUGGCUGGAGGUCAUCUGCAUGGUAUGAUGCUAUUGGGCGGGUAUCCUAGUCCAGUGGAGCUGCUAAGGGACAGGUCGGUUGCAGAUAGUGGCCUUUAUCAAGACCGAUGUCGCUCCUUACCUUUAUUUUAUUGCCCGAGCUCCGUAUCGGGCUUUAAAGGGUAUUACUGCGCCUCAUGCAAUGGGGUUCUACCCCAGCCAGAUCAUAUGCACUCUAGCAUUCCUUUGUGUCACUUCGACACUUUGAGCCCAAAACUUCUGGUAUGCUUCACAUAUGCGACGACCAAGAUGCAUACGGCUCAAGAAACUAUCAGCCCGAUCACCUUCAUCCUGGCCUGGAGGGGCCUGGGGAAGGUGGGCACCCGGGGGGUAACGCGCGAACCCGGACCGGGAUCUGUGCUCGUAGAAGUUGCCACUAGCGGGACAAUUCAUCAUAGAUUACAUUGUUGGAACAGAGCGCCGGCCACAGGGAUUGCAGUUUUACGUCCGUCAGUCAAGUCAAUGCGGACACCGGUUCGGCCUAUCCGUGUUGUCAGCAUUGCUUGGCAGUCCCAGGACACGGCAACGCCGAUGGUAAAAUCAUUCCGUCGUGCGCCGAGAGGUUUGGGUCUGCGAUCAGUUGAGUCCUUUCUCACGGUCUUUAACAUUCGACCAAAAAACAUCUUUCAGCUUUCUGUGGCGAAUGUUCCUCUCCCACGACUGGCACCACGCCUGUAUGCAUUAACAAUUUGCUGCGUAUCCGUAGGGGCAGCGAAUAGAACCCCCAUUAUGACACAGGCCCGCCCUCGAAGGAUGGUUCUGAUCAGUUGUGCAUCAAAGUAUCCUUGGAAGCGCCCAGUUAGACGGCUUAUAGGCACAAUACUAAAGUACGUGAAGUAUAUGGGCUUCUUAGUAUGUAGGAGGCCCCCAGGUAGCGUGCUGGCAAGCAACCAUAAGACGCUUCAGCCAAUCGAAGGAAGCUUCCACGUAUGCGUAAUGAAGCGCACGCAAUGUUACCUAAGCCUUAUACCUUCGAGCACUAACCACCGAAAACAUGGAGACGACGAACGGCGGUACCCCGCAGAACCACGCAGAUGGCGGUCAGGACACGGCCAGCGCAAAAGGUCGUCCACGCGCAUUCGAACAUUACCAUGUGAGUAG"

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
