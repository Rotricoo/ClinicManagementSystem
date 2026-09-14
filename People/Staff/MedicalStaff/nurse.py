# Purpose: define nurses and track patients attended during the day.
# Group members: Rick Grimes - 123456
# Date: 2026-09-14

from People.Staff.MedicalStaff.medical_staff import MedicalStaff
class Nurse(MedicalStaff):
    def __init__(self, name, person_id, hours_worked_today, patients_attended_today):
        super().__init__(name, person_id, hours_worked_today)
        self.patients_attended_today = patients_attended_today

    def record_patient_attended(self):
        self.patients_attended_today += 1

    def __str__(self):
        return f"{self.name} | ID: {self.person_id} | Hours: {self.hours_worked_today} | Patients attended: {self.patients_attended_today}"

