import tdl
from input_handlers import handle_keys


def main():
    screen_width = 80
    screen_height = 50

    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    tdl.set_font('font/qbicfeet_10x10.png', columnFirst=False, greyscale=False)

    # Creates separate consoles from the root
    # Cria um console separado do root
    root_console = tdl.init(screen_width, screen_height, title='Advanced Calabouços & Cachorros')
    con = tdl.Console(screen_width, screen_height)

    while not tdl.event.is_window_closed():
        # Creates the character on the console and blit it on the root
        # Cria o carácter no console e exibe o console no root
        con.draw_char(player_x, player_y, '@', bg=None, fg=(255, 255, 255))
        root_console.blit(con, 0, 0, screen_width, screen_height, 0, 0)
        tdl.flush()

        # Clear the character after the movement
        # Limpar o carácter depois do movimento
        con.draw_char(player_x, player_y, ' ', bg=None)

        # Get the user input, if any
        # Pega a entrada do usuário, se existir alguma
        for event in tdl.event.get():
            if event.type == 'KEYDOWN':
                user_input = event
                break
        else:
            user_input = None

        if not user_input:
            continue

        # Manage the input and do the designated action
        # Trata a entrada e faz a ação designada
        action = handle_keys(user_input)

        move = action.get('move')
        exit_game = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move:
            dx, dy = move
            player_x += dx
            player_y += dy

        if exit_game:
            return True

        if fullscreen:
            tdl.set_fullscreen(not tdl.get_fullscreen())


if __name__ == '__main__':
    main()
