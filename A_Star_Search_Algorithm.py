import ast
#read the graph from text grapg
with open('Graph.txt') as file1:
    data1 = file1.read()
graph = ast.literal_eval(data1)
#read heurstic table from text file
with open('HeursticTable.txt') as file2:
    data2 = file2.read()
h_table = ast.literal_eval(data2)

#function to get cost
def path_f_cost(path):
    g_cost = 0
    for(node , cost) in path:
        g_cost += cost
    last_node = path[-1][0]
    h_cost = h_table[last_node]
    f_cost = g_cost + h_cost
    return f_cost , last_node
#functon to get the shortest path
def Astar_Search(graph , start , goal):
        visited =[]
        queue =[[(start , 0)]]
        while queue:
            queue.sort(key = path_f_cost)
            path = queue.pop(0)
            node = path[-1][0]
            if node in visited:
                continue
            visited.append(node)
            if node == goal:
                return path
            else:
                adjacent_nodes= graph.get(node , [])
                for(node2 , cost) in adjacent_nodes:
                    new_path = path.copy()
                    new_path.append((node2 , cost))
                    queue.append(new_path)
                    
solution = Astar_Search(graph , 'A' , 'J')
print("Solution is : ", solution)
print("Cost Of Solutions is : " , path_f_cost(solution)[0])
