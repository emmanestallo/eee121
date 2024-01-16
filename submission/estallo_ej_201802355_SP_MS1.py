from collections import defaultdict

# input parameter are resistor names and resistor network
# ouputs a boolean value indicating whether the two resistors are in parallel
def parallel_identify_connection(r1 , r2, resistor_network):
    edge_r1 = resistor_network[r1]
    edge_r2 = resistor_network[r2]

    return set(edge_r1) == set(edge_r2)

# for the linked list idea, the following sources were used

# https://stackoverflow.com/questions/14022701/good-data-structure-for-representing-multigraph-c 
# https://stackoverflow.com/questions/71653546/linked-list-keeping-track-of-each-node

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

series_linked_list = None

count = 0

n = 0
q = 0
resistor_network = {}
resistances = {}
connecting_edges = defaultdict(list)
starting_from = defaultdict(list)
ending_to = defaultdict(list)
edges_list = []



if count == 0:
    n,q = [int(i) for i in input().split(" ")] 
    count = count + 1

while count <= n + q:
    if count > int(n):
        res1, res2 = input().replace("\n", "").split(" ")
            
        if series_linked_list is None:
            series_linked_list = series_generate_linked_list(resistor_network, starting_from, ending_to)
            
        print(identify_connection_type(res1, res2, series_linked_list))
        count = count + 1
        
    else:
        resName, start, end, value = input().split()
        value = float(value)
        resistor_network[resName] = [start, end]
        resistances[resName] = value
        connecting_edges[(start, end)].append(resName)
        starting_from[start].append(resName)
        ending_to[end].append(resName)
        edges_list.append((start, end))
        count = count + 1