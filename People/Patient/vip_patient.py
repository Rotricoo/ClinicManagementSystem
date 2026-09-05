from People.Patient.patient import Patient


# VIPPatient is a subclass of Patient.
# It reuses the normal patient information and overrides the priority behavior.
class VIPPatient(Patient):
    def __init__(self, name, person_id, contact_detail, number_of_visits, priority_care_tier):
        super().__init__(name, person_id, contact_detail, number_of_visits)
        self.priority_care_tier = priority_care_tier

    def calculate_priority(self):
        return "High Priority - VIP Client"

    def __str__(self):
        return f"{self.name} | ID: {self.person_id} | Contact: {self.contact_detail} | Visits: {self.number_of_visits} |  Tier: {self.priority_care_tier} | Priority Care Tier: {self.calculate_priority()}"

