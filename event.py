class Event:
    def __init__(self, payload: dict):
        self.payload = payload
class EnrollmentSubmittedEvent(Event):
    def __init__(self, payload: dict):
        super().__init__(payload)
class EnrollmentRejectedEvent(Event):
    def __init__(self, payload: dict):
        super().__init__(payload)