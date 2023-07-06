class spiceLine: 

    def __init__(self,edgeName,node1,node2,edgeWeight):
        self.edgeName = edgeName 
        self.node1 = node1 
        self.node2 = node2 
        self.edgeWeight = edgeWeight 


class resistorNetwork: 

    elements = []
    parallelNodes = [] 
    seriesNodes = [] 
    isCheckedP = []
    isCheckedS = [] 

    def __init__(self): 
        pass

    def addElement(self,element):
        self.elements.append(element) 

    def viewNetwork(self): 
        for element in self.elements:
            print(type(element.edgeName))  

    def isParallel(self):
        toCheck = 0
        for idx in range(len(self.elements)):
            toCheck = self.elements[idx]
            n1,n2 = toCheck.node1, toCheck.node2
            for _ in range(idx+1,len(self.elements)):
                m1,m2 = self.elements[_].node1, self.elements[_].node2
                if [m1,m2] == [n1,n2]:
                    self.parallelNodes.append([self.elements[idx].edgeName, self.elements[_].edgeName])
                    self.parallelNodes.append([self.elements[_].edgeName, self.elements[idx].edgeName])
        return self.parallelNodes 
            
    def isSeries(self):
        toCheck = 0
        for idx in range(len(self.elements)):
            toCheck = self.elements[idx]
            n1,n2 = toCheck.node1, toCheck.node2
            for _ in range(idx+1,len(self.elements)):
                m1,m2 = self.elements[_].node1, self.elements[_].node2
                x = [i for i in [n1,n2] if i in set([m1,m2])]
                if len(x) == 1 and 'Vdd' not in x and 'GND' not in x:
                    self.seriesNodes.append([self.elements[idx].edgeName, self.elements[_].edgeName])
                    self.seriesNodes.append([self.elements[_].edgeName, self.elements[idx].edgeName])
        return self.seriesNodes 



resNet = resistorNetwork() 

n,q = [int(i) for i in input().split(" ")]
for j in range(n): 
    resName,start,end,value = [j for j in input().split(" ")]
    value = float(value)
    resNet.addElement(spiceLine(resName,start,end,value)) 

a = resNet.isParallel()
b = resNet.isSeries()


for i in range(q):
    n1,n2 = input().split(" ")
    if [n1,n2] in a:
        print('PARALLEL') 
    elif [n1,n2] in b: 
        print("SERIES")
    else:
        print("NEITHER")