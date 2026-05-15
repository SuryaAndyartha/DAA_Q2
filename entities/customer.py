import pygame
import math

import config.colors as colors

from config.settings import CELL
from config.map_data import FLAVOURS

class Customer:
    def __init__(self, row, col, flavour):
        self.row = row
        self.col = col
        self.flavour = flavour
        self.dragging = False
        self.done = False
        self.animation_timer = 0.0

    def cell_center(self):
        return (
            self.col * CELL + CELL // 2,
            self.row * CELL + CELL // 2
        )
    
    def update(self, dt):
        self.animation_timer += dt

    def draw(self, surf, font_sm):
        cx, cy = self.cell_center()

        pulse = math.sin(self.animation_timer * 4.0)
        radius = int(18 + pulse * 3)

        pygame.draw.circle(
            surf,
            (0, 0, 0),
            (cx + 3, cy + 3),
            radius
        )

        pygame.draw.circle(
            surf,
            (255, 200, 140),
            (cx, cy),
            radius
        )

        pygame.draw.circle(
            surf,
            colors.C_BLACK,
            (cx, cy),
            radius,
            2
        )

        col = FLAVOURS[self.flavour]

        bx = cx
        if cy - 32 < 10:
            by = cy + radius
        else:
            by = cy - radius

        pygame.draw.rect(
            surf,
            col,
            (bx - 22, by - 10, 44, 20),
            border_radius=8
        )

        pygame.draw.rect(
            surf,
            colors.C_BLACK,
            (bx - 22, by - 10, 44, 20),
            2,
            border_radius=8
        )

        label = font_sm.render(
            self.flavour[:3], 
            True, 
            colors.C_BLACK
        )

        surf.blit(
            label, 
            label.get_rect(center=(bx, by))
        )
