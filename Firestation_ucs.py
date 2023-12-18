import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def edge(self, start, end, cost):
        if start not in self.graph:
            self.graph[start] = []
        self.graph[start].append((end, cost))

def ucs(graph, start, goal):
    # priority queue for UCS
    priority_queue = [(0, start, [start])]  # cost, node, path
    visited = set()

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            if cost > 0:
                print(f'Visiting barangay {node} with distance {cost} meters')
                print(f'\nGoal reached! Visited barangay: {" -> ".join(map(str, path))} with a total distance of {cost} meters')
            return

        if node in graph.graph:
            for neighbor, edge_cost in graph.graph[node]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (cost + edge_cost, neighbor, path + [neighbor]))

        if cost > 0 and node != goal:  # Check if the distance is greater than 0 before printing
            print(f'Visiting barangay {node} with distance {cost} meters')

# Barangay graph
g = Graph()
g.edge(2, 1, 900)
g.edge(2, 3, 750)
g.edge(3, 4, 500)
g.edge(1, 8, 600)
g.edge(1, 7, 1000)
g.edge(4, 7, 600)
g.edge(4, 5, 1200)
g.edge(8, 7, 400)
g.edge(8, 6, 1500)
g.edge(7, 6, 500)

# Initial start and goal
start_node = 2
goal_node = 6

ucs(g, start_node, goal_node)
