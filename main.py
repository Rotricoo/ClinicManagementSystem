from Management.clinic_manager import ClinicManager
from People.Patient.patient import Patient
from People.Patient.vip_patient import VIPPatient
from People.Staff.MedicalStaff.doctor import Doctor
from People.Staff.MedicalStaff.nurse import Nurse
from Storage.storage_manager import load_data
from User_interaction import terminal_menu


def load_sample_data(clinic):
    clinic.add_staff_member(Nurse("Maria", "NUR0001", 8, 2))
    clinic.add_staff_member(Nurse("Julia", "NUR0002", 7, 5))
    clinic.add_staff_member(Doctor("Lucas", "DOC0001", 8, 500))
    clinic.add_patient(Patient("Rod", "PAT0001", "0000000000", 2))
    clinic.add_patient(VIPPatient("Ana Silva", "VIP0001", "0400999888", 5, "Gold"))


def setup_clinic():
    clinic = load_data()
    if clinic is None:
        clinic = ClinicManager()
        load_sample_data(clinic)
    return clinic


def main():
    clinic = setup_clinic()
    while True:
        terminal_menu.show_main_menu()
        choice = terminal_menu.get_text_input("Choose an option: ")
        if choice == "1":
            terminal_menu.staff_menu(clinic)
        elif choice == "2":
            terminal_menu.patient_menu(clinic)
        elif choice == "3":
            terminal_menu.report_menu(clinic)
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
