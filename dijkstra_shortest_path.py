from collections import defaultdict

def shortest_path(edges, src, dest):
    nodes = set()
    for a, b, _ in edges:
        nodes.add(a)
        nodes.add(b)
    dists = { node: float('inf') for node in nodes }
    descendants = defaultdict(list)
    for a, b, wt in edges:
        descendants[a].append((b, wt))
    dists[dest] = 0
    path = set()
    completed = set()
    completed.add(dest)


    def visit(next):
        min_dist = float('inf')
        if next in completed:
            return dists[next]
        for dsc, edge_wt in descendants[next]:
            if dsc not in path:
                path.add(dsc)
                dsc_dest_len = visit(dsc)
                min_dist = min(min_dist, edge_wt + dsc_dest_len)
                path.remove(dsc)
        completed.add(next)
        dists[next] = min_dist
        return min_dist

    return visit(src)


if __name__ == "__main__":
    from testing import test_case

    edges = [
        ('A', 'B', 1),
        ('A', 'C', 2),
        ('B', 'A', 2),
        ('C', 'D', 1),
        ('C', 'B', 1),
        ('B', 'D', 3),
        ('D', 'E', 1),
        ('B', 'E', 4),
        ('C', 'F', 1),
        ('F', 'E', 1),
        ('J', 'E', 6),
        ('G', 'E', 6),
        ('R', 'E', 6),
        ('N', 'E', 6),
        ('A', 'N', 0),
    ]

    test_case(
        "It should return the shortest path",
        shortest_path(edges, 'D', 'N'),
        float('inf')
    )

    test_case(
        "It should return the shortest path",
        shortest_path(edges, 'A', 'A'),
        0
    )

    test_case(
        "It should return the shortest path",
        shortest_path(edges, 'A', 'E'),
        4
    )
    
    test_case(
        "It should return the shortest path",
        shortest_path(edges, 'C', 'E'),
        2
    )