class spiceLine: 

    def __init__(self,edgeName,node1,node2,edgeWeight):
        self.edgeName = edgeName 
        self.node1 = node1 
        self.node2 = node2 
        self.edgeWeight = edgeWeight 


class resistorNetwork: 

    elements = []

    def __init__(self): 
        pass

    def addElement(self,element):
        self.elements.append(element) 

    def viewNetwork(self): 
        for element in self.elements:
            print(type(element.edgeName))




resNet = resistorNetwork() 

n,q = [int(i) for i in input().split(" ")]
for j in range(n): 
    resName,start,end,value = [j for j in input().split(" ")]
    value = float(value)
    resNet.addElement(spiceLine(resName,start,end,value)) 

resNet.viewNetwork()


