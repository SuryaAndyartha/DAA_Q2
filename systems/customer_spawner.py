import random

from entities.customer import Customer
from config.settings import ROWS, COLS
from config.map_data import ROAD_MAP, FLAVOURS

def nearest_road_cell(row, col):
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = row + dr, col + dc

        if 0 <= nr < ROWS and 0 <= nc < COLS:
            if ROAD_MAP[nr][nc] == 1:
                return (nr, nc)
    
    return None

def spawn_customer():
    road_cells = [
        (r, c)
        for r in range(ROWS)
        for c in range(COLS)
        if ROAD_MAP[r][c] == 0
        and nearest_road_cell(r, c) is not None
    ]

    r, c = random.choice(road_cells)

    flavour = random.choice(list(FLAVOURS.keys()))

    return Customer(r, c, flavour)