from enum import Enum
# orientation 
class Direction(Enum):
    NORD = (0, -1)
    SUD = (0, 1)
    EST = (1, 0)
    OUEST = (-1, 0)

# Utilisation
dx, dy = Direction.NORD.value
x, y = 5, 5
x += dx
y += dy