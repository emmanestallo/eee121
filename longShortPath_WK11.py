v,e,c = [int(i) for i in input().split(' ')]

inf = 100000000

final_weights = [inf for i in range(v)]
final_weights[c-1] = 0

current_weights = final_weights 

edgeList = [] 

for pairs in range(e): 
    edgeList.append([int(j) for j in input().split(' ')] + [False])

print(edgeList)