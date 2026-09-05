from Management.clinic_manager import ClinicManager

# Staff imports
from People.Staff.MedicalStaff.doctor import Doctor
from People.Staff.MedicalStaff.nurse import Nurse

# Patients import
from People.Patient.patient import Patient
from People.Patient.vip_patient import VIPPatient

# def show_menu():
#     print("\nClinic Management System")
#     print("1. Add Nurse")
#     print("2. Add Doctor")
#     print("3. Add Patient")
#     print("4. Add VIP Patient")
#     print("5. View staff members")
#     print("6. View patients")
#     print("7. Search by name")
#     print("8. Record patient attended by Nurse")
#     print("9. View daily report")
#     print("10. Exit\n")

# Main menu with main options
def show_main_menu():
    print("\nClinic Management System")
    print("1. Staff Management")
    print("2. Patient Management")
    print("3. Reports")
    print("4. Exit\n")

# Staff menu after chosing 1 in the main menu
def show_staff_menu():
    print("\nStaff Management")
    print("1. Add Nurse")
    print("2. Add Doctor")
    print("3. View staff members")
    print("4. Search staff")
    print("5. Record patient attended by Nurse") 
    print("6. Back to main menu\n")

# Patient menu after chosing 2 in the main menu
def show_patient_menu():
    print("\nPatient Management")
    print("1. Add Patient")
    print("2. Add VIP Patient")
    print("3. View patients")
    print("4. Search patients")
    print("5. Back to main menu\n")

# Report menu after chosing 3 in the main menu
def show_reports_menu():
    print("\nReports")
    print("1. View daily report")
    print("2. Back to main menu\n")

# Staff Management menu
def staff_menu(clinic):
    while True:
        show_staff_menu()
        choice = get_text_input("Choose an option: ")

        # Add Nurse
        if choice == "1":
            name = get_text_input("Nurse name: ")

            if clinic.find_staff_by_name(name):
                print("Staff member with this name already exists.")
            else:
                person_id = clinic.generate_id("NUR")
                hours_worked_today = get_int_input("Hours worked today: ")
                patients_attended_today = get_int_input("Patients attended today: ")

                nurse = Nurse(name, person_id, hours_worked_today, patients_attended_today)
                clinic.add_staff_member(nurse)
                print(f"Nurse added successfully with ID: {person_id}.")

        # Add Doctor
        elif choice == "2":
            name = get_text_input("Doctor name: ")

            if clinic.find_staff_by_name(name):
                print("Staff member with this name already exists.")
            else:
                person_id = clinic.generate_id("DOC")
                hours_worked_today = get_int_input("Hours worked today: ")
                shift_operational_budget = get_float_input("Shift operational budget: ")

                doctor = Doctor(name, person_id, hours_worked_today, shift_operational_budget)
                clinic.add_staff_member(doctor)
                print(f"Doctor added successfully with ID: {person_id}.")

        elif choice == "3":
            clinic.display_staff_members()

        elif choice == "4":
            name = get_text_input("Enter staff name: ")

            found_staff = clinic.find_staff_by_name(name)

            if isinstance(found_staff, Nurse):
                print(f"Found Nurse: {found_staff}")
            elif isinstance(found_staff, Doctor):
                print(f"Found Doctor: {found_staff}")           
            else:
                print("No staff found with that name.")

        elif choice == "5":
            nurse_name = get_text_input("Enter Nurse name: ")
            found_staff = clinic.find_staff_by_name(nurse_name)

            if found_staff and isinstance(found_staff, Nurse):
                found_staff.record_patient_attended()
                print(f"Recorded patient attended for Nurse: {found_staff}")
            else:
                print("No Nurse found with that name.")

        elif choice == "6":
            break
        else:
            print("Invalid option. Please try again.")

# Patient Management Menu
def patient_menu(clinic):
    while True:
        show_patient_menu()
        choice = get_text_input("Choose an option: ")

        if choice == "1":
            name = get_text_input("Patient name: ")

            if clinic.find_patient_by_name(name):
                 print("Patient with this name already exists.")
            else:
                 contact_number = get_contact_input("Contact number: ")
                 number_of_visits = get_int_input("Number of visits: ")

                 person_id = clinic.generate_id("PAT")
                 patient = Patient(name, person_id, contact_number, number_of_visits)
                 clinic.add_patient(patient)
                 print(f"Patient added successfully with ID: {person_id}.")

        elif choice == "2":
            name = get_text_input("VIP Patient name: ")
            if clinic.find_patient_by_name(name):
                 print("Patient with this name already exists.")
            else:
                 contact_number = get_contact_input("Contact number: ")
                 number_of_visits = get_int_input("Number of visits: ")
                 priority_care_tier = get_text_input("Priority care tier: ")

                 person_id = clinic.generate_id("VIP")
                 vip_patient = VIPPatient(name, person_id, contact_number, number_of_visits, priority_care_tier)
                 clinic.add_patient(vip_patient)
                 print(f"VIP Patient added successfully with ID: {person_id}.")

        elif choice == "3":
            clinic.display_patients()

        elif choice == "4":
            name = get_text_input("Enter patient name to search: ")

            found_patient = clinic.find_patient_by_name(name)
            
            if isinstance(found_patient, VIPPatient):
                print(f"Found VIP patient: {found_patient}")
            elif isinstance(found_patient, Patient):
                print(f"Found patient: {found_patient}")
            else:
                print("No patient found with that name.")

        elif choice == "5":
            break
        else:
            print("Invalid option. Please try again.")

# Report Menu
def report_menu(clinic):
    while True:
        show_reports_menu()
        choice = get_text_input("Choose an option: ")

        if choice == "1":
            report = clinic.daily_report(300)
            display_daily_report(report)
        elif choice == "2":
            break
        else:
            print("Invalid option. Please try again.")

def display_daily_report(report):
    print("Daily Report")
    print(f"Total staff: {report['total_staff']}")
    print(f"Number of nurses: {report['number_of_nurses']}")
    print(f"Number of doctors: {report['number_of_doctors']}")
    print(f"Total patients attended: {report['total_patients_attended']}")
    print(f"Top nurse: {report['top_nurse']}")
    print(f"Doctor budget status: {report['doctor_budget_status']}")
    print(f"Total patients: {report['total_patients']}")
    print(f"VIP patients: {report['number_of_vip_patients']}")

def get_int_input(message):
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            print("Invalid input. Please enter just numbers.")

def get_float_input(message):
    while True:
        try:
            number = float(input(message))
            return number
        except ValueError:
            print("Invalid input. Please enter just numbers.")

def get_text_input(message):
    while True:
        text = input(message).strip()

        if text:
            return text

        print("This field cannot be empty.")

def get_contact_input(message):
    while True:
        contact_number = input(message).strip()

        if not contact_number:
            print("This field cannot be empty.")
        elif len(contact_number) < 10:
            print("Contact number must have at least 10 digits.")
        else:
            return contact_number

def main():
    clinic = ClinicManager()

    nurse = Nurse("Maria", "NUR0001", 8, 2)
    nurse_two = Nurse("Julia", "NUR0002", 7, 5)    
    doctor = Doctor("Lucas", "DOC0001", 8, 500)
    patient = Patient("Rod","PAT0001", "00 000 000 00", 2)
    vip_patient = VIPPatient("Ana Silva", "VIP0001", "0400 999 888", 5, "Gold")

    clinic.add_staff_member(nurse)
    clinic.add_staff_member(nurse_two)
    clinic.add_staff_member(doctor)
    clinic.add_patient(patient)
    clinic.add_patient(vip_patient)

    while True:
        show_main_menu()
        choice_menu = get_text_input("Choose an option: ")

        if choice_menu == "1":
            staff_menu(clinic)
        elif choice_menu == "2":
            patient_menu(clinic)
        elif choice_menu == "3":
            report_menu(clinic)
        elif choice_menu == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

main()

