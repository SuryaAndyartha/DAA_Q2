import pygame
import sys

import config.colors as colors

from config.settings import W, H, FPS

from rendering.city_renderer import draw_city, draw_shops, draw_path

from rendering.hud_renderer import draw_hud, draw_game_over

from game.game_state import GameState

from game.input_handler import handle_input

from config.map_data import FLAVOURS

from systems.customer_spawner import spawn_customer


def run_game():
    surf = pygame.display.set_mode(
        (W, H)
    )

    pygame.display.set_caption(
        "Courier Service Game"
    )

    font = pygame.font.SysFont(
        "Arial",
        22,
        bold=True
    )

    font_sm = pygame.font.SysFont(
        "Arial",
        14,
        bold=True
    )

    clock = pygame.time.Clock()

    state = GameState()

    while True:
        dt = (clock.tick(FPS) / 1000.0)

        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        handle_input(events, state)

        if not state.game_over:

            if not state.delivering:
                state.time_left -= dt

                if state.time_left <= 0:
                    state.time_left = 0
                    state.game_over = True
            
            state.courier.update(dt)

            if (state.delivering
                and state.courier.delivered
                and not state.courier.active
            ):
                state.delivering = False
                state.active_path = []

                state.customers = [
                    c for c in state.customers
                    if not c.waiting_courier
                ]
                state.customers.append(spawn_customer())

        surf.fill(colors.C_BG)

        draw_city(surf)

        if state.active_path:
            draw_path(surf, state.active_path, state.last_path_flavour)

        draw_shops(surf, font_sm)

        state.courier.draw(surf)

        for cust in state.customers:
            cust.draw(surf, font_sm)
            cust.update(dt)

        draw_hud(surf, font, state.score, state.time_left)

        if state.dragging_c:
            col = FLAVOURS[
                state.dragging_c.flavour
            ]

            dx, dy = state.drag_pos

            pygame.draw.circle(
                surf,
                col,
                (dx, dy),
                18
            )

            pygame.draw.circle(
                surf,
                colors.C_BLACK,
                (dx, dy),
                18,
                2
            )

            lbl = font_sm.render(
                state.dragging_c.flavour[:3],
                True,
                colors.C_BLACK
            )

            surf.blit(
                lbl,
                lbl.get_rect(
                    center=(dx, dy)
                )
            )

        if state.game_over:
            draw_game_over(surf, font, font_sm, state.score)

        pygame.display.flip()
