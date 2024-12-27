# Answer: az,cg,ei,hz,jc,km,kt,mv,sv,sx,wc,wq,xy

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

def search(node, req):
    key = tuple(sorted(req))
    if key in sets:
        return
    sets.add(key)
    for neighbour in connections[node]:
        if neighbour in req:
            continue
        if not all(neighbour in connections[query] for query in req):
            continue
        search(neighbour, req | {neighbour})


for x in connections:
    search(x, {x})

print(",".join(sorted(max(sets, key=len))))
