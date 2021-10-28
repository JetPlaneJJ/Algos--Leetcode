from collections import defaultdict
from queue import PriorityQueue
import math

# Assume all vertices are reachable to each other. All nodes have a unique value.
# Graphs may have cycles.
class TreeAndGraph:
    def __init__(self, max_nodes: int):
        self.visitedNodes = set()
        self.graph1 = { # no cycles, Node -> points to
            'A' : ['B','C'],
            'B' : ['D', 'E'],
            'C' : ['F'],
            'D' : [],
            'E' : ['F'],
            'F' : []
        }
        self.customGraph = defaultdict(list)
        self.edgeCosts = [[-1 for i in range(max_nodes)] for j in range(max_nodes)]

    # Adds a oneway edge, from u to v, onto the custom graph
    def addEdge(self, u, v, weight) -> None:
        self.customGraph[u].append(v)
        self.edgeCosts[u][v] = weight

    # Resets all graphs and queues
    def reset(self) -> None:
        self.visitedNodes.clear()
        self.customGraph.clear()

#--------------------------------------------------------------------------------------------------
    # Depth First Search: 1) Pick a starting node 2) If newly seen, add to visited 
    # 3) do the same for adjacent neighbors, recurse.
    def dfs(self, graph, node: str) -> None:
        if node not in self.visitedNodes:
            print(node, end="")
            self.visitedNodes.add(node)
            for adj in graph[node]:
                self.dfs(graph, adj)

#--------------------------------------------------------------------------------------------------
    # Breadth First Search: explore rings of the same distance from the start node at a time
    def bfs(self, graph, node) -> None: # node may be an int or string
        bfsQueue = []
        bfsQueue.append(node) # mark starting node as visited
        self.visitedNodes.add(node)
        while bfsQueue: # there are vertices left to explore
            current = bfsQueue.pop()
            print(current, end="")
            for neighbor in graph[current]:
                if neighbor not in self.visitedNodes: # newly found
                    bfsQueue.append(neighbor)
                    self.visitedNodes.add(neighbor)

#--------------------------------------------------------------------------------------------------
    # Dijkstra's Algorithm. Assumes the nodes are named by int.
    def dijkstra(self, graph, num_vertices: int, start_node: int) -> None:
        shortestCosts = [math.inf for i in range(0, num_vertices)] # best costs, start to node
        shortestCosts[start_node] = 0

        pq = PriorityQueue() # tracks the next shortest distance vertex to look at
        pq.put((0, start_node))
        parents = [-1] * (num_vertices) # tracks the BEST/SHORTEST PATH parent of node
        
        while not pq.empty():
            (total_cost, curr_node) = pq.get()
            self.visitedNodes.add(curr_node)
            for neighbor in graph[curr_node]:
                if neighbor not in self.visitedNodes: # if not already expanded upon
                    old_cost = shortestCosts[neighbor]
                    new_cost = shortestCosts[curr_node] + self.edgeCosts[curr_node][neighbor] 
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        shortestCosts[neighbor] = new_cost
                        parents[neighbor] = curr_node

        for vertex in range(0, num_vertices):
            print("Distance from 0 to", vertex, "is", shortestCosts[vertex])
            print("     Path: ", end="")
            self.printBestPathFromStart(parents, vertex)
            print()
    
    # Prints the shortest route from start to given node, left to right order
    def printBestPathFromStart(self, parents, node):
        if parents[node] == -1: # starting node
            print(node, end="")
            return
        self.printBestPathFromStart(parents, parents[node]) # go all the way to beginning
        print(node, end="")
