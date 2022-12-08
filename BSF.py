import ast
with open('BFS_Graph.txt') as file1:
    data1 = file1.read()
graph = ast.literal_eval(data1)

def BFS(garph , start , goal):
    visited = []
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            return path
        else:
            adjacent_nodes = graph.get(node , [])
            for node2 in adjacent_nodes:
                new_path = path.copy()
                new_path.append(node2)
                queue.append(new_path)

solution = BFS(graph , '5' , '8')
print('SOLUTION : ' , solution)