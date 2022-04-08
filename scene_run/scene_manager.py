scene_dict = {}
game = "GAME"
menu = "MENU"
settings = "SET"

next_scene = None
running = True


def change_scene(key):
    global running, next_scene
    running = False
    next_scene = scene_dict[key]
