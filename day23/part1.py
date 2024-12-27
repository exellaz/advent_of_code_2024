# Answer: 1075

edges = [line.strip().split("-") for line in open("input.txt")]
connections = {}

for x, y in edges:
    if x not in connections:
        connections[x] = set()
    if y not in connections:
        connections[y] = set()
    connections[x].add(y)
    connections[y].add(x)

sets = set()
for x in connections:
    for y in connections[x]:
        for z in connections[y]:
            if x != z and x in connections[z]:
                sets.add(tuple(sorted([x, y, z])))

print(len([s for s in sets if any(connection.startswith("t") for connection in s)]))
