# Purpose: manage clinic records and produce operational reports.
# Date: 2026-09-14

from People.Staff.MedicalStaff.nurse import Nurse
from People.Staff.MedicalStaff.doctor import Doctor
from People.Patient.patient import Patient
from People.Patient.vip_patient import VIPPatient

class ClinicManager:
    # Separate collections keep staff and patient operations easy to query.
    def __init__(self):
        self.staff_members = []
        self.patients = []

    def add_staff_member(self, staff_member):
        # Names are unique across the whole clinic to avoid ambiguous searches.
        if self.find_person_by_name(staff_member.name):
            return False
        else:
            self.staff_members.append(staff_member)
            return True

    def add_patient(self, patient):
        # Apply the same cross-category uniqueness rule to patients.
        if self.find_person_by_name(patient.name):
            return False
        else:
            self.patients.append(patient)
            return True

    def display_staff_members(self):
        if not self.staff_members:
            print("No staff members registered.")
            return
        for staff_member in self.staff_members:
            print(staff_member)

    def display_patients(self):
        if not self.patients:
            print("No patients registered.")
            return
        for patient in self.patients:
            print(patient)


    def find_staff_by_name(self, name):
        for staff_member in self.staff_members:
            if staff_member.name.lower() == name.lower():
                return staff_member

        return None

    def find_person_by_name(self, name):
        # Centralizing this lookup prevents duplicate-name checks from diverging.
        found_staff = self.find_staff_by_name(name)
        if found_staff:
            return found_staff

        found_patient = self.find_patient_by_name(name)
        if found_patient:
            return found_patient

        return None

    def find_patient_by_name(self, name):
        for patient in self.patients:
            if patient.name.lower() == name.lower():
                return patient

        return None

    def find_staff_by_id(self, person_id):
        return next((staff for staff in self.staff_members if staff.person_id.upper() == person_id.upper()), None)

    def find_patient_by_id(self, person_id):
        return next((patient for patient in self.patients if patient.person_id.upper() == person_id.upper()), None)

    def delete_staff(self, person_id):
        staff = self.find_staff_by_id(person_id)
        if staff is None:
            return False
        self.staff_members.remove(staff)
        return True

    def delete_patient(self, person_id):
        patient = self.find_patient_by_id(person_id)
        if patient is None:
            return False
        self.patients.remove(patient)
        return True

    def generate_id(self, prefix):
        # Counting existing IDs keeps generated identifiers predictable by type.
        id_count = 0

        existing_items = self.staff_members + self.patients

        for item in existing_items:
            if item.person_id.startswith(prefix):
                id_count += 1

        next_number = id_count + 1
        return f"{prefix}{next_number:04d}"
    

    def daily_report(self, budget_amount=0):
        total_staff = len(self.staff_members)
        total_patients = len(self.patients)
        nurses = []
        doctors = []
        number_of_nurses = 0
        number_of_doctors = 0
        number_of_vip_patients = 0
        doctor_budget_status = []
        total_patients_attended = 0

        for staff_member in self.staff_members:
            if isinstance(staff_member, Nurse):
                number_of_nurses += 1
                total_patients_attended += staff_member.patients_attended_today
                nurses.append(staff_member)
                

            elif isinstance(staff_member, Doctor):
                number_of_doctors += 1

                if staff_member.check_budget(budget_amount):
                    doctor_budget_status.append(f"{staff_member.name}: Within budget!")
                else:
                    doctor_budget_status.append(f"{staff_member.name}: Budget exceeded!")
        
        # A report still needs a meaningful value when no nurses are registered.
        if nurses:
            top_nurse = max(nurses, key=lambda nurse: nurse.patients_attended_today)
        else:
            top_nurse = None

        for patient in self.patients:
            if isinstance(patient, VIPPatient):
                number_of_vip_patients += 1

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
