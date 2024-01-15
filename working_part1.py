from collections import defaultdict

n = 0
q = 0
resistor_network = {}
resistances = {}
connecting_edges = defaultdict(list)
to_diverge = defaultdict(list)
to_converge = defaultdict(list)
edges_list = []

# input parameter is the list of edges
# outputs an array of pair of edges that are parallel
def parallel_generate_edges(edges_list):
    edges = {}
    for edge in edges_list:
        if edge not in edges:
            edges[edge] = 0
        edges[edge] += 1

    res = []
    for edge, count in edges.items():
        if count > 1:
            res.append(edge)
    return res

# input parameter are resistor names and resistor network
# ouputs a boolean value indicating whether the two resistors are in parallel
def parallel_identify_connection(r1 , r2, resistor_network):
    edge_r1 = resistor_network[r1]
    edge_r2 = resistor_network[r2]

    return set(edge_r1) == set(edge_r2)

# input parameters are resistor names and resistor network
# outputs a boolean value indicating whether the two resistors are immediately in series
def series_identify_immediate_connection(r1, r2, resistor_network, to_diverge, to_converge):
    edge_r1 = resistor_network[r1]
    edge_r2 = resistor_network[r2]
    start_r1 = edge_r1[0]
    start_r2 = edge_r2[0]
    end_r1 = edge_r1[1]
    end_r2 = edge_r2[1]

    if start_r2 == end_r1:
        return (len(to_converge[start_r2]) <= 1) and (len(to_diverge[start_r2]) <= 1)
    elif start_r1 == end_r2:
        return (len(to_converge[start_r1]) <= 1) and (len(to_diverge[start_r1]) <= 1)
    else :
        return False

# output is a dictionary of resistors that are in series
# key points to the resistor that is immediately in series
def series_generate_linked_list(resistor_network, to_diverge, to_converge):
    series_linked_list = {}
    resistors_list = resistor_network.keys()
    for res1 in resistors_list:
        for res2 in resistors_list:
            if res1 != res2:
                if series_identify_immediate_connection(res1, res2, resistor_network, to_diverge, to_converge):
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

series_linked_list = None

count = 0


if count == 0:
    n,q = [int(i) for i in input().split(" ")] 
    count = count + 1

while count <= n + q:
    if count > int(n):
        res1, res2 = input().replace("\n", "").split(" ")
            
        if series_linked_list is None:
            series_linked_list = series_generate_linked_list(resistor_network, to_diverge, to_converge)
            
        print(identify_connection_type(res1, res2, series_linked_list))
        count = count + 1
        
    else:
        resName, start, end, value = input().split()
        value = float(value)
        resistor_network[resName] = [start, end]
        resistances[resName] = value
        connecting_edges[(start, end)].append(resName)
        to_diverge[start].append(resName)
        to_converge[end].append(resName)
        edges_list.append((start, end))
        count = count + 1
