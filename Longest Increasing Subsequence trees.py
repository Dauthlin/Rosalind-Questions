class Tree:
    def __init__(self, data):
        self.children = []
        self.data = data

    def Print_tree(self, parent = None):
        #prints the tree displaying the parent node and whether its a node or a leaf connecting to it
        if parent == None:
            parent_data = -1
        else:
            parent_data = parent.data
        if self.children == []:
            print(parent_data,"leaf",self.data)
            return
        result = []
        print(parent_data,"node",self.data)
        for i in self.children:
            i.Print_tree(self)
        
    def longest_path(self):
        #finds the longest total path in the graph and outputs the data at each position
        longest = []
        if self.children == []:
            return([self.data])
        for i in self.children:
            current_path = i.longest_path()
            if len(current_path) > len(longest):
                longest = current_path
        longest.append(self.data)
        return(longest)    

    def longest_path_upto_ass(self,max_value):
        #finds the longest total path in the graph up to a max value and outputs the pointer to that position for numbers that are accending from its parent
        longest = []
        if self.children == []:
            return([self])
        for i in self.children:
            current_path = i.longest_path_upto_ass(max_value)
            if (len(current_path) > len(longest))  and (i.data <= max_value):
                longest = current_path
        longest.append(self)
        return(longest)    
    
    def longest_path_upto_dec(self,max_value):
        #finds the longest total path in the graph up to a max value and outputs the pointer to that position for numbers that are decending from its parent
        longest = []
        if self.children == []:
            return([self])
        for i in self.children:
            current_path = i.longest_path_upto_dec(max_value)
            if (len(current_path) > len(longest))  and (i.data >= max_value):
                longest = current_path
        longest.append(self)
        return(longest)    

    def add_child_accending(self,data):
        #adds a single new child to the graph in the accending tree, this is useful as it prevents the graph from become too large and impossible to process in 5 mins 
        path = self.longest_path_upto_ass(data)
        path[0].children.append(Tree(data))
        
    def add_child_decending(self,data):
        #adds a single new child to the graph in the accending tree, this is useful as it prevents the graph from become too large and impossible to process in 5 mins 
        path = self.longest_path_upto_dec(data)
        path[0].children.append(Tree(data)) 



fid = open('rosalind_lgis5.txt','r')
fout = open('result.txt','w')
n = int(fid.readline().strip())
text = [int(x) for x in fid.readline().split()]






first = Tree(0)
second = Tree(10000000000000000000)

for i in text:
    first.add_child_accending(int(i))
    second.add_child_decending(int(i))

inc = str(first.longest_path()[::-1][1:]).replace("[","").replace("]","").replace("'","").replace(",","")
dec = str(second.longest_path()[::-1][1:]).replace("[","").replace("]","").replace("'","").replace(",","")

fout.write('%s\n%s' %(inc,dec))


# print(str(first.longest_path()[::-1][1:]).replace("[","").replace("]","").replace("'","").replace(",",""))
# print(str(second.longest_path()[::-1][1:]).replace("[","").replace("]","").replace("'","").replace(",",""))






            
            


