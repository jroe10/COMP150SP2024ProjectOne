class Event:
    def __init__(self, name, requirements, success_outcome, partial_success_outcome, failure_outcome):
        self.name = name
        self.requirements = requirements
        self.success_outcome = success_outcome
        self.partial_success_outcome = partial_success_outcome
        self.failure_outcome = failure_outcome

event1 = Event(
    name="Encountering enemy (slime)",
    requirements="Encounter Slime",
    success_outcome="You defeated the slime!",
    partial_success_outcome="The slime ran away!",
    failure_outcome="You fainted."
)


event2 = Event(
        name="Encountering enemy (goblin)",
        requirements="Encounter Goblin",
        success_outcome="You defeated the Goblin!",
        partial_outcome_success="The Goblin ran away!",
        fail_outcome="You fainted."
        )
        
event3 = Event(
        name="Encountering boss enemy (dragon)",
        requirements="Face the Dragon",
        success_outcome="You defeated the Dragon!!",
        partial_outcome_success="You sealed away the Dragon!",
        fail_outcome="You fainted. The Dragon took over the world"
        )
        
event4 = Event(
        name="Go to the forest?",
        requirements="Go to the forest",
        success_outcome="You enter the forest.",
        partial_outcome_success="You were dragged into the forest",
        fail_outcome="You don't enter the forest"
        )
    
event5 = Event(
        name="Go to the Dragons Lair?",
        requirements="Go to the Dragons Lair",
        success_outcome="You enter the Dragon's Lair.",
        partial_outcome_success="You were dragged into the Dragon's Lair.",
        fail_outcome="You don't enter the Dragon's Lair."
        )

event6 = Event(
        name="Go to the Sea?",
        requirements="You go to the Sea.",
        success_outcome="You go to the Sea.",
        partial_outcome_success="You were dragged to the Sea",
        fail_outcome="You don't go to the Sea."
        )

event7 = Event(
        name="Go to Mundy Room 414?",
        requirements="Go to Mundy Room 414",
        success_outcome="You enter Mundy Room 414",
        partial_outcome_success="You were dragged into Mundy Room 414",
        fail_outcome="You don't enter Mundy Room 414."
        )

event8 = Event(
        name="",
        requirements="",
        success_outcome="",
        partial_outcome_success="",
        fail_outcome=""
        )