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

    def checkParallel(self,input1,input2):
        result = ''
        in_test = []
        for element in self.elements: 
            if element.edgeName == input1 or element.edgeName == input2: 
                in_test.append(element)
        a,b = in_test[0],in_test[1]
        if a.node1 == b.node1 and a.node2 == b.node2: 
            result = 'PARALLEL'
        else:
            result = 'NULL'
        return result 

resNet = resistorNetwork() 

n,q = [int(i) for i in input().split(" ")]
for j in range(n): 
    resName,start,end,value = [j for j in input().split(" ")]
    value = float(value)
    resNet.addElement(spiceLine(resName,start,end,value)) 

a = resNet.checkParallel
print(a)


