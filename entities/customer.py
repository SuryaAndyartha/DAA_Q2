import pygame
import math
import random

import config.colors as colors

from config.settings import CELL
from config.map_data import FLAVOURS, FLAVOUR_EMOJI, CUSTOMER_EMOJIS


class Customer:
    def __init__(self, row, col, flavour):
        self.row = row
        self.col = col
        self.flavour = flavour
        self.dragging = False
        self.done = False
        self.animation_timer = 0.0
        self.waiting_courier = False    
        self.person_emoji = random.choice(CUSTOMER_EMOJIS)# pick random person emoji

    def cell_center(self):
        return (
            self.col * CELL + CELL // 2,
            self.row * CELL + CELL // 2
        )

    def update(self, dt):
        self.animation_timer += dt

    def _draw_emoji(self, surf, emoji, cx, cy, size=22):
        font = pygame.font.SysFont("segoeuiemoji,applesymbols,symbola,notocoloremoji", size)
        text = font.render(emoji, True, (0, 0, 0))
        rect = text.get_rect(center=(cx, cy))
        surf.blit(text, rect)

    def draw(self, surf, font_sm):
        cx, cy = self.cell_center()

        pulse = math.sin(self.animation_timer * 4.0)
        offset_y = int(pulse * 3)  

        self._draw_emoji(surf, self.person_emoji, cx, cy + offset_y, size=24)# draw person emoji 

        # draw request bubble above
        bx = cx
        by = cy - 28 + offset_y
        if by < 14:
            by = cy + 28 + offset_y  

        col = FLAVOURS[self.flavour]
        item_emoji = FLAVOUR_EMOJI.get(self.flavour, "?")

        # bubble background
        pygame.draw.rect(
            surf,
            col,
            (bx - 18, by - 14, 36, 28),
            border_radius=8
        )
        pygame.draw.rect(
            surf,
            colors.C_BLACK,
            (bx - 18, by - 14, 36, 28),
            2,
            border_radius=8
        )

        self._draw_emoji(surf, item_emoji, bx, by, size=18) # item emoji inside bubble

    def on_order_dispatched(self):
        self.waiting_courier = True

    def on_courier_returned(self):
        self.done = True
