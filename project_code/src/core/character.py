import random

class Character:
    def __init__(self, name=None):
        """
        Core Stats: Everyone has these
        - Strength: How much you can lift. How strong you are. How hard you punch, etc.
        - Dexterity: How quick your limbs can perform intricate tasks. How adept you are at avoiding blows you anticipate. Impacts speed.
        - Constitution: The body's natural armor. Characters may have unique positive or negative constitutions that provide additional capabilities.
        - Vitality: A measure of how lively you feel. How many Hit Points you have. An indirect measure of age.
        - Endurance: How fast you recover from injuries. How quickly you recover from fatigue.
        - Intelligence: How smart you are. How quickly you can connect the dots to solve problems. How fast you can think.
        - Wisdom: How effectively you can make choices under pressure. Generally low in younger people.
        - Knowledge: How much you know? This is a raw score for all knowledge. Characters may have specific areas of expertise with a bonus or deficit in some areas.
        - Willpower: How quickly or effectively the character can overcome natural urges. How susceptible they are to mind control.
        - Spirit: Catchall for the ability to perform otherworldly acts. High spirit is rare. Different skills have different resource pools they might use like mana, stamina, etc. These are unaffected by spirit. Instead, spirit is a measure of how hard it is to learn new otherworldly skills and/or master general skills.
        """
        self.name = self._generate_name() if name is None else name
        self.strength = Statistic()
        self.dexterity = Statistic()
        self.constitution = Statistic()
        self.vitality = Statistic()
        self.endurance = Statistic()
        self.intelligence = Statistic()
        self.wisdom = Statistic()
        self.knowledge = Statistic()
        self.willpower = Statistic()
        self.spirit = Statistic()

    def _generate_name(self):
        names = ['Jen', 'Phoebe', Therese', 'Larry', 'Arjun']
        return random.choice(names)

class Statistic:
    def __init__(self, value=None):
        if value is None:
            self.value = self._generate_starting_value()
        else:
            self.value = value

    def _generate_starting_value(self):
        """Generate a starting value for the statistic based on a random number."""
        return random.randint(1, 100)