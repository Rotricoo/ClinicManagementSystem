# Purpose: define the patient type that receives priority care.
# Group members: Rick Grimes - 123456
# Date: 2026-09-14

from People.Patient.patient import Patient

class VIPPatient(Patient):
    def __init__(self, name, person_id, contact_detail, number_of_visits, priority_care_tier):
        super().__init__(name, person_id, contact_detail, number_of_visits)
        self.priority_care_tier = priority_care_tier

    def calculate_priority(self):
        # Overriding the base behavior keeps priority policy polymorphic.
        return "High Priority - VIP Client"

    def __str__(self):
        return f"{self.name} | ID: {self.person_id} | Contact: {self.contact_detail} | Visits: {self.number_of_visits} |  Tier: {self.priority_care_tier} | Priority Care Tier: {self.calculate_priority()}"

