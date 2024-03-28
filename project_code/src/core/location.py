class Location:
    def __init__(self, name=None, description=None, x=0, y=0):
        self.name = Name(self, name)
        self.description = Description(self, description)

class Name:
    def __init__(self, location, value=None):
        self.location = location
        self.value = value

    def set(self, value):
        self.value = value

    def get(self):
        return self.value


class Description:
    def __init__(self, location, value=None):
        self.location = location
        self.value = value

    def set(self, value):
        self.value = value

    def get(self):
        return self.value

location1 = Location()
location1.name.set("The Forest")
location1.description.set("A dense forest with tall evergreen trees decreasing visibility. It is good for hiding but difficult to navigate.")

location2 = Location()
location2.name.set("The Dragon's Lair")
location2.description.set("You are likely to find the Dragon here in his dark, monstorous cave.")

location3 = Location()
location3.name.set("The Sea")
location3.description.set("The vast waters offer endless possibilities. There may be sea monsters but there also may be sunken treasure chests!")

location4 = Location()
location4.name.set("Mundy Room 414")
location4.description.set("This classroom is like your homebase where you can do all your behind the scenes coding work from.")