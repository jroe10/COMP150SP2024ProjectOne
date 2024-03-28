from parser import UserInputParser, EventInputParser

class UserInputParser:
    def __init__(self):
        self.style = "console"  # Default style is console

    def parse(self, prompt):
        """Prompt the user for input."""
        response = input(prompt)
        return response

class EventInputParser:
    def __init__(self):
        self.style = "console"  # Default style is console

    def select_party_member(self, party):
        """Select a party member for an event."""
        return random.choice(party)

    def select_skill(self, character):
        """Select a skill for a character."""
        return random.choice(character.skills)