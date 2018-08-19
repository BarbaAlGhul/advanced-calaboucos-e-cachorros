def handle_keys(user_input):

    # Movement keys
    # Teclas de movimentação
    if user_input.key == 'UP':
        return {'move': (0, -1)}
    elif user_input.key == 'DOWN':
        return {'move': (0, 1)}
    elif user_input.key == 'LEFT':
        return {'move': (-1, 0)}
    elif user_input.key == 'RIGHT':
        return {'move': (1, 0)}

    if user_input.key == 'ENTER' and user_input.alt:
        # Alt + Enter: toggle full screen
        # Alt + Enter: modo tela cheia
        return {'fullscreen': True}
    elif user_input.key == 'ESCAPE':
        # Exit the game
        # Sai do jogo
        return {'exit': True}

    # No key was pressed
    # Nenhuma tecla foi pressionada
    return {}
