from config.settings import GAME_DURATION

from entities.courier import Courier

from systems.customer_spawner import spawn_customer

class GameState:
    def __init__(self):
        self.score = 0

        self.time_left = float(GAME_DURATION)

        self.customers = [spawn_customer()]

        self.courier = Courier()

        self.dragging_c = None
        self.drag_pos = (0, 0)

        self.active_path = []

        self.game_over = False

        self.last_path_flavour = None

        self.delivering = False

        self.notifications = []
    
    def add_notification(self, text, x, y):
        self.notifications.append({
            "text": text,
            "x": x,
            "y": y,
            "timer": 1.2,
            "alpha": 255
        }
        )