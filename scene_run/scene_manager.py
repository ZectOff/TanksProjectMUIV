scene_dict = {}
game = "GAME"
menu = "MENU"
settings = "SET"

next_scene = None
running = True


def change_scene(key):
    global running, next_scene
    running = False
    print(key)
    next_scene = scene_dict[key]
    print(next_scene)
    print(scene_dict)
