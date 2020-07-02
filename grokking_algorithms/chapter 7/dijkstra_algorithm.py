graph = {}
graph['start'] = {}
graph['start']['A'] = 6
graph['start']['B'] = 2

# print(graph['start'].keys())    # все соседи узла "старт"
# print(graph['start']['A'])      # вес ребра "А"
# print(graph['start']['B'])      # вес ребра "В"

graph['A'] = {}
graph['A']['end'] = 1
graph['B'] = {}
graph['B']['A'] = 3
graph['B']['end'] = 5
graph['end'] = {}

infinity = float("inf")
costs = {}

costs['A'] = 6
costs['B'] = 2
costs['end'] = infinity

# parents = {}
#
# parents['A'] = 'start'
# parents['B'] = 'start'
# parents['In'] = None

parents = {'A': 'start', 'B': 'start', 'In': None}

processed = []  # Массив для отслеживания узлов


def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

print(costs['end'])