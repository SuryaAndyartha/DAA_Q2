import heapq


def dijkstra(grid, start, end):
    rows = len(grid)
    cols = len(grid[0])

    dist = {start: 0}
    prev = {start: None}
    pq = [(0, start)]

    while pq:
        cost, node = heapq.heappop(pq)

        if node == end:
            break

        if cost > dist.get(node, float("inf")):
            continue

        r, c = node

        for dr, dc in [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]:
            nr = r + dr
            nc = c + dc

            if (
                0 <= nr < rows
                and 0 <= nc < cols
                and grid[nr][nc] == 1
            ):
                new_cost = cost + 1

                if new_cost < dist.get(
                    (nr, nc),
                    float("inf")
                ):
                    dist[(nr, nc)] = new_cost
                    prev[(nr, nc)] = node

                    heapq.heappush(
                        pq,
                        (new_cost, (nr, nc))
                    )

    path = []
    node = end

    while node is not None:
        path.append(node)
        node = prev.get(node)

    path.reverse()

    return (
        path
        if path and path[0] == start
        else []
    )