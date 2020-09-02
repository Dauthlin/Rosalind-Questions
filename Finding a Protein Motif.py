import requests
text = """
P08514_ITAB_HUMAN
P01876_ALC1_HUMAN
Q8WW18
P03415_VME1_CVMA5
P01189_COLI_HUMAN
P06765_PLF4_RAT
Q81QB7
B4R8K2
Q28409
P08198_CSG_HALHA
P05113_IL5_HUMAN
B8CH81
P01045_KNH2_BOVIN
"""

text_array = text.split("\n")[1:]
text_array = text_array[:len(text_array)-1]
output = ""

for i in text_array:
    r = requests.get("http://www.uniprot.org/uniprot/"+i+".fasta")
    data = r.text[::-1]


    for count in range(len(data)):
        if data[count].isnumeric():
            data = data[:count][::-1]
            break
    data = data.replace("\n","")
    position = ""
    for j in range(len(data)):
        if len(data[:j]) + 3 <= len(data):
            if data[j] == "N":
                if data[j+1] != "P":
                    if data[j+2] == "S" or data[j+2] == "T":
                        if data[j+3] != "P":  
                            position += " " +str(j+1)
    if position != "":
        output += i + "\n" + position + "\n"

print(output)



