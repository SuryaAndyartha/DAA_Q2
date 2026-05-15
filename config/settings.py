import pygame

pygame.init()

info = pygame.display.Info()
SCREEN_W = info.current_w
SCREEN_H = info.current_h

MARGIN = 100
UI_BAR = 80

COLS = 27
ROWS = 21

CELL = min(
    (SCREEN_W - MARGIN) // COLS,
    (SCREEN_H - MARGIN - UI_BAR) // ROWS
)

W = COLS * CELL
H = ROWS * CELL + UI_BAR

FPS = 60
GAME_DURATION = 90
