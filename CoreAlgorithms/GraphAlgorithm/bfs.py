length = int(input("Please enter the number of unique keys:"))
graph = {}
valList = []

for i in range(length):

    keys = input("Please enter the key input value: ")
    valLength = int(input("Please enter the number of values for this specific key: "))
    valList = []
    for j in range(valLength):
        values = input("Please enter the value of the key: ")
        valList.append(values)
        graph[keys] = valList

    
print(graph)

visited = []
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end = '')

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

inputNode = input("Specify the node you want to start bfs: ")
bfs(visited, graph, inputNode)