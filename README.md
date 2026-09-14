# Clinic Management System

A Python clinic management application with terminal menus, a Tkinter dashboard, and pickle persistence.

## Requirements

- Python 3.10 or newer
- Tkinter, included with most Python installations

## Run the application

From the project folder:

```powershell
python main.py
```

The application stores its data in `Storage/clinic_data.pkl`.

## Features

- Inheritance-based `Nurse`, `Doctor`, `Patient`, and `VIPPatient` classes.
- Automatic IDs by entity type.
- Case-insensitive person search and duplicate-name protection.
- Validation for names, non-negative numeric values, and 10-digit contact numbers.
- The word `cancel` cancels any Nurse, Doctor, Patient, or VIP Patient registration without saving partial data.
- Terminal menus for staff, patients, and reports.
- Edit and delete operations using person IDs.
- Daily report with nurse, patient, VIP, and doctor budget information.
- TXT and CSV report export.
- Export accepts either a file path or a folder path; folders receive `daily_report.txt` or `daily_report.csv`.
- Tkinter dashboard with summary cards, report details, and a people table.
- Pickle persistence between application runs.

## Tests

Run the automated tests with:

```powershell
python -m unittest discover -s tests -p "test_*.py"
```

## Project structure

- `main.py`: application startup and sample-data setup.
- `Management/`: clinic business rules.
- `People/`: staff and patient domain classes.
- `Storage/`: pickle persistence and report export.
- `User_interaction/`: terminal menus and Tkinter dashboard.
- `tests/`: automated tests.

## Before submission

1. Remove local `Storage/clinic_data.pkl` data if it should not be submitted.
2. Remove private developer notes and debug-only files.
3. Run the automated tests from a clean checkout.
4. Run the complete manual acceptance flow: create records, search, edit, delete, generate and export a report, open the dashboard, close the application, reopen it, and confirm persistence.
