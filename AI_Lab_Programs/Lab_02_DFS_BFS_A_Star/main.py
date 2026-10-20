"""Lab 2: DFS, BFS and A* on a small graph."""

from collections import deque
import heapq


def dfs(graph, start, goal):
    """Return a path found by depth-first search, or None."""
    stack = [(start, [start])]
    visited = set()

    while stack:
        node, path = stack.pop()
        if node == goal:
            return path
        if node in visited:
            continue
        visited.add(node)

        # Reverse keeps the displayed traversal easy to follow.
        for neighbour in reversed(graph.get(node, [])):
            if neighbour not in visited:
                stack.append((neighbour, path + [neighbour]))
    return None


def bfs(graph, start, goal):
    """Return a shortest path in an unweighted graph, or None."""
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path
        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, path + [neighbour]))
    return None


def a_star(graph, start, goal, heuristic):
    """A* for graph represented as {node: [(neighbour, edge_cost), ...]}."""
    frontier = [(heuristic.get(start, 0), 0, start, [start])]
    best_cost = {start: 0}

    while frontier:
        _, cost_so_far, node, path = heapq.heappop(frontier)
        if node == goal:
            return path, cost_so_far
        if cost_so_far > best_cost.get(node, float("inf")):
            continue

        for neighbour, edge_cost in graph.get(node, []):
            new_cost = cost_so_far + edge_cost
            if new_cost < best_cost.get(neighbour, float("inf")):
                best_cost[neighbour] = new_cost
                priority = new_cost + heuristic.get(neighbour, 0)
                heapq.heappush(
                    frontier, (priority, new_cost, neighbour, path + [neighbour])
                )
    return None, float("inf")


def main():
    # Unweighted graph for DFS and BFS.
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["G"],
        "F": ["G"],
        "G": [],
    }
    start, goal = "A", "G"
    print("DFS path:", dfs(graph, start, goal))
    print("BFS path:", bfs(graph, start, goal))

    # Weighted graph for A*.
    weighted_graph = {
        "A": [("B", 1), ("C", 4)],
        "B": [("D", 2), ("E", 5)],
        "C": [("E", 1)],
        "D": [("G", 5)],
        "E": [("G", 2)],
        "G": [],
    }
    heuristic = {"A": 4, "B": 4, "C": 2, "D": 4, "E": 1, "G": 0}
    path, cost = a_star(weighted_graph, start, goal, heuristic)
    print("A* path:", path)
    print("A* path cost:", cost)


if __name__ == "__main__":
    main()
