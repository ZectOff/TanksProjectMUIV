

class Game_stats():
    """Отслеживание статистики в игре"""
    def __init__(self):
        """Инициализация статистики"""
        self.reset_stats()

    def reset_stats(self):
        """Статистика изменяющаяся во время игры"""
        self.tank_lifes = 3
        self.killed_enemies = 0
        self.briks_lifes = 1