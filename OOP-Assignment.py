class Person:
    def __init__(self, name, age, gender, phone_number):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone_number = phone_number

class Patient(Person):
    def __init__(self, name, age, gender, phone_number, medical_history):
        super().__init__(name, age, gender, phone_number)
        self.medical_history = medical_history
        self.appointments = []
        self.test_reports = {}

    def make_appointment(self, hospital):
        matching_doctors = []
        doctor_name = input("Enter the name of the doctor you want to make an appointment with: ")
        for doctor in hospital.doctors:
            if doctor.name == doctor_name:
                matching_doctors.append(doctor)
        if matching_doctors:
            date_time = input("Enter the appointment date and time (e.g., '2023-09-20 10:00 AM'): ")
            appointment = Appointment(matching_doctors[0], self, date_time)
            self.appointments.append(appointment)
            print(f"Appointment with Dr. {doctor_name} made successfully.")
        else:
            print(f"Doctor {doctor_name} not found in the hospital.")

    def view_appointments(self):
        if self.appointments:
            print("Your Appointments:")
            for appointment in self.appointments:
                print(appointment)
        else:
            print("You have no appointments.")

    def request_lab_test(self, test_name, laboratory):
        if test_name in laboratory.tests:
            report = laboratory.perform_test(self, test_name)
            if report is not None:
                self.test_reports[test_name] = report
                print(f"Test '{test_name}' performed successfully.")
                print(report)
            else:
                print(f"Test '{test_name}' result not available.")
        else:
            print(f"Test '{test_name}' not found in the test center.")

    def search_doctors(self, hospital, specialization):
        matching_doctors = []
        for doctor in hospital.doctors:
            if doctor.specialization == specialization:
                matching_doctors.append(doctor)
        if matching_doctors:
            print(f"Doctors with specialization '{specialization}':")
            for doctor in matching_doctors:
                print(doctor)
        else:
            print(f"No doctors found with specialization '{specialization}'.")

    def search_test_report(self, test_name):
        if test_name in self.test_reports:
            print(self.test_reports[test_name])
        else:
            print(f"Test report for '{test_name}' not found.")
    
    def __str__(self):
        return f"Patient: {self.name}, Age: {self.age}, Gender: {self.gender}, Phone Number: {self.phone_number}, Medical History: {self.medical_history}"

class Doctor(Person):
    def __init__(self, name, age, gender, phone_number, specialization):
        super().__init__(name, age, gender, phone_number)
        self.specialization = specialization

    def __str__(self):
        return f'Doctor: {self.name}, Age: {self.age}, Gender: {self.gender}, Phone_Number: {self.phone_number}, Specialization: {self.specialization}'

class Nurse(Person):
    def __init__(self, name, age, gender, phone_number, department):
        super().__init__(name, age, gender, phone_number)
        self.department = department

    def __str__(self):
        return f'Nurse: {self.name}, Age: {self.age}, Gender: {self.gender}, Phone_Number: {self.phone_number},  Department: {self.department}'

class Laboratory:
    def __init__(self, name):
        self.name = name
        self.tests = {}

    def add_test(self, test_name, description):
        self.tests[test_name] = description

    def perform_test(self, patient, test_name):
        if test_name in self.tests:
            report = f"Test Report of {patient.name} for - {test_name}: Result - Normal"
            return report
        else:
            return "Test not found in the test center."

    def __str__(self):
        return f'Test Center: {self.name}'

class Appointment:
    def __init__(self, doctor, patient, date_time):
        self.doctor = doctor
        self.patient = patient
        self.date_time = date_time

    def __str__(self):
        return f'Appointment with Dr. {self.doctor.name} at {self.date_time}'

class Hospital:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.doctors = []
        self.nurses = []
        self.patients = []
        self.laboratorys = []

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def update_doctor_info(self):
        name = input("Please enter the name of the doctor whose information you want to update: ")
        for doctor in self.doctors:
            if doctor.name == name:
                print(f"Doctor {name}'s current information:")
                print(doctor)
                field = input("Enter the field you want to update (name/age/gender/phone_number/specialization): ")
                if field == 'name':
                    new_name = input("Enter the new name: ")
                    doctor.name = new_name
                elif field == 'age':
                    new_age = int(input("Enter the new age: "))
                    doctor.age = new_age
                elif field == 'gender':
                    new_gender = input("Enter the new gender: ")
                    doctor.gender = new_gender
                elif field == 'phone_number':
                    new_phone_number = input("Enter the new phone number: ")
                    doctor.phone_number = new_phone_number
                elif field == 'specialization':
                    new_specialization = input("Enter the new specialization: ")
                    doctor.specialization = new_specialization
                else:
                    print("Invalid field.")
                print(f"Doctor {name}'s information updated successfully.")
                return
        print(f"Doctor {name} not found in the hospital.")
    
    def delete_doctor(self, doctor_name):
        for doctor in self.doctors:
            if doctor.name == doctor_name:
                self.doctors.remove(doctor)
                print(f"Doctor {doctor_name} has been removed from the hospital.")
                return
        print(f"Doctor {doctor_name} not found in the hospital.")
    
    def add_nurse(self, nurse):
        self.nurses.append(nurse)

    def update_nurse_info(self):
        name = input("Please enter the name of the nurse whose information you want to update: ")
        for nurse in self.nurses:
            if nurse.name == name:
                print(f"Nurse {name}'s current information:")
                print(nurse)
                field = input("Enter the field you want to update (name/age/gender/phone_number/department): ")
                if field == 'name':
                    new_name = input("Enter the new name: ")
                    nurse.name = new_name
                elif field == 'age':
                    new_age = int(input("Enter the new age: "))
                    nurse.age = new_age
                elif field == 'gender':
                    new_gender = input("Enter the new gender: ")
                    nurse.gender = new_gender
                elif field == 'phone_number':
                    new_phone_number = input("Enter the new phone number: ")
                    nurse.phone_number = new_phone_number
                elif field == 'department':
                    new_department = input("Enter the new department: ")
                    nurse.department = new_department
                else:
                    print("Invalid field.")
                print(f"Nurse {name}'s information updated successfully.")
                return
        print(f"Nurse {name} not found in the hospital.")

    def delete_nurse(self, nurse_name):
        for nurse in self.nurses:
            if nurse.name == nurse_name:
                self.nurses.remove(nurse)
                print(f"Nurse {nurse_name} has been removed from the hospital.")
                return
        print(f"Nurse {nurse_name} not found in the hospital.")

    def add_patient(self, patient):
        self.patients.append(patient)

    def list_doctors(self):
        for doctor in self.doctors:
            print(doctor)
    
    def list_patients(self):
        for patient in self.patients:
            print(patient)
    
    def list_nurses(self):
        for nurse in self.nurses:
            print(nurse)
    
    def list_laboratorys(self):
        for laboratory in self.laboratorys:
            print(laboratory)

    def add_laboratory(self, laboratory):
        self.laboratorys.append(laboratory)

    def delete_laboratory(self, laboratory_name):
        for laboratory in self.laboratorys:
            if laboratory.name == laboratory_name:
                self.laboratorys.remove(laboratory)
                print(f"Test Center {laboratory_name} has been removed from the hospital.")
                return
        print(f"Test Center {laboratory_name} not found in the hospital.")

    def __str__(self):
        return f'Hospital: {self.name}, Location: {self.location}'


hospital = Hospital("ABC Hospital", "City Center")
def Display():
    Do = input("Please Press S to start the program: ")
    while Do != "t":
        print("a. If you want to add patient.")
        print("b. If you want to add doctor.")
        print("c. If you want to add nurse.")
        print("d. If you want to add Labporatory.")
        print("e. If you want tests to be performed.")
        print("f. if you want to see the list of all patient.")
        print("g. if you want to see the list of all doctors.")
        print("h. if you want to see the list of all nurses.")
        print("i. if you want to see the list of all laboratories.")
        print("j. if you want to delete doctor from hospital.")
        print("k. if you want to delete nurse from hospital.")
        print("l. if you want to delete laboratory from hospital.")
        print("m. if you want to update the info of doctor.")
        print("n. if you want to update the info of nurse.")
        print("o. if you want to search for any speciific doctor.")
        print("p. if you want to search for any specific test.") 
        print("q. if you want to make an appointment with a doctor.")
        print("r. if you want to view all the appointments.")         
        Choice = input("Enter your choice from above Options: ")     
        
        if Choice == 'a':
            loop = int(input("how many patients you want to add: "))
            for i in range(loop):
                name = input("Please! Enter Patient's name: ")
                age = int(input("Please! Enter Patient's age: "))
                gender = input("Please! Enter Patient's gender: ")
                phone_number = input("Please! Enter Patient's Phone number: ")
                history = input("Please! Enter Patient's medical history: ")
                patient = Patient(name, age, gender, phone_number, history)
                hospital.add_patient(patient)
        if Choice == 'b':
            loop = int(input("how many doctors you want to add: "))
            for i in range(loop):
                name = input("Please! Enter Doctor's name: ")
                age = int(input("Please! Enter Doctor's age: "))
                gender = input("Please! Enter Doctor's gender: ")
                phone_number = input("Please! Enter Doctor's Phone number: ")
                specialization = input("Please! Enter Doctor's Specialization: ")
                doctor = Doctor(name, age, gender, phone_number, specialization)
                hospital.add_doctor(doctor)
        if Choice == 'c':
            loop = int(input("how many nurses you want to add: "))
            for i in range(loop):
                name = input("Please! Enter Nurse's name: ")
                age = int(input("Please! Enter Nurse's age: "))
                gender = input("Please! Enter Nurse's gender: ")
                phone_number = input("Please! Enter Nurse's Phone number: ")
                department = input("Please! Enter Nurse's Department: ")
                nurse = Nurse(name, age, gender, phone_number, department)
                hospital.add_nurse(nurse)
        if Choice == 'd':
            loop = int(input("how many laboratories you want to add: "))
            for i in range(loop):
                name = input("Please! Enter Laboratories's name: ")
                laboratory = Laboratory(name)
                hospital.add_laboratory(laboratory)
        if Choice == 'e':
            loop = int(input("how many tests you want to perfrom: "))
            for i in range(loop):
                name = input("Please! Enter Laboratories's name: ")
                laboratory = Laboratory(name)
                name1 = input("Please! Enter Test's name: ")
                description = input("Please! Enter Test's Description: ")
                test = laboratory.add_test(name1, description)
                patient.request_lab_test(name1, laboratory)
        if Choice == 'f':
            hospital.list_patients()
        if Choice == 'g':
            hospital.list_doctors()
        if Choice == 'h':
            hospital.list_nurses()
        if Choice == 'i':
            hospital.list_laboratorys()
        if Choice == 'j':
            name = input("Please! Enter Doctor's name: ")
            hospital.delete_doctor(name)
        if Choice == 'k':
            name = input("Please! Enter Nurse's name: ")
            hospital.delete_nurse(name)
        if Choice == 'l':
            name = input("Please! Enter Test Center's name: ")
            hospital.delete_laboratory(name)
        if Choice == 'm':
            hospital.update_doctor_info()
        if Choice == 'n':
            hospital.update_nurse_info()
        if Choice == 'o':
            specialization = input("Please! Enter Doctor's Specialization: ")
            patient.search_doctors(hospital, specialization)
        if Choice == 'p':
            name = input("Please! Enter Test's name: ")
            patient.search_test_report(name)
        if Choice == 'q':
            patient.make_appointment(hospital)
        if Choice == 'r':
            patient_name = input("Enter the patient's name to view appointments: ")
            for patient in hospital.patients:
                if patient.name == patient_name:
                    patient.view_appointments()
                    break
                else:
                    print(f"Patient {patient_name} not found in the hospital.")
        if Choice == 't':
            print("Invalid Command")
            break

Display()
