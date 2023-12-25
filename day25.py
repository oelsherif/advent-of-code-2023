from collections import defaultdict
import random

with open("inputs/25.txt", "r") as File:
    lines = [line[:-1] for line in File]

connections = defaultdict(list)
for line in lines:
    comp1, comps = line.split(':')
    for comp2 in comps.split():
        connections[comp1].append(comp2)
        connections[comp2].append(comp1)

def shortest_path(source, dest):
    """find shortest path between two components"""
    if source == dest:
        return []
    paths = [[source]]
    visited = set()
    while True:
        new_paths = []
        for path in paths:
            comp1 = path[-1]
            for comp2 in connections[comp1]:
                if comp2 == dest:
                    path.append(comp2)
                    return path
                if comp2 in visited:
                    continue
                new_path = path.copy()
                new_path.append(comp2)
                visited.add(comp2)
                new_paths.append(new_path)
        paths = new_paths.copy()

def get_wires(path):
    if not path:
        return []
    """takes path and returns the wires passed"""
    wires = []
    for i in range(len(path) - 1):
        comp1, comp2 = sorted([path[i], path[i+1]])
        wires.append((comp1, comp2))
    return wires

n = len(connections)
components = list(connections.keys())

count_wire_usage = defaultdict(int)
trials = 1000
#The top 3 used wires should be cut
for i in range(trials):
    comp1, comp2 = (random.choices(components, k=2))
    wires = get_wires(shortest_path(comp1, comp2))
    for wire in wires:
        count_wire_usage[wire] += 1

sorted_wires = sorted(count_wire_usage.keys(), key=count_wire_usage.get, reverse=True)
top_three_wires = sorted_wires[:3]
for comp1, comp2 in top_three_wires:
    connections[comp1].remove(comp2)
    connections[comp2].remove(comp1)

# Start from any component and see how many will be reached. If it reaches all components then we've cut a wrong wire
comp0 = components[0]
visited = {comp0}
currents = {comp0}
while currents:
    old_visited = visited.copy()
    for comp1 in currents:
        visited.update(connections[comp1])
    currents = visited - old_visited

k = len(visited)
if k == n:
    print("Dismal Failure")
else:
    print("Success!")
    ans = k * (n-k)
    print(ans)