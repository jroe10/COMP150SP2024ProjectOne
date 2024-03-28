class Event:
    def __init__(self, name, requirements, success_outcome, partial_success_outcome, failure_outcome):
        self.name = name
        self.requirements = requirements
        self.success_outcome = success_outcome
        self.partial_success_outcome = partial_success_outcome
        self.failure_outcome = failure_outcome

event1 = Event(
    name="Encountering enemy (slime)",
    requirements="Encounter slime",
    success_outcome="",
    partial_success_outcome="",
    failure_outcome=""
)


event2 = Event(
        name="",
        requirements="",
        success_outcome="",
        partial_outcome_success="",
        fail_outcome=""
        )
        
event3 = Event(
        name="",
        requirements="",
        success_outcome="",
        partial_outcome_success="",
        fail_outcome=""
        )
        
event4 = Event(
        name="",
        requirements="",
        success_outcome="",
        partial_outcome_success="",
        fail_outcome=""
        )
    
event5 = Event(
        name="",
        requirements="",
        success_outcome="",
        partial_outcome_success="",
        fail_outcome=""
        )