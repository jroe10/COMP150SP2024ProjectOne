from enum import Enum

class EventStatus(Enum):
    UNKNOWN = "unknown"
    PASS = "pass"
    FAIL = "fail"
    PARTIAL = "partial pass"

class CharacterStatus(Enum):
    ALIVE = "alive"
    DEAD = "dead"
    INJURED = "injured"

MAX_HEALTH = 100
MIN_HEALTH = 0

class HealthStatus:
    def __init__(self, current_health):
        self.current_health = current_health

    def heal(self, amount):
        self.current_health = min(self.current_health + amount, MAX_HEALTH)

    def take_damage(self, amount):
        self.current_health = max(self.current_health - amount, MIN_HEALTH)

def is_critical_health(health):
    return health < 20