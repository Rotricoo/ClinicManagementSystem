# Purpose: display clinic summaries and registered people in a Tkinter window.
# Group members: Rick Grimes - 123456
# Date: 2026-09-14

import tkinter as tk
from tkinter import ttk


def open_dashboard(clinic):
    window = tk.Tk()
    window.title("Clinic Management Dashboard")
    window.geometry("760x560")
    window.minsize(680, 480)

    report = clinic.daily_report(300)
    header = ttk.Frame(window, padding=12)
    header.pack(fill="x")
    ttk.Label(header, text="Clinic Management Dashboard", font=("Segoe UI", 18, "bold")).pack(side="left")

    cards = ttk.Frame(window, padding=(12, 0, 12, 12))
    cards.pack(fill="x")
    card_values = {}
    card_definitions = (
        ("total_staff", "Staff"),
        ("total_patients", "Patients"),
        ("number_of_nurses", "Nurses"),
        ("number_of_doctors", "Doctors"),
    )
    for column, (key, label) in enumerate(card_definitions):
        card = ttk.LabelFrame(cards, text=label, padding=10)
        card.grid(row=0, column=column, padx=4, sticky="nsew")
        cards.columnconfigure(column, weight=1)
        card_values[key] = ttk.Label(card, font=("Segoe UI", 16, "bold"))
        card_values[key].pack()

    report_frame = ttk.LabelFrame(window, text="Daily report", padding=10)
    report_frame.pack(fill="x", padx=12, pady=(0, 10))
    report_text = ttk.Label(report_frame, justify="left")
    report_text.pack(anchor="w")

    table_frame = ttk.LabelFrame(window, text="Registered people", padding=10)
    table_frame.pack(fill="both", expand=True, padx=12, pady=(0, 12))
    tree = ttk.Treeview(table_frame, columns=("type", "name", "id"), show="headings")
    tree.heading("type", text="Type")
    tree.heading("name", text="Name")
    tree.heading("id", text="ID")
    tree.column("type", width=120)
    tree.column("name", width=260)
    tree.column("id", width=120)
    scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    tree.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    def refresh():
        # Rebuild all visible values from the model so Refresh remains reliable.
        report = clinic.daily_report(300)
        for key, label in card_values.items():
            label.config(text=report[key])
        statuses = "\n".join(report["doctor_budget_status"] or ["No doctors registered"])
        report_text.config(text=(
            f"Total patients attended: {report['total_patients_attended']}\n"
            f"Top nurse: {report['top_nurse']}\n"
            f"Doctor budget status:\n{statuses}\n"
            f"VIP patients: {report['number_of_vip_patients']}"
        ))
        tree.delete(*tree.get_children())
        for staff in clinic.staff_members:
            tree.insert("", "end", values=(type(staff).__name__, staff.name, staff.person_id))
        for patient in clinic.patients:
            tree.insert("", "end", values=(type(patient).__name__, patient.name, patient.person_id))

    ttk.Button(header, text="Refresh", command=refresh).pack(side="right", padx=(8, 0))
    ttk.Button(header, text="Close", command=window.destroy).pack(side="right")
    refresh()
    window.mainloop()

