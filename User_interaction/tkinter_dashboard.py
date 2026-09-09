import tkinter as tk

def open_dashboard(clinic):
    window = tk.Tk()
    window.title("Daily Report Dashboard")
    window.geometry("500x400")

    report = clinic.daily_report(300)
    doctor_budget_text = "\n".join(report["doctor_budget_status"])

    tk.Label(window, text="Daily Report Dashboard", font=("Arial", 16, "bold")).pack(pady=10)

    report_frame = tk.Frame(window)
    report_frame.pack(pady=10)

    tk.Label(report_frame, text=f"Total staff: {report['total_staff']}").pack(anchor="w", pady=2)
    tk.Label(report_frame, text=f"Number of nurses: {report['number_of_nurses']}").pack(anchor="w", pady=2)
    tk.Label(report_frame, text=f"Number of doctors: {report['number_of_doctors']}").pack(anchor="w", pady=2)
    tk.Label(report_frame, text=f"Total patients attended: {report['total_patients_attended']}").pack(anchor="w", pady=2)
    tk.Label(report_frame, text=f"Top nurse: {report['top_nurse']}").pack(anchor="w", pady=2)
    tk.Label(report_frame, text=f"Doctor budget status:\n{doctor_budget_text}").pack(anchor="w", pady=2)
    tk.Label(report_frame, text=f"Total patients: {report['total_patients']}").pack(anchor="w", pady=2)
    tk.Label(report_frame, text=f"VIP patients: {report['number_of_vip_patients']}").pack(anchor="w", pady=2)

    window.mainloop()

