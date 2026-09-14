import pickle
import csv
from pathlib import Path

DATA_FILE = Path(__file__).parent / "clinic_data.pkl"


def save_data(clinic):
    # Save the full ClinicManager object to a local pickle file
    with open(DATA_FILE, "wb") as file:
        pickle.dump(clinic, file)


def load_data():
    # Load the saved ClinicManager object if the data file exists.
    try:
        with open(DATA_FILE, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return None


def export_report_to_txt(report, file_path):
    file_path = Path(file_path)
    if file_path.is_dir():
        file_path = file_path / "daily_report.txt"
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("Daily Report\n")
        for key, value in report.items():
            file.write(f"{key}: {value}\n")
    return file_path


def export_report_to_csv(report, file_path):
    file_path = Path(file_path)
    if file_path.is_dir():
        file_path = file_path / "daily_report.csv"
    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Metric", "Value"])
        for key, value in report.items():
            writer.writerow([key, value])
    return file_path
