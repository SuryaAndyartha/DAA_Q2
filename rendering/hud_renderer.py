import pygame

import config.colors as colors

from config.settings import W, H, ROWS, GAME_DURATION

def draw_hud(
    surf,
    font,
    score,
    time_left
):
    hud_y = ROWS * H // (ROWS + 1)

    pygame.draw.rect(
        surf,
        colors.C_HUD,
        (0, hud_y, W, 80)
    )

    sc_lbl = font.render(
        f"Score: {score}",
        True,
        colors.C_YELLOW
    )

    surf.blit(
        sc_lbl,
        (20, hud_y + 20)
    )

    bar_w = int(
        (
            time_left
            / GAME_DURATION
        )
        * (W - 200)
    )

    if time_left > 20:
        bar_col = colors.C_GREEN
    elif time_left > 10:
        bar_col = colors.C_ORANGE
    else:
        bar_col = colors.C_RED

    pygame.draw.rect(
        surf,
        (80, 80, 80),
        (
            180,
            hud_y + 28,
            W - 200,
            24
        ),
        border_radius=6
    )

    pygame.draw.rect(
        surf,
        bar_col,
        (
            180,
            hud_y + 28,
            bar_w,
            24
        ),
        border_radius=6
    )

    t_lbl = font.render(
        f"{int(time_left)}s",
        True,
        colors.C_WHITE
    )

    surf.blit(
        t_lbl,
        (
            W - 60,
            hud_y + 28
        )
    )


def draw_game_over(
    surf,
    font,
    font_sm,
    score
):
    overlay = pygame.Surface(
        (W, H),
        pygame.SRCALPHA
    )

    overlay.fill((0, 0, 0, 160))

    surf.blit(overlay, (0, 0))

    go = font.render(
        "GAME OVER",
        True,
        colors.C_RED
    )

    sc = font.render(
        f"Final Score: {score}",
        True,
        colors.C_YELLOW
    )

    hint = font_sm.render(
        "Close the window to exit.",
        True,
        colors.C_WHITE
    )

    surf.blit(
        go,
        go.get_rect(
            center=(W // 2, H // 2 - 30)
        )
    )

    surf.blit(
        sc,
        sc.get_rect(
            center=(W // 2, H // 2 + 20)
        )
    )

    surf.blit(
        hint,
        hint.get_rect(
            center=(W // 2, H // 2 + 60)
        )
    )