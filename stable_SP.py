from collections import defaultdict




def traverse_from_start(conn_edges,graph,node): 
    series_resistors = [] 
    parallel_resistors = [] 

    #implements depth first search 
    stack = [] 

    stack.append(node) 

    before_stack = []
    series_streak = [] 

    while len(stack) != 0: 
        current_node = stack.pop()
        print(current_node)
        #print(f'{current_node}: {graph[current_node]}')
        for neighbor in graph[current_node]:
            # check if there is a parallel connection
            # use before stack structure
            before_stack.append(neighbor)
            #print(before_stack)
            neighbor_toTest = before_stack.pop()
            #conn_edges = connecting edge from node1 to node 2 (> 1 if parallel edges)
            res = conn_edges[(current_node,neighbor_toTest)]
            if len(res) > 1:
                parallel_resistors.append([i for i in res]) 

            if neighbor_toTest != 'GND':
                stack.append(neighbor)
            
            #print(before_stack)
            #print(stack)




            

    #print(parallel_resistors)
    #print(series_resistors)
    


def create_adjList(input_dict): 
    adjList = defaultdict(list)
    for res, (n1,n2) in input_dict.items():
        if n1 not in adjList: 
            adjList[n1] = [] 
        if n2 not in adjList[n1]:
            adjList[n1].append(n2) 
    return adjList


resistor_network = {} 
resistances = {} 
connecting_edges = defaultdict(list) 

n,q = [int(i) for i in input().split(" ")]
for j in range(n): 
    resName,start,end,value = [j for j in input().split(" ")]
    value = float(value)
    resistor_network[resName] = [start, end] 
    resistances[resName] = value 
    connecting_edges[(start,end)].append(resName) 

res_graph = create_adjList(resistor_network) 

#print(res_graph)
#print(resistances)
#print(connecting_edges)
#print(resistor_network)

a = traverse_from_start(connecting_edges,res_graph,'Vdd') 