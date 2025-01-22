class Event:
    def __init__(self, payload: dict):
        self.payload = payload
class EnrollmentSubmittedEvent(Event):
    def __init__(self, payload: dict):
        super().__init__(payload)
class EnrollmentRejectedEvent(Event):
    def __init__(self, payload: dict):
        super().__init__(payload)
class University:
    def __init__(self, name):
        self.name = name
        self.course_catalog = {}
        self.event_queue = []
    def add_course(self, course_name, max_seats):
        self.course_catalog[course_name] = self.course_catalog.get(course_name, 0) + max_seats
    def submit_enrollment(self, student, course_name, seats_requested):
        if course_name in self.course_catalog and self.course_catalog[course_name] >= seats_requested:
            self.course_catalog[course_name] -= seats_requested
            event = EnrollmentSubmittedEvent({
                "student_name": student.name,
                "course_name": course_name,
                "seats_reserved": seats_requested
            })
            self.event_queue.append(event)
        else:
            event = EnrollmentRejectedEvent({
                "student_name": student.name,
                "course_name": course_name,
                "reason": "Not enough seats available"
            })
            self.event_queue.append(event)
    def process_events(self):
        while self.event_queue:
            event = self.event_queue.pop(0)
            if isinstance(event, EnrollmentSubmittedEvent):
                print(f"Enrollment Successful: {event.payload}")
            elif isinstance(event, EnrollmentRejectedEvent):
                print(f"Enrollment Failed: {event.payload}")
class Student:
    def __init__(self, name):
        self.name = name
if __name__ == "__main__":
    
    university = University("Elite Academy")
    student = Student("Emma")
   
    university.add_course("Machine Learning", 4)
    university.add_course("Data Analytics", 6)
   
    university.submit_enrollment(student, "Machine Learning", 1) 
    university.submit_enrollment(student, "Data Analytics", 7)        
    university.process_events()




















