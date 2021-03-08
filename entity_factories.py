from components.ai import HostileEnemy, BaseAI
from components.consumable import HealingConsumable
from components.fighter import Fighter
from entity import Actor, Item

player = Actor(
    char="@", 
    color=(255, 255, 255), 
    name="Player", 
    ai_cls=BaseAI,
    fighter=Fighter(hp=30, defense=2, power=5)
)

goblin = Actor(
    char="g", 
    color=(63, 127, 63), 
    name="Goblin",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3)
)

orc = Actor(
    char="o", 
    color=(0, 127, 0), 
    name="Orc",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=15, defense=1, power=5)
)

health_potion = Item(
    char="!",
    color=(127, 0, 255),
    name="Health Potion",
    consumable=HealingConsumable(amount=8)
)