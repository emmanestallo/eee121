# gets the pairwise combination of resistors
def find_pairwise(arr,storage):
    for i in range(len(arr)): 
        for j in range(i+1,len(arr)):
            storage.append([arr[i],arr[j]])
            storage.append([arr[j],arr[i]])
    return 


def create_adjList(graph):
    adjList = {} 

    for edgeName, (node1,node2,_) in graph.items():
        if node1 not in adjList: 
            adjList[node1] = []
        adjList[node1].append((node2, edgeName)) 

        if node2 not in adjList: 
            adjList[node2] = []
        adjList[node2].append((node1, edgeName))

    return adjList

#brute force method 
def find_parallel(graph):
    visited = set() # contains the nodes of visited resistors 
    parallelCombinations = [] 

    for resistor in graph: 
        current_resistors = []
        if resistor not in visited: 
            to_visit = set([graph[resistor][0],graph[resistor][1]]) #check the nodes of the current resistor
            current_resistors.append(resistor)
            visited.add(resistor) 
            
            for resName in graph: 
                if resName not in current_resistors and resName not in visited: 
                    node1, node2 = graph[resName][0], graph[resName][1]
                    if to_visit == set([node1,node2]): 
                        current_resistors.append(resName) 
                        visited.add(resName)
        find_pairwise(current_resistors,parallelCombinations)

    return parallelCombinations
    

# implement iterative DFS to get longest continuous edges 
def traverse(adjList,start_node):
    visited = set() 
    res_streak = [] 

    seriesCombinations = [] 

    to_check = [] 

    visited.add(start_node)
    to_check.append(start_node)

    while len(to_check) != 0: 
        current_node = to_check.pop()[0] 
        for neighbor in adjList[current_node]:
            if neighbor[0] not in visited: 
                res_streak.append(neighbor[1]) 
                visited.add(neighbor)[0]
                to_check.append(neighbor)[0]

    return seriesCombinations 
                    
                        
resistor_network = {}
resistor_network_series = resistor_network

n,q = [int(i) for i in input().split(" ")]
for j in range(n): 
    resName,start,end,value = [j for j in input().split(" ")]
    value = float(value)
    resistor_network[resName] = [start, end, value] 

a = find_parallel(resistor_network)

unique_parallel_res = [] 

for pair in a: 
    for elem in pair: 
        if elem not in unique_parallel_res:
            unique_parallel_res.append(elem)

for k in unique_parallel_res:
    del(resistor_network_series[k])

b = create_adjList(resistor_network_series)

for h in b: 
    print(f'{h}: {b[h]}')


for i in range(q):
    n1,n2 = input().split(" ")
    if [n1,n2] in a:
        print('PARALLEL') 
    else:
        print("NEITHER")



