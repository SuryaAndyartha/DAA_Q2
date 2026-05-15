import pygame

from config.settings import CELL
from config.map_data import SHOP_POS, ROAD_MAP

from systems.pathfinding import dijkstra

from systems.scoring import calculate_delivery_score, wrong_shop_penalty

from systems.customer_spawner import nearest_road_cell

def handle_input(events, state):
    for event in events:

        if state.game_over:
            continue

        if (event.type == pygame.MOUSEBUTTONDOWN 
            and event.button == 1):
            mx, my = event.pos

            for cust in state.customers:
                cx, cy = cust.cell_center()

                if (abs(mx - cx) < 20
                    and abs(my - cy) < 20
                    and not cust.done
                ):
                    state.dragging_c = cust
                    state.drag_pos = (
                        mx,
                        my
                    )
                    break

        elif (event.type == pygame.MOUSEMOTION
            and state.dragging_c
        ):
            state.drag_pos = event.pos

        elif (event.type == pygame.MOUSEBUTTONUP
            and event.button == 1
            and state.dragging_c
        ):
            mx, my = event.pos

            for name, (sc, sr) in (
                SHOP_POS.items()
            ):
                sx = (sc * CELL + CELL // 2)

                sy = (sr * CELL + CELL // 2)

                if (abs(mx - sx) < CELL // 2
                    and abs(my - sy) < CELL // 2
                ):

                    if (name == state.dragging_c.flavour):
                        delivery_target = nearest_road_cell(
                            state.dragging_c.row,
                            state.dragging_c.col
                        )

                        if delivery_target:
                            path = dijkstra(
                                ROAD_MAP,
                                (sr, sc),
                                delivery_target
                            )
                        else:
                            path = []

                        if path:
                            state.courier.dispatch(
                                path,
                                name
                            )

                            state.active_path = path

                            state.last_path_flavour = (
                                name
                            )
                        
                        state.delivering = True

                        state.score += (
                            calculate_delivery_score(
                                path
                            )
                        )

                        state.dragging_c.done = True

                        state.customers = [
                            c
                            for c
                            in state.customers
                            if not c.done
                        ]

                    else:
                        state.score = max(0, state.score - wrong_shop_penalty())

                        state.add_notification(
                            "Toko Salah! -5",
                            sx,
                            sy
                        )

                    break

            state.dragging_c = None