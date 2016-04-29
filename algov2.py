import sys

class patient:
    def __init__(self, req, esi, idx):
        self.req = req
        self.esi = esi
        self.idx = idx

def addPatient(p, patientQueue):
	counter = 0
	for c in patientQueue:
		if(p.req < c.req):
			patientQueue.insert(counter, p)
			return patientQueue
		elif(p.req == c.req):
			if(p.esi < c.esi):
				patientQueue.insert(counter , p)
				return patientQueue
		counter = counter + 1

	patientQueue.append(p)
	return patientQueue






if __name__ == "__main__":
	patientQueue = []
	patienta = patient(3, 1, "a")
	patientb = patient(6, 4, "b")
	patientc = patient(2, 3, "c")
	patientd = patient(0, 4, "d")
	patiente = patient(2, 2, "e")
	patientf = patient(6, 1, "f")

	addPatient(patienta, patientQueue)
	addPatient(patientb, patientQueue)
	addPatient(patientc, patientQueue)
	addPatient(patientd, patientQueue)
	addPatient(patiente, patientQueue)
	addPatient(patientf, patientQueue)

	print("finalQueue")
	for p in patientQueue:
		print p.idx





