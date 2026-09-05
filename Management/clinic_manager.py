# ClinicManager is the container class for the system.
# It will store staff and patients, then provide methods to manage them.

from People.Staff.MedicalStaff.nurse import Nurse
from People.Staff.MedicalStaff.doctor import Doctor
from People.Patient.patient import Patient
from People.Patient.vip_patient import VIPPatient

class ClinicManager:
    # Inicialization with empty lists
    def __init__(self):
        self.staff_members = []
        self.patients = []

    # Function to add staff member
    def add_staff_member(self, staff_member):
        self.staff_members.append(staff_member)

    # Function to add patient
    def add_patient(self, patient):
        self.patients.append(patient)

    # Function to show staff member
    def display_staff_members(self):
        for staff_member in self.staff_members:
            print(staff_member)

    # Function to show patients
    def display_patients(self):
        for patient in self.patients:
            print(patient)

    # Function to search staff by name
    def find_staff_by_name(self, name):
        for staff_member in self.staff_members:
            if staff_member.name == name:
                return staff_member

        return None

    # Function to search patient by name
    def find_patient_by_name(self, name):
        for patient in self.patients:
            if patient.name == name:
                return patient

        return None

    def generate_id(self, prefix):
        id_count = 0

        existing_items = self.staff_members + self.patients

        for item in existing_items:
            if item.person_id.startswith(prefix):
                id_count += 1

        next_number = id_count + 1
        return f"{prefix}{next_number:04d}"
    

    def daily_report(self, budget_amount = 0):
        total_staff = len(self.staff_members)
        total_patients = len(self.patients)
        number_of_nurses = 0
        number_of_doctors = 0
        number_of_vip_patients = 0
        total_patients_attended = 0

        for staff_member in self.staff_members:
            if isinstance(staff_member, Nurse):
                number_of_nurses += 1

        for staff_member in self.staff_members:
            if isinstance(staff_member, Doctor):
                number_of_doctors += 1

        for patient in self.patients:
            if isinstance(patient, VIPPatient):
                number_of_vip_patients += 1

        for staff_member in self.staff_members:
            if isinstance(staff_member, Nurse):
                total_patients_attended += staff_member.patients_attended_today

        nurses = []
        for staff_member in self.staff_members:
            if isinstance(staff_member, Nurse):
                nurses.append(staff_member)

        if nurses:
            top_nurse = max(nurses, key=lambda nurse:nurse.patients_attended_today)
        else:
            top_nurse = None

        doctor_budget_status = []

        for staff_member in self.staff_members:
            if isinstance(staff_member, Doctor):
                if staff_member.check_budget(budget_amount):
                    doctor_budget_status.append(f"{staff_member.name}: Within budget!")
                else:
                    doctor_budget_status.append(f"{staff_member.name}: Budget exceeded!")

        return {
            "total_staff": total_staff,
            "total_patients": total_patients,
            "number_of_nurses": number_of_nurses,
            "number_of_doctors": number_of_doctors,
            "number_of_vip_patients": number_of_vip_patients,
            "total_patients_attended": total_patients_attended,
            "top_nurse": top_nurse.name if top_nurse else "No nurses registered",
            "doctor_budget_status": doctor_budget_status
        }
