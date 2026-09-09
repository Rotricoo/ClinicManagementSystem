import pickle
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
