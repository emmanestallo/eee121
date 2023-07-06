from collections import defaultdict

def is_parallel(node1,node2,con_edges):
    parallel = False 
    if len(con_edges[(node1,node2)]) > 1:
        parallel = True 

    return parallel

def get_total_series_resistance(ser_res,values):
    total_series_resistance = 0
    for i in ser_res:
        total_series_resistance += values[i] 
    return total_series_resistance

def get_total_parallel_resistance(par_res,values):
    total_conductance = 0 
    for j in par_res:
        total_conductance += 1/values[j]
    total_parallel_resistance = 1/total_conductance
    return total_parallel_resistance


def create_pairwise(resList,storage):
    for i in range(len(resList)):
        for j in range(i+1, len(resList)):
            storage.append((resList[i],resList[j]))
            storage.append((resList[j],resList[i]))
    return

def ends_in_diverging(connectors, node):
    diverging = False 
    if len(connectors[node]) > 1:
        diverging = True 
    return diverging 

def ends_in_converging(connectors, node):
    converging = False 
    if len(connectors[node]) > 1:
        converging = True 
    return converging 


def traverse_from_start(conn_edges,graph,node): 
    series_resistors = [] 
    parallel_resistors = [] 

    start_node = node 

    #implements depth first search 
    stack = [] 

    stack.append(node) 

    #to implement
    #visited = set of traversed edges instead of visited nodes
    visited = set()

    series_streak = [] 
    diverging_node = 0

    while len(stack) != 0: 

        current_node = stack.pop()
        
        if current_node not in [f'{start_node}','GND']:
            visited.add(current_node)

        if current_node == 'GND':
            if len(graph) > 1:
                stack.append(f'{start_node}')

        for neighbor in graph[current_node]:
            if neighbor not in visited and neighbor not in stack:
                stack.append(neighbor)
            if neighbor not in visited: 
                can_be_series = True 
                #series_streak += conn_edges[(current_node,neighbor)]
                if is_parallel(current_node,neighbor,conn_edges):
                    can_be_series = False
                    if len(series_streak) > 1: 
                        if series_streak not in series_resistors:
                            series_resistors.append(series_streak)
                    res = conn_edges[(current_node,neighbor)]
                    parallel_resistors.append([i for i in res])
                    series_streak.clear()
                if can_be_series:
                    series_streak += conn_edges[(current_node,neighbor)]
                    if ends_in_converging:
                        stack.append(diverging_node)
                        if len(series_streak) > 1:
                            if series_streak not in series_resistors:
                                series_resistors.append(series_streak)
                        series_streak.clear()
                    if ends_in_diverging:
                        diverging_node = neighbor
                        if len(series_streak) > 1:
                            if series_streak not in series_resistors:
                                series_resistors.append(series_streak)
                        series_streak.clear()

        if len(series_streak) > 1:
            if series_streak not in series_resistors:
                series_resistors.append(series_streak)
                
        
    return series_resistors, parallel_resistors


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
to_diverge = defaultdict(list)
to_converge = defaultdict(list)

#n,q = [int(i) for i in input().split(" ")]

n = int(input())

for j in range(n): 
    resName,start,end,value = [j for j in input().split(" ")]
    value = float(value)
    resistor_network[resName] = [start, end] 
    resistances[resName] = value 
    connecting_edges[(start,end)].append(resName) 
    to_diverge[start].append(resName)
    to_converge[end].append(resName)

res_graph = create_adjList(resistor_network) 

ser_resist, par_resist = traverse_from_start(connecting_edges,res_graph,'Vdd') 

total_resistances = list()

for series_element in ser_resist:
    total_resistances.append((series_element, get_total_series_resistance(series_element, resistances))) 

for parallel_element in par_resist:
    total_resistances.append((parallel_element, get_total_parallel_resistance(parallel_element, resistances))) 

for element in total_resistances:
    if element[0] == []:
        del(total_resistances[0])


for resists, values in total_resistances:
    print(f'[' + ', '.join(resists) + ']', f'{int(values)}')


'''
for element in ser_resist:
    create_pairwise(element, series_resistances)

for element in par_resist:
    create_pairwise(element, parallel_resistances)

for i in range(q):
    n1,n2 = input().split(" ")
    if (n1,n2) in parallel_resistances:
        print('PARALLEL') 
    elif (n1,n2) in series_resistances: 
        print("SERIES")
    else:
        print("NEITHER")

'''
