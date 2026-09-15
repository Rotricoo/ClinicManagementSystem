# Purpose: define doctors and their operational budget checks.
# Date: 2026-09-14

from People.Staff.MedicalStaff.medical_staff import MedicalStaff

class Doctor(MedicalStaff):
    def __init__(self, name, person_id, hours_worked_today, shift_operational_budget):
        super().__init__(name, person_id, hours_worked_today)
        self.shift_operational_budget = shift_operational_budget

    def check_budget(self, amount):
        # The report passes its allowed amount, so equality remains within budget.
        return self.shift_operational_budget <= amount

    def __str__(self):
        return f"{self.name} | ID: {self.person_id} | Hours: {self.hours_worked_today} | Budget: {self.shift_operational_budget}"
