class Entity:
    # A generic object to represent players, enemies, items, etc
    # Um objeto genérico representando jogadores, inimigos, items, etc
    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx, dy):
        # Move the entity by a given amount
        # Move a entidade dada uma quantidade
        self.x += dx
        self.y += dy
