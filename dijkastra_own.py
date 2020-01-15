nodes = ('A', 'B', 'C', 'D', 'E', 'F')

graph_distance = {
    'B': {'A': 8, 'C': 7, 'E': 2},
    'A': {'B': 8, 'D': 4, 'C': 2},
    'D': {'F': 5, 'C': 1, 'A': 2},
    'C': {'A': 2, 'B': 8, 'E': 3, 'D': 1, 'F': 9},
    'E': {'B': 2, 'C': 3},
    'F': {'C': 9, 'D': 5}
}

start = 'A'
current_node_distance = 0
visited = {}
unvisited = {}
unvisited[start] = current_node_distance

for all nodes