import tempfile
import unittest
from pathlib import Path

from Management.clinic_manager import ClinicManager
from People.Patient.patient import Patient
from People.Patient.vip_patient import VIPPatient
from People.Staff.MedicalStaff.doctor import Doctor
from People.Staff.MedicalStaff.nurse import Nurse
from Storage import storage_manager


class ClinicManagerTests(unittest.TestCase):
    def setUp(self):
        self.clinic = ClinicManager()

    def test_adds_all_supported_people(self):
        self.assertTrue(self.clinic.add_staff_member(Nurse("maria", "NUR0001", 8, 2)))
        self.assertTrue(self.clinic.add_staff_member(Doctor("lucas", "DOC0001", 8, 500)))
        self.assertTrue(self.clinic.add_patient(Patient("ron", "PAT0001", "0123456789", 1)))
        self.assertTrue(self.clinic.add_patient(VIPPatient("ana", "VIP0001", "0123456789", 2, "Gold")))

    def test_names_are_case_insensitive_and_unique(self):
        self.assertTrue(self.clinic.add_patient(Patient("ron", "PAT0001", "0123456789", 1)))
        self.assertFalse(self.clinic.add_staff_member(Doctor("RON", "DOC0001", 8, 300)))
        self.assertEqual(self.clinic.find_patient_by_name("RON").person_id, "PAT0001")

    def test_budget_status_uses_report_limit(self):
        self.clinic.add_staff_member(Doctor("within", "DOC0001", 8, 250))
        self.clinic.add_staff_member(Doctor("exceeded", "DOC0002", 8, 500))
        self.assertEqual(
            self.clinic.daily_report(300)["doctor_budget_status"],
            ["within: Within budget!", "exceeded: Budget exceeded!"],
        )

    def test_delete_by_id(self):
        self.clinic.add_patient(Patient("ron", "PAT0001", "0123456789", 1))
        self.assertTrue(self.clinic.delete_patient("pat0001"))
        self.assertIsNone(self.clinic.find_patient_by_id("PAT0001"))
        self.assertFalse(self.clinic.delete_patient("PAT0001"))

    def test_pickle_round_trip(self):
        with tempfile.TemporaryDirectory() as directory:
            original_path = storage_manager.DATA_FILE
            storage_manager.DATA_FILE = Path(directory) / "clinic_data.pkl"
            try:
                self.clinic.add_patient(Patient("ron", "PAT0001", "0123456789", 1))
                storage_manager.save_data(self.clinic)
                loaded = storage_manager.load_data()
                self.assertEqual(loaded.find_patient_by_name("RON").person_id, "PAT0001")
            finally:
                storage_manager.DATA_FILE = original_path


if __name__ == "__main__":
    unittest.main()
