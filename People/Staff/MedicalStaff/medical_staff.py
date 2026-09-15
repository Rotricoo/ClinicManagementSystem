# Purpose: define shared fields and display behavior for medical staff.
# Date: 2026-09-14

class MedicalStaff:
    def __init__(self, name, person_id, hours_worked_today):
        self.name = name
        self.person_id = person_id
        self.hours_worked_today = hours_worked_today

    def add_worked_hours(self, hours):   
        self.hours_worked_today += hours
            

    def __str__(self):
        return f"{self.name} | ID: {self.person_id} | Hours: {self.hours_worked_today}"
