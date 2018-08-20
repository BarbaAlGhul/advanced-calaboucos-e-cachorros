from numpy.random import random_integers


class Rect:
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h

    def center(self):
        center_x = int((self.x1 + self.x2) / 2)
        center_y = int((self.y1 + self.y2) / 2)
        return center_x, center_y

    def intersect(self, other):
        # Return true if this rectangle intersects with another one
        # Retorna verdadeiro se este retângulo intercepta com outro
        return (self.x1 <= other.x2 and self.x2 >= other.x1 and
                self.y1 <= other.y2 and self.y2 >= other.y1)


def create_room(game_map, room):
    # Go through the tiles in the rectangle and make them passable
    # Percorre os tiles do retângulo e os transforma em 'passáveis'
    for x in range(room.x1 + 1, room.x2):
        for y in range(room.y1 + 1, room.y2):
            game_map.walkable[x, y] = True
            game_map.transparent[x, y] = True


def create_h_tunnel(game_map, x1, x2, y):
    for x in range(min(x1, x2), max(x1, x2) + 1):
        game_map.walkable[x, y] = True
        game_map.transparent[x, y] = True


def create_v_tunnel(game_map, y1, y2, x):
    for y in range(min(y1, y2), max(y1, y2) + 1):
        game_map.walkable[x, y] = True
        game_map.transparent[x, y] = True


def make_map(game_map, max_rooms, room_min_size, room_max_size, map_width, map_height, player):
    rooms = []
    num_rooms = 0

    for r in range(max_rooms):
        # Random width and height
        # Largura e altura aleatórios
        w = random_integers(room_min_size, room_max_size)
        h = random_integers(room_min_size, room_max_size)
        # Random position whitout going out the bondaries of the map
        # Posição aleatória sem sair dos limites do mapa
        x = random_integers(0, map_width - w - 1)
        y = random_integers(0, map_height - h - 1)

        # Rect class makes rectangles easier to work with
        # A classe Rect faz ficar mais fácil trabalhar com retângulos
        new_room = Rect(x, y, w, h)

        # Run through the other rooms and see if they intersect with this one
        for other_room in rooms:
            if new_room.intersect(other_room):
                break
        else:
            # This means that there is no intersection, so it's valid
            # Isto significa que não há interseção, então é válido

            # 'Paint' it to the map's tiles
            # 'Desenha' ela nos tiles do mapa
            create_room(game_map, new_room)

            # Center the coordinates of the new room
            # Centraliza as coordenadas da nova sala
            (new_x, new_y) = new_room.center()

            if num_rooms == 0:
                # This is the first room, where the player starts at
                # Esta é a primeira sala, onde o jogador começa
                player.x = new_x
                player.y = new_y
            else:
                # All rooms after the first:
                # connect it to the previous room with a tunnel
                # Todas as salas após a primeira:
                # conecta a sala atual com a sala anterior através de um túnel

                # Center coordinates of the previous room
                # Coordenadas centrais da sala anterior
                (prev_x, prev_y) = rooms[num_rooms - 1].center()

                # Flip a coin (random number that is either 0 or 1)
                # Joga uma moeda (número aleatório que é 0 ou 1)
                if random_integers(0, 1) == 1:
                    # First move horizontally than vertically
                    # Primeiro move horizontalmente depois verticalmente
                    create_h_tunnel(game_map, prev_x, new_x, prev_y)
                    create_v_tunnel(game_map, prev_y, new_y, new_x)
                else:
                    # First move vertically than horizontally
                    # Primeiro move verticalmente depois horizontalmente
                    create_v_tunnel(game_map, prev_y, new_y, prev_x)
                    create_h_tunnel(game_map, prev_x, new_x, new_y)

        # Finally, append the new room to the list
        # Por fim acrescenta a sala nova à lista
        rooms.append(new_room)
        num_rooms += 1
