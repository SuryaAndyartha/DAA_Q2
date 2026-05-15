import pygame

import config.colors as colors

from config.settings import CELL, ROWS, COLS

from config.map_data import ROAD_MAP, SHOP_POS, FLAVOURS, FLAVOUR_EMOJI

def draw_city(surf):
    for r in range(ROWS):
        for c in range(COLS):
            rect = pygame.Rect(
                c * CELL,
                r * CELL,
                CELL,
                CELL
            )

            if ROAD_MAP[r][c] == 1:
                pygame.draw.rect(
                    surf,
                    colors.C_ROAD,
                    rect
                )

                pygame.draw.rect(
                    surf,
                    colors.C_GRID,
                    rect,
                    1
                )

            else:
                pygame.draw.rect(
                    surf,
                    (160, 130, 90),
                    rect
                )

                pygame.draw.rect(
                    surf,
                    (140, 110, 70),
                    rect,
                    1
                )

def _draw_emoji(surf, emoji, cx, cy, size=18):
    font = pygame.font.SysFont("segoeuiemoji,applesymbols,symbola,notocoloremoji", size)
    text = font.render(emoji, True, (0, 0, 0))
    surf.blit(text, text.get_rect(center=(cx, cy)))

def draw_shops(surf, font_sm):
    for name, (sc, sr) in SHOP_POS.items():
        col = FLAVOURS[name]

        x = sc * CELL
        y = sr * CELL

        pygame.draw.rect(
            surf,
            col,
            (
                x + 4,
                y + 4,
                CELL - 8,
                CELL - 8
            ),
            border_radius=4
        )

        pygame.draw.rect(
            surf,
            colors.C_BLACK,
            (
                x + 4,
                y + 4,
                CELL - 8,
                CELL - 8
            ),
            2,
            border_radius=4
        )

        roof_points = [
            (x + CELL // 2, y - 6),
            (x + 2, y + 6),
            (x + CELL - 2, y + 6),
        ]

        pygame.draw.polygon(surf, col, roof_points)
        pygame.draw.polygon(surf, colors.C_BLACK, roof_points, 2)

        board_cx = x + CELL // 2
        board_cy = y - 20

        lbl = font_sm.render(
            name,
            True,
            colors.C_BLACK
        )

        lbl_w = lbl.get_width()
        pad = 3.5

        board_w = lbl_w + pad * 2
        board_half = board_w // 2
        
        pygame.draw.rect(surf, colors.C_WHITE,
            (board_cx - board_half, board_cy - 2, board_w, 16),
            border_radius=4)
        pygame.draw.rect(surf, col,
            (board_cx - board_half, board_cy - 2, board_w, 16),
            2, 
            border_radius=4)

        surf.blit(lbl, lbl.get_rect(center=(board_cx, board_cy + 6)))

        for lx in [x + 8, x + CELL - 8]:
            pygame.draw.circle(surf, colors.C_YELLOW, (lx, y + 8), 4)
            pygame.draw.circle(surf, colors.C_BLACK, (lx, y + 8), 4, 1)

        pygame.draw.circle(
            surf,
            colors.C_WHITE,
            (
                x + CELL // 2,
                y + 4
            ),
            6
        )

        emoji = FLAVOUR_EMOJI.get(name, "?")
        _draw_emoji(
            surf,
            emoji,
            x + CELL // 2,
            y + CELL // 2 + 4,
            size=14 # size emoji on shop
        )


def draw_path(
    surf,
    path,
    flavour
):
    if len(path) < 2:
        return

    col = FLAVOURS.get(
        flavour,
        (255, 255, 255)
    )

    for i in range(len(path) - 1):
        r0, c0 = path[i]
        r1, c1 = path[i + 1]

        pygame.draw.line(
            surf,
            col,
            (
                c0 * CELL + CELL // 2,
                r0 * CELL + CELL // 2
            ),
            (
                c1 * CELL + CELL // 2,
                r1 * CELL + CELL // 2
            ),
            4
        )
