from components.ai import HostileEnemy, BaseAI
from components import consumable, equipable
from components.equipment import Equipment
from components.fighter import Fighter
from components.inventory import Inventory
from components.level import Level
from entity import Actor, Item

player = Actor(
    char="@", 
    color=(255, 255, 255), 
    name="Player", 
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=30, defense=2, power=5),
    inventory=Inventory(capacity=26),
    level=Level(level_up_base=200)
)

goblin = Actor(
    char="g", 
    color=(63, 127, 63), 
    name="Goblin",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=10, defense=1, power=4),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=50)
)

orc = Actor(
    char="o", 
    color=(0, 127, 0), 
    name="Orc",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=15, defense=2, power=7),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=100)
)

kobold = Actor(
    char="k",
    color=(210, 105, 30),
    name="Kobold",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=6, defense=1, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=25)
)

health_potion = Item(
    char="!",
    color=(127, 0, 255),
    name="Health Potion",
    consumable=consumable.HealingConsumable(amount=6)
)

lightning_scroll = Item(
    char="~",
    color=(255, 255, 0),
    name="Lightning Scroll",
    consumable=consumable.LightningDamageConsumable(damage=20, maximum_range=5)
)

confusion_scroll = Item(
    char="~",
    color=(207, 63, 255),
    name="Confusion Scroll",
    consumable=consumable.ConfusionConsumable(number_of_turns=10)
)

fireball_scroll = Item(
    char="~",
    color=(255, 0, 0),
    name="Fireball Scroll",
    consumable=consumable.FireballDamageConsumable(damage=12, radius=3)
)

dagger = Item(
    char="/",
    color=(0, 191, 255),
    name="Dagger",
    equipable=equipable.Dagger()
)

sword = Item(
    char="|",
    color=(0, 191, 255),
    name="Sword",
    equipable=equipable.Sword()
)

leather_armor = Item(
    char="[",
    color=(139, 69, 19),
    name="Leather Armor",
    equipable=equipable.LeatherArmor()
)

chain_mail = Item(
    char="[",
    color=(160, 160, 160),
    name="Chain Mail",
    equipable=equipable.ChainMail()
)
