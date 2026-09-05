# This file defines the base class for regular patients.
# Patient stores shared patient information and basic visit/priority behavior.
class Patient:
    def __init__(self, name, person_id, contact_detail, number_of_visits):
        self.name = name
        self.person_id = person_id
        self.contact_detail = contact_detail
        self.number_of_visits = number_of_visits
    
    def add_visit(self):   
        self.number_of_visits += 1

    def calculate_priority(self):
        return "Regular Priority"
    
    def __str__(self):
        return f"{self.name} | ID: {self.person_id} | Contact: {self.contact_detail} | Visits: {self.number_of_visits}"

   
