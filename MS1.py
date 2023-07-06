from collections import defaultdict

n,q = [int(i) for i in input().split(' ')]

R = []

# get all resistors
for _ in range(n):
    resName, n1, n2, res = input().split(' ')
    R.append((resName, n1, n2, float(res))) # convert resistance to float

connected_nodes = dict()
for resName, n1, n2, _ in R:
    connected_nodes[resName] = (n1, n2)

adjacent_resistors = defaultdict(list)
for resName, n1, n2, _ in R:
    adjacent_resistors[n1].append(resName)

def cant_traverse(s1, s2):
    next_edges = adjacent_resistors[connected_nodes[s1][1]]
    if len(next_edges) == 0:
        return True
    for resistor in next_edges: 
        if resistor != s2 and cant_traverse(resistor,s2):
            return True 
    return False 

def is_series(s1, s2):
    return not (cant_traverse(s1, s2))

def is_parallel(s1, s2):
    return set(connected_nodes[s1]) == set(connected_nodes[s2])


for test in range(q): 
    print(connected_nodes)
    s1,s2 = input().split(' ')
    if is_parallel(s1, s2):
        print('PARALLEL')
    elif is_series(s1, s2):
        print('SERIES')
    else:
        print('NEITHER')


'''

6 
R1 Vdd a 0 
R2 Vdd b 0 
R3 a GND 0
R4 b c 0 
R5 b c 0
R6 c GND 0 

'''

