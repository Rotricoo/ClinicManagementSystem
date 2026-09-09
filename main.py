# Storage imports
from Storage.storage_manager import save_data, load_data

# Clinic rules import
from Management.clinic_manager import ClinicManager

# Staff imports
from People.Staff.MedicalStaff.doctor import Doctor
from People.Staff.MedicalStaff.nurse import Nurse

# Patients import
from People.Patient.patient import Patient
from People.Patient.vip_patient import VIPPatient

# Dashboard interaction import
from User_interaction.tkinter_dashboard import open_dashboard

# Shows the main system menu.
def show_main_menu():
    print("\nClinic Management System")
    print("1. Staff Management")
    print("2. Patient Management")
    print("3. Reports")
    print("4. Exit\n")


# Shows staff-related options.
def show_staff_menu():
    print("\nStaff Management")
    print("1. Add Nurse")
    print("2. Add Doctor")
    print("3. View staff members")
    print("4. Search staff")
    print("5. Record patient attended by Nurse")
    print("6. Back to main menu\n")


# Shows patient-related options.
def show_patient_menu():
    print("\nPatient Management")
    print("1. Add Patient")
    print("2. Add VIP Patient")
    print("3. View patients")
    print("4. Search patients")
    print("5. Back to main menu\n")


# Shows report-related options.
def show_reports_menu():
    print("\nReports")
    print("1. View daily report")
    print("2. Open dashboard")
    print("3. Back to main menu\n")


# Handles staff-related actions.
def staff_menu(clinic):
    while True:
        show_staff_menu()
        choice = get_text_input("Choose an option: ")

        # Add Nurse
        if choice == "1":
            name = get_text_input("Nurse name: ")

            if clinic.find_person_by_name(name):
                print("A person with this name already exists.")
            else:
                person_id = clinic.generate_id("NUR")
                hours_worked_today = get_int_input("Hours worked today: ")
                patients_attended_today = get_int_input("Patients attended today: ")
                nurse = Nurse(name, person_id, hours_worked_today, patients_attended_today)

                if clinic.add_staff_member(nurse):
                    save_data(clinic)
                    print(f"Nurse added successfully with ID: {person_id}.")
                else:
                    print("Failed to add Nurse. A person with this name may already exist.")

        # Add Doctor
        elif choice == "2":
            name = get_text_input("Doctor name: ")

            if clinic.find_person_by_name(name):
                print("A person with this name already exists.")
            else:
                person_id = clinic.generate_id("DOC")
                hours_worked_today = get_int_input("Hours worked today: ")
                shift_operational_budget = get_float_input("Shift operational budget: ")
                doctor = Doctor(name, person_id, hours_worked_today, shift_operational_budget)

                if clinic.add_staff_member(doctor):
                    save_data(clinic)
                    print(f"Doctor added successfully with ID: {person_id}.")
                else:
                    print("Failed to add Doctor. A person with this name may already exist.")

        # Show staff members
        elif choice == "3":
            clinic.display_staff_members()

        # Search staff by name
        elif choice == "4":
            name = get_text_input("Enter staff name: ")

            found_staff = clinic.find_staff_by_name(name)

            if isinstance(found_staff, Nurse):
                print(f"Found Nurse: {found_staff}")
            elif isinstance(found_staff, Doctor):
                print(f"Found Doctor: {found_staff}")
            else:
                print("No staff found with that name.")

        # Record patient attended by Nurse
        elif choice == "5":
            nurse_name = get_text_input("Enter Nurse name: ")
            found_staff = clinic.find_staff_by_name(nurse_name)

            if found_staff and isinstance(found_staff, Nurse):
                found_staff.record_patient_attended()
                save_data(clinic)
                print(f"Recorded patient attended for Nurse: {found_staff}")
            else:
                print("No Nurse found with that name.")

        # Exit
        elif choice == "6":
            break
        # Invalid option
        else:
            print("Invalid option. Please try again.")


# Handles patient-related actions.
def patient_menu(clinic):
    while True:
        show_patient_menu()
        choice = get_text_input("Choose an option: ")

        # Add regular patient
        if choice == "1":
            name = get_text_input("Patient name: ")

            if clinic.find_person_by_name(name):
                print("A person with this name already exists.")
            else:
                contact_number = get_contact_input("Contact number: ")
                number_of_visits = get_int_input("Number of visits: ")
                person_id = clinic.generate_id("PAT")
                patient = Patient(name, person_id, contact_number, number_of_visits)

                if clinic.add_patient(patient):
                    save_data(clinic)
                    print(f"Patient added successfully with ID: {person_id}.")
                else:
                    print("Failed to add Patient. A person with this name may already exist.")

        # Add VIP patient
        elif choice == "2":
            name = get_text_input("VIP Patient name: ")

            if clinic.find_person_by_name(name):
                print("A person with this name already exists.")
            else:
                contact_number = get_contact_input("Contact number: ")
                number_of_visits = get_int_input("Number of visits: ")
                priority_care_tier = get_text_input("Priority care tier: ")
                person_id = clinic.generate_id("VIP")
                vip_patient = VIPPatient(
                    name,
                    person_id,
                    contact_number,
                    number_of_visits,
                    priority_care_tier,
                )

                if clinic.add_patient(vip_patient):
                    save_data(clinic)
                    print(f"VIP Patient added successfully with ID: {person_id}.")
                else:
                    print("Failed to add VIP Patient. A person with this name may already exist.")

        # Show patients
        elif choice == "3":
            clinic.display_patients()

        # Search patient by name
        elif choice == "4":
            name = get_text_input("Enter patient name to search: ")

            found_patient = clinic.find_patient_by_name(name)

            if isinstance(found_patient, VIPPatient):
                print(f"Found VIP patient: {found_patient}")
            elif isinstance(found_patient, Patient):
                print(f"Found patient: {found_patient}")
            else:
                print("No patient found with that name.")

        # Exit
        elif choice == "5":
            break
        # Invalid option
        else:
            print("Invalid option. Please try again.")


# Handles report-related actions.
def report_menu(clinic):
    while True:
        show_reports_menu()
        choice = get_text_input("Choose an option: ")

        # Daily report
        if choice == "1":
            report = clinic.daily_report(300)
            display_daily_report(report)

        # Open dashboard with daily report data
        elif choice == "2":
            open_dashboard(clinic)

        # Exit
        elif choice == "3":
            break 

        # Invalid option
        else:
            print("Invalid option. Please try again.") 


# Displays the daily report in a readable terminal format.
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


# Gets an integer from the user and keeps asking until the input is valid.
def get_int_input(message):
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            print("Invalid input. Please enter just numbers.")


# Gets a decimal number from the user and keeps asking until the input is valid.
def get_float_input(message):
    while True:
        try:
            number = float(input(message))
            return number
        except ValueError:
            print("Invalid input. Please enter just numbers.")


# Gets required text from the user and rejects empty input.
def get_text_input(message):
    while True:
        text = input(message).strip()

        if text:
            return text

        print("This field cannot be empty.")


# Gets a contact number and checks that it has at least 10 characters.
def get_contact_input(message):
    while True:
        contact_number = input(message).strip()

        if not contact_number:
            print("This field cannot be empty.")
        elif len(contact_number) < 10:
            print("Contact number must have at least 10 digits.")
        else:
            return contact_number


def load_sample_data(clinic):
    nurse_one = Nurse("Maria", "NUR0001", 8, 2)
    nurse_two = Nurse("Julia", "NUR0002", 7, 5)
    doctor_one = Doctor("Lucas", "DOC0001", 8, 500)
    patient_one = Patient("Rod", "PAT0001", "00 000 000 00", 2)
    vip_patient_one = VIPPatient("Ana Silva", "VIP0001", "0400 999 888", 5, "Gold")

    clinic.add_staff_member(nurse_one)
    clinic.add_staff_member(nurse_two)
    clinic.add_staff_member(doctor_one)
    clinic.add_patient(patient_one)
    clinic.add_patient(vip_patient_one)


def setup_clinic():
    clinic = load_data()

    if clinic is None:
        clinic = ClinicManager()
        load_sample_data(clinic)

    return clinic


def main():
    clinic = setup_clinic()

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


if __name__ == "__main__":
    main()
