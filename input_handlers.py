import tcod as libtcod

def handle_keys(key):
    if key.vk == libtcod.KEY_UP:
        return {'move': (0, -1)}
    elif key.vk == libtcod.KEY_DOWN:
        return {'move': (0, 1)}
    elif key.vk == libtcod.KEY_LEFT:
        return {'move': (-1, 0)}
    elif key.vk == libtcod.KEY_RIGHT:
        return {'move': (1, 0)}
    
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        return {'fullscreen': True}
    elif key.vk == libtcod.KEY_ESCAPE:
        return {'exit': True}
    
    return {}

    # Vim keys to move diagonaly
    # if user_input.key == 'UP' or key_char == 'k':
    #     return {'move': (0, -1)}
    # elif user_input.key == 'DOWN' or key_char == 'j':
    #     return {'move': (0, 1)}
    # elif user_input.key == 'LEFT' or key_char == 'h':
    #     return {'move': (-1, 0)}
    # elif user_input.key == 'RIGHT' or key_char == 'l':
    #     return {'move': (1, 0)}
    # elif key_char == 'y':
    #     return {'move': (-1, -1)}
    # elif key_char == 'u':
    #     return {'move': (1, -1)}
    # elif key_char == 'b':
    #     return {'move': (-1, 1)}
    # elif key_char == 'n':
    #     return {'move': (1, 1)}

    # if user_input.key == 'ENTER' and user_input.alt:
    #     return {'fullscreen': True}
    # elif user_input.key == 'ESCAPE':
    #     return {'exit': True}

    # return {}
