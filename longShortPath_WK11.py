v,e,c = int(input()), int(input()), int(input()) 

inf = 100000000

final_weights = [inf for i in range(v)]
final_weights[c-1] = 0

current_weights = final_weights 

for pairs in range(e): 
    node1, node2, weight = int(input), int(input()), int(input()) 

print(final_weights)