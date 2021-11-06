#--------------------------------------------------------------------------------------------------
# Author: Jay Lin
# Date: October 2021

# These are some problems that you may see in a technical interview.
# Patterns:
# 1) Sliding Windows (Fixed, Dynamic): "minimum subarray", "maximum contiguous avg sum"
# 2) Two Pointers (Regular, Fast/Slow): "find a pair (in sorted array)", "cyclic linked list"
# 3) Modified Binary Search: "find a target/find the min in a ROTATED and sorted array",
# 4) Backtracker: "find all possible solutions to a puzzle", "brute force path"
# 5) Merged Intervals
# 6) Tree and graph traversals (DFS, BFS, Dijkstra, A*): "find the shortest path"
# 7) Dynamic Programming:
# 8) other

# from TreeAndGraph import TreeAndGraph
from Backtracker import Backtracking

#--------------------------------------------------------------------------------------------------
# Backtracking test Problem N Queens
# backtracker = Backtracking()
# backtracker.solveNQueens(4)

#--------------------------------------------------------------------------------------------------
# Tree and Graph tests
# test = TreeAndGraph(100)

# print("--------------------------------DFS--------------------------------")
# test.dfs(test.graph1, 'A')
# print()
# test.reset()

# print("--------------------------------BFS--------------------------------")
# test.bfs(test.graph1, 'A')
# test.reset()

# print()
# test.addEdge(0, 1, 0)
# test.addEdge(0, 2, 0)
# test.addEdge(1, 2, 0)
# test.addEdge(2, 0, 0)
# test.addEdge(2, 3, 0)
# test.addEdge(3, 4, 0)
# test.bfs(test.customGraph, 2)
# print()

# print("--------------------------------Dijkstra's--------------------------------")
# test.reset()
# test.addEdge(0, 1, 1)
# test.addEdge(0, 2, 7)
# test.addEdge(1, 2, 2)
# test.addEdge(2, 0, 9)
# test.addEdge(2, 3, 5)
# test.addEdge(3, 4, 14)
# test.addEdge(4, 5, 6)
# test.addEdge(0, 5, 2)
# test.addEdge(2, 4, 1)
# test.addEdge(5, 6, 23)
# test.addEdge(4, 6, 3)
# test.dijkstra(test.customGraph, 7, 0)

# print("--------------------------------Permutations--------------------------------")
# permute = Backtracking()
# permute.permute("Andy")
