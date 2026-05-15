import pygame

import config.colors as colors

from config.settings import CELL
from config.map_data import FLAVOURS


class Courier:
    SPEED = 10

    def __init__(self):
        self.path = []
        self.active = False
        self.step_idx = 0
        self.pixel_pos = None
        self.target_px = None
        self.flavour = None
        self.progress = 0.0

    def dispatch(self, path, flavour):
        if len(path) < 2:
            return

        self.path = path
        self.step_idx = 0
        self.active = True
        self.flavour = flavour
        self.progress = 0.0

        r, c = path[0]

        self.pixel_pos = [
            c * CELL + CELL // 2,
            r * CELL + CELL // 2
        ]

    def update(self, dt):
        if not self.active:
            return

        if self.step_idx >= len(self.path) - 1:
            self.active = False
            return

        self.progress += self.SPEED * dt

        if self.progress >= 1.0:
            self.progress = 0.0
            self.step_idx += 1

            if self.step_idx >= len(self.path) - 1:
                self.active = False

                r, c = self.path[-1]

                self.pixel_pos = [
                    c * CELL + CELL // 2,
                    r * CELL + CELL // 2
                ]

                return

        r0, c0 = self.path[self.step_idx]
        r1, c1 = self.path[self.step_idx + 1]

        t = self.progress

        self.pixel_pos = [
            (c0 + (c1 - c0) * t) * CELL + CELL // 2,
            (r0 + (r1 - r0) * t) * CELL + CELL // 2,
        ]

    def draw(self, surf):
        if not self.active or self.pixel_pos is None:
            return

        col = FLAVOURS.get(
            self.flavour,
            (255, 255, 255)
        )

        x = int(self.pixel_pos[0])
        y = int(self.pixel_pos[1])

        pygame.draw.rect(
            surf,
            col,
            (x - 14, y - 9, 28, 18),
            border_radius=5
        )

        pygame.draw.rect(
            surf,
            colors.C_BLACK,
            (x - 14, y - 9, 28, 18),
            2,
            border_radius=5
        )

        pygame.draw.rect(
            surf,
            (180, 230, 255),
            (x - 8, y - 8, 16, 10),
            border_radius=3
        )

        for wx, wy in [
            (-9, 9),
            (9, 9),
            (-9, -9),
            (9, -9)
        ]:
            pygame.draw.circle(
                surf,
                colors.C_BLACK,
                (x + wx, y + wy),
                4
            )