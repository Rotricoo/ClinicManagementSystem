from People.Staff.MedicalStaff.medical_staff import MedicalStaff


# Doctor is a subclass of MedicalStaff.
# It reuses the shared staff information and adds shift budget checking.
class Doctor(MedicalStaff):
    def __init__(self, name, person_id, hours_worked_today, shift_operational_budget):
        super().__init__(name, person_id, hours_worked_today)
        self.shift_operational_budget = shift_operational_budget

    def check_budget(self, amount):
        return self.shift_operational_budget <= amount

    def __str__(self):
        return f"{self.name} | ID: {self.person_id} | Hours: {self.hours_worked_today} | Budget: {self.shift_operational_budget}"
