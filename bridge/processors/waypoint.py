"""
Описание структуры путевой точки

Хранит:
- Координата путевой точки
- Желаемый угол поворота робота в точке
- Тип путевой точки
"""

import bridge.processors.auxiliary as aux
from enum import Enum

class WType(Enum):
    __ROBOT = -1 # хз, нужен в Route
    S_ENDPOINT = 0 # Двигаться в точку и остановиться (конечная точка пути)
    S_IGNOREOBSTACLES = 1 # Двигаться в точку игнорируя препятствия
    S_BALL_KICK = 2 # Захватить мяч и мгновенно его пнуть
    S_BALL_GRAB = 3 # Захватить мяч не пиная

    R_PASSTHROUGH = 4 # Двигаться в точку не останавливаясь (промежуточная точка пути)

    R_BALL_ALIGN = 5 # Выровнятся напротив мяча, приготовившись его захватить
    S_STOP = 6 # Kostil for stopping 
    __GRAVEYARD = 100

class Waypoint:
    def __init__(self, pos: aux.Point, angle: float, type: WType) -> None:
        self.pos = pos
        self.angle = angle
        self.type = type

    def __str__(self):
        return "WP: " + str(self.pos) + "; angle = %.2f"%self.angle + "; type = " + str(self.type)
