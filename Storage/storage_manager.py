# Purpose: persist clinic data and export reports to common text formats.
# Date: 2026-09-14

import pickle
import csv
from pathlib import Path

DATA_FILE = Path(__file__).parent / "clinic_data.pkl"


def save_data(clinic):
    # Pickle preserves the object graph, so all domain types reload together.
    with open(DATA_FILE, "wb") as file:
        pickle.dump(clinic, file)


def load_data():
    # A missing file is normal on first launch, so return None instead of failing.
    try:
        with open(DATA_FILE, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return None


def export_report_to_txt(report, file_path):
    file_path = Path(file_path)
    if file_path.is_dir():
        # Directory input gets a stable filename for predictable exports.
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
