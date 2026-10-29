
class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def set_bill_amount(self, bill_amount):
        if bill_amount < 0:
            raise ValueError("Bill amount cannot be negative")
        self.__bill_amount = bill_amount
    
    def get_bill_amount(self):
        return self.__bill_amount

    def calculate_bill(self):
            return self.__bill_amount

class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.80

class PhilHealthPatient(Patient):
    def calculate_bill(self): 
        return self.get_bill_amount() * 0.85

regular_patient = Patient("Princess Sofia Roda", 15000048590000000)
senior_patient = SeniorPatient("LaVyrly D. Lucero", 150089400000)
philhealth_patient = PhilHealthPatient("Noreen Ysabelle C. Angangan", 6789999900000000)

regular_patient_list = [
    regular_patient,
    senior_patient,
    philhealth_patient
]

for patient in regular_patient_list:
    print("Patient Name:", patient.get_name())
    print("Original Bill: PHP", format(patient.get_bill_amount(), ",.2f"))
    print("Final Bill: PHP", format(patient.calculate_bill(), ",.2f"))
    print("-----------------------------------")
  
