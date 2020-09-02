

text = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"

starts = []
ends = []
output_array = []

for i in range(len(text)):
    if text[i:i+3] == "ATG":
        starts.append(i)
    if (text[i:i+3] == "TGA") or (text[i:i+3] == "TAG") or (text[i:i+3] == "TAA"): 
        ends.append(i)
print(starts)
print(ends)
for i in starts:
    lowest = 1000000000000000000000
    current_end = 0
    for j in ends:
        if j-i < lowest:
            if j-i > 0:
                lowest = j-i
                current_end = j
    output_array.append(text[i:current_end]) 

output_array_unique = []
for i in output_array:
    if i not in output_array_unique:
        output_array_unique.append(i)
output = ""
for i in output_array_unique:
    output += i + "\n"

print(output)   



