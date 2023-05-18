v,e,c = [int(i) for i in input().split(' ')]

inf = 100000000

final_weights = [inf for i in range(v)]

dist = [inf]*v 
dist[c] = 0  

isProbed = [False]*v 
isProbed[c] = True 

adjMat = [[inf]*v]*v  

for pairs in range(e): 
    [node1,node2,weight] = [int(j) for j in range(3)]
