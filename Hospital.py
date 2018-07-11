import random;
class Patient(object):
	"""docstring for Patient"""
	def __init__(self, id, name, allergies):
		# super(Patient, self).__init__()
		self.id = id;
		self.name = name;
		self.allergies = allergies;
		self.bed_number = None;
	def display_info(self):
		print self.name;
		print self.allergies;
		print self.bed_number;	
	
class Hospital(object):
			
			"""docstring for Hospital"""
			def __init__(self):
				self.patients = [];
				self.name = "Evergreen Hospital";
				self.capacity = 2;
				# super(Hospital, self).__init__()
				

			def admit(self,patient):
				if(len(self.patients) >= self.capacity):
					print "The Hospital is Full. Admission denied.";
				else:
					patient.bed_number = random.randint(0,200);
					self.patients.append(patient);
					print "Patient has been admitted to the Hospital. Bed number is: " + str(patient.bed_number);

			def discharge(self,patient_remove):
				for patient in self.patients:
					if(patient == patient_remove):
						patient.bed_number = None;
						self.patients.remove(patient);
						print "Patient Removed"
						break;		

patient1 = Patient(1,"susie","sulfa");
patient2 = Patient(2,"bob","peanuts");
patient3 = Patient(3,"fred","wheat");

evergreen = Hospital();

evergreen.admit(patient1);
evergreen.admit(patient2);
evergreen.admit(patient3);
evergreen.discharge(patient1);



						

		