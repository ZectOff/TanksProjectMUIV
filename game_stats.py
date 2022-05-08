class GameStats:
    """Отслеживание статистики в игре"""
    def __init__(self):
        """Инициализация статистики"""
        self.tank_lifes = 3
        self.base_lifes = 1
        self.brick_lifes = 2
        self.killed_enemies = 0
        self.score = 0