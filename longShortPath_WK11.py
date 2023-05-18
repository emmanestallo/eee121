def probeNode(node,startNode):
    #set current node
    if node in isNotProbed: 
        currNode = node 
        isNotProbed.remove(node)

        if currNode == startNode:
            cost = 0
        
        else:
            cost = final_weights[node]

        for neighbor in range(len(adjMat[currNode])): 
            if neighbor != currNode: 
                if adjMat[currNode][neighbor] + cost < final_weights[neighbor]: 
                    final_weights[neighbor] = adjMat[currNode][neighbor] + cost 


v,e,c = [int(i) for i in input().split(' ')]

inf = 100000000

final_weights = [inf for i in range(v)]
final_weights[c] = 0

start = c 

isNotProbed = [i for i in range(v)]

adjMat = [] 

for j in range(v):
    adjMat.append([inf]*v)

for center in range(v):
    adjMat[center][center] = 0

for trio in range(e): 
    [node1, node2, weight] = [int(a) for a in input().split(' ')]
    adjMat[node1][node2] = weight 
    adjMat[node2][node1] = weight 

for i in range(v): 
    x = int(input())
    probeNode(x,start)
    print(final_weights)
    print(isNotProbed)

#TESTING 

'''
7 9 3
0 1 50
0 2 60
1 3 150
1 4 20
2 5 50
3 5 80
3 6 70
4 6 40
5 6 140
'''
