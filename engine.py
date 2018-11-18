import tdl

from input_handlers import handle_keys
from components.fighter import Fighter
from death_functions import kill_monster, kill_player
from entity import Entity, get_blocking_entities_at_location
from game_states import GameStates
from render_functions import render_all, clear_all
from map_utils import make_map, GameMap


def main():
    screen_width = 80
    screen_height = 50
    map_width = 80
    map_height = 45

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    fov_algorithm = 'BASIC'
    fov_light_walls = True
    fov_radius = 8

    max_monsters_per_room = 3

    colors = {
        'dark_wall': (0, 51, 0),
        'dark_ground': (38, 115, 38),
        'light_wall': (130, 110, 50),
        'light_ground': (200, 180, 50),
        'desaturated_blue': (83, 136, 237),
        'dark_blue': (0, 62, 124),
        'dark_red': (191, 0, 0)
    }

    # Declare the entities and hold them in a list
    # Declara as entidades e coloca elas em uma lista
    fighter_componente = Fighter(hp=30, defense=2, power=5)
    player = Entity(0, 0, '@', (255, 255, 255), 'Player', blocks=True, fighter=fighter_componente)
    entities = [player]

    tdl.set_font('font/qbicfeet_10x10.png', columnFirst=False, greyscale=False)

    # Creates separate consoles from the root
    # Cria um console separado do root
    root_console = tdl.init(screen_width, screen_height, title='Advanced Calabouços & Cachorros')
    con = tdl.Console(screen_width, screen_height)
    # Creates the map of the game
    # Cria o mapa do jogo
    game_map = GameMap(map_width, map_height)
    make_map(game_map, max_rooms, room_min_size, room_max_size, map_width, map_height, player, entities,
             max_monsters_per_room, colors)

    fov_recompute = True

    game_state = GameStates.PLAYERS_TURN

    while not tdl.event.is_window_closed():
        if fov_recompute:
            game_map.compute_fov(player.x, player.y, fov=fov_algorithm, radius=fov_radius, light_walls=fov_light_walls)

        render_all(con, entities, game_map, fov_recompute, root_console, screen_width, screen_height, colors)
        tdl.flush()

        clear_all(con, entities)

        fov_recompute = False

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

        player_turn_results = []

        if move and game_state == GameStates.PLAYERS_TURN:
            dx, dy = move
            destination_x = player.x + dx
            destination_y = player.y + dy
            if game_map.walkable[destination_x, destination_y]:
                target = get_blocking_entities_at_location(entities, destination_x, destination_y)

                if target:
                    attack_results = player.fighter.attack(target)
                    player_turn_results.extend(attack_results)
                else:
                    player.move(dx, dy)

                    fov_recompute = True

                game_state = GameStates.ENEMY_TURN

        if exit_game:
            return True

        if fullscreen:
            tdl.set_fullscreen(not tdl.get_fullscreen())

        for player_turn_result in player_turn_results:
            message = player_turn_result.get('message')
            dead_entity = player_turn_result.get('dead')

            if message:
                print(message)

            if dead_entity:
                if dead_entity == player:
                    message, game_state = kill_player(dead_entity, colors)
                else:
                    message = kill_monster(dead_entity, colors)

                print(message)

        if game_state == GameStates.ENEMY_TURN:
            for entity in entities:
                if entity.ai:
                    enemy_turn_results = entity.ai.take_turn(player, game_map, entities)

                    for enemy_turn_result in enemy_turn_results:
                        message = enemy_turn_result.get('message')
                        dead_entity = enemy_turn_result.get('dead')

                        if message:
                            print(message)

                        if dead_entity:
                            if dead_entity == player:
                                message, game_state = kill_player(dead_entity, colors)
                            else:
                                message = kill_monster(dead_entity, colors)

                            print(message)

                            if game_state == GameStates.PLAYER_DEAD:
                                break

                    if game_state == GameStates.PLAYER_DEAD:
                        break
            else:
                game_state = GameStates.PLAYERS_TURN


if __name__ == '__main__':
    main()
