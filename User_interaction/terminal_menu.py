# Purpose: provide the interactive terminal menus for clinic operations.
# Group members: Rick Grimes - 123456
# Date: 2026-09-14

from Management.clinic_manager import ClinicManager
from People.Patient.patient import Patient
from People.Patient.vip_patient import VIPPatient
from People.Staff.MedicalStaff.doctor import Doctor
from People.Staff.MedicalStaff.nurse import Nurse
from Storage.storage_manager import export_report_to_csv, export_report_to_txt, save_data
from User_interaction.tkinter_dashboard import open_dashboard


class RegistrationCancelled(Exception):
    pass


def show_main_menu():
    print("\nClinic Management System")
    print("1. Staff Management")
    print("2. Patient Management")
    print("3. Reports")
    print("4. Exit\n")


def show_staff_menu():
    print("\nStaff Management")
    print("1. Add Nurse")
    print("2. Add Doctor")
    print("3. View staff members")
    print("4. Search staff")
    print("5. Edit staff")
    print("6. Delete staff")
    print("7. Record patient attended by Nurse")
    print("8. Back to main menu\n")


def show_patient_menu():
    print("\nPatient Management")
    print("1. Add Patient")
    print("2. Add VIP Patient")
    print("3. View patients")
    print("4. Search patients")
    print("5. Edit patient")
    print("6. Delete patient")
    print("7. Back to main menu\n")


def show_reports_menu():
    print("\nReports")
    print("1. View daily report")
    print("2. Export report to TXT")
    print("3. Export report to CSV")
    print("4. Open dashboard")
    print("5. Back to main menu\n")


def staff_menu(clinic):
    while True:
        show_staff_menu()
        choice = get_text_input("Choose an option: ")
        if choice == "1":
            try:
                name = get_name_input("Nurse name (or 'cancel'): ", allow_cancel=True)
                if clinic.find_person_by_name(name):
                    print("Error: A person with this name already exists.")
                    continue
                hours = get_int_input("Hours worked today (or 'cancel'): ", allow_cancel=True)
                patients_attended = get_int_input("Patients attended today (or 'cancel'): ", allow_cancel=True)
                nurse = Nurse(name, clinic.generate_id("NUR"), hours, patients_attended)
                if clinic.add_staff_member(nurse):
                    save_data(clinic)
                    print(f"Nurse added successfully with ID: {nurse.person_id}.")
            except RegistrationCancelled:
                print("Registration cancelled. No data was saved.")
        elif choice == "2":
            try:
                name = get_name_input("Doctor name (or 'cancel'): ", allow_cancel=True)
                if clinic.find_person_by_name(name):
                    print("Error: A person with this name already exists.")
                    continue
                hours = get_int_input("Hours worked today (or 'cancel'): ", allow_cancel=True)
                budget = get_float_input("Shift operational budget (or 'cancel'): ", allow_cancel=True)
                doctor = Doctor(name, clinic.generate_id("DOC"), hours, budget)
                if clinic.add_staff_member(doctor):
                    save_data(clinic)
                    print(f"Doctor added successfully with ID: {doctor.person_id}.")
            except RegistrationCancelled:
                print("Registration cancelled. No data was saved.")
        elif choice == "3":
            clinic.display_staff_members()
        elif choice == "4":
            staff = clinic.find_staff_by_name(get_name_input("Enter staff name: "))
            print(f"Found staff: {staff}" if staff else "No staff found with that name.")
        elif choice == "5":
            edit_staff(clinic)
        elif choice == "6":
            delete_staff(clinic)
        elif choice == "7":
            nurse = clinic.find_staff_by_name(get_name_input("Enter Nurse name: "))
            if isinstance(nurse, Nurse):
                nurse.record_patient_attended()
                save_data(clinic)
                print(f"Recorded patient attended for Nurse: {nurse}")
            else:
                print("No Nurse found with that name.")
        elif choice == "8":
            break
        else:
            print("Invalid option. Please try again.")


def patient_menu(clinic):
    while True:
        show_patient_menu()
        choice = get_text_input("Choose an option: ")
        if choice == "1":
            add_patient(clinic, False)
        elif choice == "2":
            add_patient(clinic, True)
        elif choice == "3":
            clinic.display_patients()
        elif choice == "4":
            patient = clinic.find_patient_by_name(get_name_input("Enter patient name to search: "))
            print(f"Found patient: {patient}" if patient else "No patient found with that name.")
        elif choice == "5":
            edit_patient(clinic)
        elif choice == "6":
            delete_patient(clinic)
        elif choice == "7":
            break
        else:
            print("Invalid option. Please try again.")


def add_patient(clinic, is_vip):
    # One flow for both patient types keeps validation and persistence consistent.
    try:
        name = get_name_input("VIP Patient name (or 'cancel'): " if is_vip else "Patient name (or 'cancel'): ", allow_cancel=True)
        if clinic.find_person_by_name(name):
            print("Error: A person with this name already exists.")
            return
        contact = get_contact_input("Contact number (or 'cancel'): ", allow_cancel=True)
        visits = get_int_input("Number of visits (or 'cancel'): ", allow_cancel=True)
        if is_vip:
            tier = get_text_input("Priority care tier (or 'cancel'): ", allow_cancel=True)
            person = VIPPatient(name, clinic.generate_id("VIP"), contact, visits, tier)
        else:
            person = Patient(name, clinic.generate_id("PAT"), contact, visits)
        if clinic.add_patient(person):
            save_data(clinic)
            print(f"Patient added successfully with ID: {person.person_id}.")
    except RegistrationCancelled:
        print("Registration cancelled. No data was saved.")


def report_menu(clinic):
    while True:
        show_reports_menu()
        choice = get_text_input("Choose an option: ")
        # Reports use the same operational budget threshold across menu actions.
        report = clinic.daily_report(300)
        if choice == "1":
            display_daily_report(report)
        elif choice == "2":
            path = get_text_input("TXT output path: ")
            try:
                exported_path = export_report_to_txt(report, path)
                print(f"Report exported to {exported_path}.")
            except OSError as error:
                print(f"Error: Could not export report: {error}")
        elif choice == "3":
            path = get_text_input("CSV output path: ")
            try:
                exported_path = export_report_to_csv(report, path)
                print(f"Report exported to {exported_path}.")
            except OSError as error:
                print(f"Error: Could not export report: {error}")
        elif choice == "4":
            open_dashboard(clinic)
        elif choice == "5":
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
    print("Doctor budget status:")
    for status in report["doctor_budget_status"] or ["No doctors registered"]:
        print(f"- {status}")
    print(f"Total patients: {report['total_patients']}")
    print(f"VIP patients: {report['number_of_vip_patients']}")


def edit_staff(clinic):
    person = clinic.find_staff_by_id(get_text_input("Staff ID: "))
    if not person:
        print("Staff member not found.")
        return
    name = get_name_input(f"Name [{person.name}]: ")
    if name != person.name and clinic.find_person_by_name(name):
        print("Error: A person with this name already exists.")
        return
    person.name = name
    person.hours_worked_today = get_int_input(f"Hours worked today [{person.hours_worked_today}]: ")
    if isinstance(person, Nurse):
        person.patients_attended_today = get_int_input(f"Patients attended today [{person.patients_attended_today}]: ")
    else:
        person.shift_operational_budget = get_float_input(f"Shift operational budget [{person.shift_operational_budget}]: ")
    save_data(clinic)
    print("Staff member updated successfully.")


def delete_staff(clinic):
    person = clinic.find_staff_by_id(get_text_input("Staff ID: "))
    if not person:
        print("Staff member not found.")
    elif get_text_input(f"Delete {person.name}? Type YES to confirm: ").upper() == "YES":
        clinic.delete_staff(person.person_id)
        save_data(clinic)
        print("Staff member deleted successfully.")


def edit_patient(clinic):
    person = clinic.find_patient_by_id(get_text_input("Patient ID: "))
    if not person:
        print("Patient not found.")
        return
    name = get_name_input(f"Name [{person.name}]: ")
    if name != person.name and clinic.find_person_by_name(name):
        print("Error: A person with this name already exists.")
        return
    person.name = name
    person.contact_detail = get_contact_input(f"Contact number [{person.contact_detail}]: ")
    person.number_of_visits = get_int_input(f"Number of visits [{person.number_of_visits}]: ")
    if isinstance(person, VIPPatient):
        person.priority_care_tier = get_text_input(f"Priority care tier [{person.priority_care_tier}]: ")
    save_data(clinic)
    print("Patient updated successfully.")


def delete_patient(clinic):
    person = clinic.find_patient_by_id(get_text_input("Patient ID: "))
    if not person:
        print("Patient not found.")
    elif get_text_input(f"Delete {person.name}? Type YES to confirm: ").upper() == "YES":
        clinic.delete_patient(person.person_id)
        save_data(clinic)
        print("Patient deleted successfully.")


def get_int_input(message, allow_cancel=False):
    while True:
        try:
            value = input(message).strip()
            check_cancel(value, allow_cancel)
            number = int(value)
            if number < 0:
                raise ValueError
            return number
        except ValueError:
            print("Invalid input. Please enter a non-negative whole number.")


def get_float_input(message, allow_cancel=False):
    while True:
        try:
            value = input(message).strip()
            check_cancel(value, allow_cancel)
            number = float(value)
            if number < 0:
                raise ValueError
            return number
        except ValueError:
            print("Invalid input. Please enter a non-negative number.")


def get_text_input(message, allow_cancel=False):
    while True:
        text = input(message).strip()
        check_cancel(text, allow_cancel)
        if text:
            return text
        print("This field cannot be empty.")


def get_name_input(message, allow_cancel=False):
    while True:
        name = input(message).strip()
        check_cancel(name, allow_cancel)
        # Normalize names once so searches and duplicate checks are consistent.
        name = name.lower()
        if not name:
            print("This field cannot be empty.")
        elif not all(part.isalpha() for part in name.split()):
            print("Name must contain letters and spaces only.")
        else:
            return name


def get_contact_input(message, allow_cancel=False):
    while True:
        contact_number = input(message).strip()
        check_cancel(contact_number, allow_cancel)
        if not contact_number:
            print("This field cannot be empty.")
        elif not contact_number.isdigit() or len(contact_number) != 10:
            print("Contact number must contain exactly 10 numeric digits.")
        else:
            return contact_number


def check_cancel(value, allow_cancel):
    if allow_cancel and value.lower() == "cancel":
        raise RegistrationCancelled
