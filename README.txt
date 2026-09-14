CLINIC MANAGEMENT SYSTEM

Purpose
This project is a small Python clinic management system. It allows users to register nurses, doctors, regular patients, and VIP patients. The application supports searching, editing, deleting, reporting, report export, and persistence between executions.

Requirements and execution
Use Python 3.10 or newer. Tkinter is required only when the dashboard is opened and is normally included with a standard Python installation. Open PowerShell in the project folder and run:

    python main.py

The first execution creates sample records when no saved data exists. The terminal menu is the main interface. The Reports menu can open the Tkinter dashboard or export a report to TXT or CSV. Run the tests with:

    python -m unittest discover -s tests -p "test_*.py"

Files and folders
- main.py starts the program, loads saved data, and creates sample data for a new installation.
- Management/clinic_manager.py stores clinic collections, enforces unique names, searches records, deletes records, generates IDs, and creates daily reports.
- People/Patient/patient.py defines regular patients.
- People/Patient/vip_patient.py extends Patient with priority-care information.
- People/Staff/MedicalStaff/medical_staff.py defines shared staff behavior.
- doctor.py and nurse.py define the two staff specializations.
- Storage/storage_manager.py saves and loads pickle data and exports reports.
- User_interaction/terminal_menu.py implements terminal input, validation, and menus.
- User_interaction/tkinter_dashboard.py implements the graphical dashboard.
- tests/test_clinic.py contains automated behavior tests.

Known limitations
Data is stored as a local pickle file in Storage/clinic_data.pkl, so it is intended for a trusted local environment and is not a multi-user database. There is no login, encryption, backup, or concurrent access control. The contact validation accepts exactly ten digits and may not match every country's phone format. The dashboard must run in an environment with a graphical display. Existing IDs are counted by prefix, so deleting a record can eventually produce an identifier that is reused.
