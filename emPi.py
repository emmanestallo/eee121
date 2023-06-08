class spiceLine: 

    def __init__(self,edgeName,node1,node2,edgeWeight):
        self.edgeName = edgeName 
        self.node1 = node1 
        self.node2 = node2 
        self.edgeWeight = edgeWeight 


class resistorNetwork: 

    elements = []
    isVisited = []

    def __init__(self): 
        pass

    def addElement(self,element):
        self.elements.append(element) 

    def viewNetwork(self): 
        for element in self.elements:
            print(type(element.edgeName))  

    def isParallel(self):
        parallelNodes = [] 
        toCheck = 0
        for elem in range(len(self.elements)):
            self.isVisited.append(False) 
        for idx in range(len(self.elements)):
            if self.isVisited[idx] == False:
                toCheck = self.elements[idx]
                n1,n2 = toCheck.node1, toCheck.node2
                self.isVisited[idx] = True 
                for _ in range(idx+1,len(self.elements)):
                    m1,m2 = self.elements[_].node1, self.elements[_].node2
                    if [m1,m2] == [n1,n2]:
                        self.isVisited[_] = True
                        parallelNodes.append([self.elements[idx].edgeName, self.elements[_].edgeName])
        return parallelNodes 
            






resNet = resistorNetwork() 

n,q = [int(i) for i in input().split(" ")]
for j in range(n): 
    resName,start,end,value = [j for j in input().split(" ")]
    value = float(value)
    resNet.addElement(spiceLine(resName,start,end,value)) 

a = resNet.isParallel()
print(a)