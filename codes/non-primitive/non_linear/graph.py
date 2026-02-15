# Graph implementation using adjacency list


graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"]
}

print("Graph representation:")
for node in graph:
    print(node, "->", graph[node])

