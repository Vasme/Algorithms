tree = {"1":["2","3"], "2": ["6","7"] ,"3": ["4","5"] ,"4": None,"5": None , "6": None , "7": None}

queue = []
visited = []
c_node = '1'
queue.append(c_node)
while True:
    visited.append(c_node)
    for elem in tree.keys():
        if  c_node == elem and tree[elem] != None:
            for i in range(len(tree[elem])):
                queue.append(tree[elem][i])
    queue.pop(0)
    if len(queue) == 0:
        break
    else:
        c_node=queue[0]

print(visited)
