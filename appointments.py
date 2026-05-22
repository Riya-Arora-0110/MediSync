class Appointments:
    def __init__(self, patient_name, doctor_name, date, time, location):
        self.patient_name = patient_name
        self.doctor_name = doctor_name
        self.date = date
        self.time = time
        self.location = location

    def schedule(self):
        return f"Appointment scheduled fpr {self.patient_name} with Dr. {self.doctor_name} on {self.date} at {self.time}"

if __name == "__main__":
    appointment1 = Appointment("John Doe", "Smith", "2026-05-22", "10:30 AM")
    print(appointment1.schedule())