# This file defines the base class for all medical staff members.
# MedicalStaff stores the shared information used by Nurse and Doctor.
#
# Learning notes:
# __init__ stores the starting information when an object is created.
# __str__ controls how the object is displayed when we print it.

class MedicalStaff:
    def __init__(self, name, person_id, hours_worked_today):
        self.name = name
        self.person_id = person_id
        self.hours_worked_today = hours_worked_today

    def add_worked_hours(self, hours):   
        self.hours_worked_today += hours
            

    def __str__(self):
        return f"{self.name} | ID: {self.person_id} | Hours: {self.hours_worked_today}"
