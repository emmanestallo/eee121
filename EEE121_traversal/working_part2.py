from collections import defaultdict

# counts the edges that connect the same two nodes
def parallel_generate_edges(edgeList):
    edge_counts = {}
    
    for edge in edgeList:
        edge_counts[edge] = edge_counts.get(edge, 0) + 1

    # find edges that appear more than once (parallel edges)
    parallel_edges = [edge for edge, count in edge_counts.items() if count > 1]
    
    return parallel_edges

# finds all the series connections using iteration
# essentially gets the longest streak from a linked list
def find_all_series_streaks(series_linked_list):
    visited = set()
    series_connections = []

    for key in series_linked_list:
        if key not in visited:
            current_element = key
            current_streak = []

            while current_element is not None and current_element not in visited:
                visited.add(current_element)
                current_streak.append(current_element)

                current_element = series_linked_list.get(current_element)

            series_connections.append(current_streak)
            
    return series_connections


# input parameter are resistor names and resistor network
# ouputs a boolean value indicating whether the two resistors are in parallel
def parallel_identify_connection(r1 , r2, resistor_network):
    edge_r1 = resistor_network[r1]
    edge_r2 = resistor_network[r2]

    return set(edge_r1) == set(edge_r2)


# input parameters are resistor names and resistor network
# outputs a boolean value indicating whether the two resistors are immediately in series
def series_identify_immediate_connection(r1, r2, resistor_network, starting_from, ending_to):
    edge_r1 = resistor_network[r1]
    edge_r2 = resistor_network[r2]
    start_r1 = edge_r1[0]
    start_r2 = edge_r2[0]
    end_r1 = edge_r1[1]
    end_r2 = edge_r2[1]

    if start_r2 == end_r1:
        return (len(ending_to[start_r2]) <= 1) and (len(starting_from[start_r2]) <= 1)
    elif start_r1 == end_r2:
        return (len(ending_to[start_r1]) <= 1) and (len(starting_from[start_r1]) <= 1)
    else :
        return False


# output is a dictionary of resistors that are in series
# key points to the resistor that is immediately in series
def series_generate_linked_list(resistor_network, starting_from, ending_to):
    series_linked_list = {}
    resistors_list = resistor_network.keys()
    for res1 in resistors_list:
        for res2 in resistors_list:
            if res1 != res2:
                if series_identify_immediate_connection(res1, res2, resistor_network, starting_from, ending_to):
                    # if not (res2 in series_linked_list.keys()):
                    series_linked_list[res1] = res2
    return series_linked_list



# create logic to iterative check if two resistors are in series using the series linked list
def series_identify_connection(r1, r2, series_linked_list):
    keys = series_linked_list.keys()

    r1_is_in_linked_list = r1 in keys
    r2_is_in_linked_list = r2 in keys

    if not r1_is_in_linked_list and not r2_is_in_linked_list:
        return False

    current_resistor = r1 if r1_is_in_linked_list else r2

    for i, r in enumerate(keys):
        if series_linked_list[current_resistor] == r2:
            return True
        else:
            current_resistor = series_linked_list[current_resistor]

    return False


def identify_connection_type(r1, r2, series_linked_list):
    if series_identify_connection(r1, r2, series_linked_list):
        return "SERIES"
    elif parallel_identify_connection(r1, r2, resistor_network):
        return "PARALLEL"
    else: 
        return "NEITHER"
    


count = 0

n = 0

resistor_network = {}
resistances = {}
connecting_edges = defaultdict(list)
starting_from = defaultdict(list)
ending_to = defaultdict(list)
edges_list = []


if count == 0:
    n = int(input())
    count = count+1

while count <= n:
    resName, start, end, value = input().split()
    value = float(value)
    resistor_network[resName] = [start, end]
    resistances[resName] = value
    connecting_edges[(start, end)].append(resName)
    starting_from[start].append(resName)
    ending_to[end].append(resName)
    edges_list.append((start, end)) 
    count = count+1
    

parallel_edges = parallel_generate_edges(edges_list)

a = series_generate_linked_list(resistor_network, starting_from, ending_to) 
series_streaks = find_all_series_streaks(a) 


for streak in series_streaks:
    total_res = 0 
    for res in streak:
        total_res += resistances[res] 

    print(str(sorted(streak)).replace("'", ""), int(total_res))

for edge in parallel_edges:
    res_value = 0
    resistors = connecting_edges[edge]
    for node in resistors:
        res_value += 1/resistances[node]
    
    print(str(sorted(resistors)).replace("'", ""), int(1/res_value))  



    

        

