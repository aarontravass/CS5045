from datetime import date, datetime
import uuid


class Patient:
    patient_guid_dt = []
    patient_guid = ""
    name = ""
    gender = ""
    address = ""
    phone_number = ""
    date_of_birth = ""
    age = 0

    def __init__(self, name, gender, address, phone_number, date_of_birth):
        if not self.isValid(date_of_birth):
            print("Date of birth format is invalid. Format should be YYYY-MM-DD")
            return
        self.patient_guid = str(uuid.uuid4())
        Patient.patient_guid_at.append(self.patient_guid)
        self.name = name
        self.gender = gender
        self.address = address
        self.phone_number = phone_number
        self.date_of_birth = date_of_birth
        self.age = self.calculate_age(date_of_birth)
        print("Successfully added patient data")
        return

    def isValid(date_of_birth):
        try:
            datetime.datetime.strptime(date_of_birth, '%Y-%m-%d')
            return True
        except:
            return False

    def calculate_age(date_of_birth):
        dt = [int(s) for s in date_of_birth.split('-')]
        born = date(dt[0], dt[1], dt[2])
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


class Doctor:
    doctor_guid_at = []
    doctor_guid = ''
    registration_number_dt = []
    registration_number = ''
    name = ""
    qualification = ""
    specialization = ""
    phone_number = ""

    def __init__(self, name, registration_number, qualification, specialization, phone_number):
        if not self.isRegistrationNoUnique(registration_number):
            print("Registration Number must be unique")
            return
        if (qualification != 'DO' or qualification != 'MD'):
            print("Qualification must be either DO or MD")
            return
        self.doctor_guid = str(uuid.uuid4())
        Doctor.doctor_guid_at.append(self.doctor_guid)
        self.name = name
        Doctor.registration_number_dt.append(registration_number)
        self.registration_number = registration_number
        self.qualification = qualification
        self.specialization = specialization
        self.phone_number = phone_number
        print("Successfully added doctor data")
        return

    def isRegistrationNoUnique(registration_number):
        return registration_number in Doctor.registration_number_dt


class PatientHealthReport:
    doctor_guid = ''
    patient_guid = ''
    last_date_of_checkup = ''
    health_problems = []
    list_of_medicines = []
    cost = 0
    report = ""

    def __init__(self, doctor_guid, patient_uid, last_date_of_checkup, health_problems, list_of_medicines, cost,
                 report):
        if not doctor_guid in Doctor.doctor_guid_at:
            print("Doctor Guid should be valid")
            return
        if not patient_uid in Patient.patient_guid_dt:
            print("Patient Guid should be valid")
            return
        self.doctor_guid = doctor_guid
        self.patient_guid = patient_uid
        self.last_date_of_checkup = last_date_of_checkup
        self.health_problems = health_problems
        self.list_of_medicines = list_of_medicines
        self.cost = cost
        self.report = report
        print("Successfully added Health report")
        return

