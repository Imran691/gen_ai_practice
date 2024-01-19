from model import Creature

_creatures: list[Creature] = [
    Creature(name="yeti",
    country="CN",
    area="Himalayas",
    description="Hirsute Himalayan",
    aka="Abominable Snowman"
    ),
    Creature(name="sasquatch",
    country="US",
    area="*",
    description="Yeti's Cousin Eddie",
    aka="Bigfoot")
]

# to return the above created list of creatures
def get_creatures() -> list[Creature]:
    return _creatures