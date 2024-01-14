from collections import defaultdict

#checks if the resistors ending to a node have same starting node
def isSameStarting(node):
    resistor_list = ending_to[node]
    unique_starting = list()
    for edge in resistor_list: 
        start_node = resistor_endpoints[edge][0]
        if start_node not in unique_starting:
            unique_starting.append(start_node)
    if len(unique_starting) == 1:
        return True 
    else:
        return False 
    
#checks if a node can be visited by looking at the succeeding edges 
#if at least one of the succeeding edges is still not visited, the node is appended to the stack
def canBeVisited(node, visited):
    allVisited = True 
    next_edges = starting_from[node]
    for res in next_edges:
        if res not in visited:
            allVisited = False 
    if not allVisited:
        return True


def traverseFromNode(start_point):
    stack = list()
    visited_edges = list()

    series_ongoing = list()
    series_stack = list()
    parallel_stack = list()

    previous_node = start_point

    stack.append(start_point)
    while len(stack) != 0: 
        current_node = stack.pop() 

        #checks if the next nodes can be appended to the stack
        for succeeding_node in graph[current_node]:

            if succeeding_node == 'GND':
                stack.append(succeeding_node)
            else: 
                if canBeVisited(succeeding_node, visited_edges):
                    stack.append(succeeding_node)
                elif not canBeVisited(succeeding_node, visited_edges):
                    connecting_res = connecting_edges[(current_node,succeeding_node)]
                    count = 0 
                    for edge in connecting_res: 
                        visited_edges.append(edge)
                        count = count + 1 
                    if count > 1:
                        parallel_stack.append([edge for edge in connecting_res]) 
                        
        if current_node == 'Vdd':
            continue

        if len(ending_to[current_node]) == 1:
            series_ongoing.append(ending_to[current_node][0]) 
            visited_edges.append(ending_to[current_node][0])
        elif len(ending_to[current_node]) > 1:
            if len(series_ongoing) > 1:
                series_stack.append(series_ongoing)
            series_ongoing.clear()
            to_check = connecting_edges[(previous_node,current_node)]
            if len(to_check) > 1:
                parallel_stack.append([edge for edge in to_check])

        print(series_ongoing)
        previous_node = current_node

    return series_stack, parallel_stack, visited_edges




#input initialization
n = 0
q = 0
resistor_endpoints = defaultdict(list)
resistances = defaultdict(list)
connecting_edges = defaultdict(list)
starting_from = defaultdict(list)
ending_to = defaultdict(list)
graph = defaultdict(list)

count = 0 

if count == 0: 
    n,q = [int(i) for i in input().split(" ")] 
    count = count + 1

while count <= n: 
    resName, start, end, value = input().split(" ")

    #create the graph object using a dictionary
    if end not in graph[start]:
        graph[start].append(end)

    #input parsing
    value = float(value)
    resistor_endpoints[resName] = [start, end]
    resistances[resName] = value
    connecting_edges[(start, end)].append(resName)
    starting_from[start].append(resName)
    ending_to[end].append(resName) 
    count = count+1 


ser, par, vis = traverseFromNode('Vdd')

print(ser)
print(par)