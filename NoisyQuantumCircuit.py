# Import Basics
import qiskit
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

# Import the noise model object
from qiskit.providers.aer.noise import NoiseModel

# Import all standard errors
from qiskit.providers.aer.noise.errors import *  

class NoisyQuantumCircuit(QuantumCircuit):
    
    def __init__(self, qReg, cReg, nQubits, errors1Qubit, errors2Qubit):
        super().__init__(qReg, cReg)
        self.createNoiseModel(nQubits, errors1Qubit, errors2Qubit)
    
    def createNoiseModel(self, nQubits, errors1Qubit, errors2Qubit):
        self.noiseModel = NoiseModel()
        for i in range(nQubits):
    
            for error in errors1Qubit:
                self.noiseModel.add_quantum_error(error, ['h'], [i])
                self.noiseModel.add_quantum_error(error, ['iden'], [i])
                self.noiseModel.add_quantum_error(error, ['rx'], [i])
                self.noiseModel.add_quantum_error(error, ['ry'], [i])
                self.noiseModel.add_quantum_error(error, ['rz'], [i])
                self.noiseModel.add_quantum_error(error, ['s'], [i])
                self.noiseModel.add_quantum_error(error, ['sdg'], [i])
                self.noiseModel.add_quantum_error(error, ['t'], [i])
                self.noiseModel.add_quantum_error(error, ['tdg'], [i])
                self.noiseModel.add_quantum_error(error, ['u0'], [i])
                self.noiseModel.add_quantum_error(error, ['u1'], [i])
                self.noiseModel.add_quantum_error(error, ['u2'], [i])
                self.noiseModel.add_quantum_error(error, ['u3'], [i])
                self.noiseModel.add_quantum_error(error, ['x'], [i])
                self.noiseModel.add_quantum_error(error, ['y'], [i])
                self.noiseModel.add_quantum_error(error, ['z'], [i])

            for error in errors2Qubit:
                for j in range(nQubits):
                    self.noiseModel.add_quantum_error(error, ['cx'], [i,j])
                    self.noiseModel.add_quantum_error(error, ['cy'], [i,j])
                    self.noiseModel.add_quantum_error(error, ['cz'], [i,j])
                    self.noiseModel.add_quantum_error(error, ['ch'], [i,j])
                    self.noiseModel.add_quantum_error(error, ['crz'], [i,j])
                    self.noiseModel.add_quantum_error(error, ['cu1'], [i,j])
                    self.noiseModel.add_quantum_error(error, ['cu3'], [i,j])
                    self.noiseModel.add_quantum_error(error, ['swap'], [i,j])
                

    def getNoiseModel(self):
        return self.noiseModel
