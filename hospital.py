# Name: Vinson Aiono
# Date: 4/3/2018
# Coding Dojo Python Stack
# Description: Create two classes. one call and one callcenters

# Create a hospital class that has patients
# Patient Attributes
# patient id number, name, allergies, room number
class Patient:
    def __init__(self, idNumber, name, allergies):
        self.idNumber = idNumber
        self.name = name
        self.allergies = allergies
        self.room = 0
class Hospital:
    def  __init__(self, hospitalName, capacity):
        self.patients = []
        self.hospitalName = hospitalName
        self.capacity = capacity

    def admit(self, patient):

        if len(self.patients) >= self.capacity:
            print('Hospital has reached max capacity')
            return self
        self.patients.append(patient)
        
        patient.room = len(self.patients)-1     
        return self

    def discharge(self, patient):
        for x in range(1, len(self.patients)):
            self.patients[x-1] = self.patients[x]
        self.room = None
    def info(self):
        # mkae if statement to to check for max capacity
        print('Patients:', len(self.patients))
        for x in range(0, len(self.patients)):
            print('Name:', self.patients[x].name)
            print('Room:', self.patients[x].room)
            print('----------------')
        return self
    
# HOSPITAL
St_Bonaventure = Hospital('St Bonaventure', 3)
#PATIENTS
patient1 = Patient(1, 'John', 'cold')
patient2= Patient(2, 'Jane', 'cough')
patient3 = Patient(3, 'Jim', 'flu')
patient4 = Patient(3, 'Jim', 'flu')

St_Bonaventure.admit(patient1).admit(patient2).admit(patient3).admit(patient4).info()