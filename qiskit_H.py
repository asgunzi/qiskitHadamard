# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 02:13:03 2020

@author: asgun
"""


from qiskit import *

qr = QuantumRegister(1)
cr = ClassicalRegister(1)

#Cria um circuito quântico, composto de um qubit e um bit
circuit = QuantumCircuit(qr,cr)

#Aplica uma porta Hadamard
circuit.h(qr[0])

#Faz a medição do circuito, armazenando no registrador clássico
circuit.measure(qr,cr)

print(circuit)
#No Jupyter Notebook
#utilizar %matplotlib.inline
#circuit.draw() 


#Define qual o backend a utilizar. No caso, vou rodar num simulador de computador quântico
simulator = Aer.get_backend('qasm_simulator')

#Roda o circuito no simulador escolhido e armazena o resultado na variável result
result = execute(circuit, backend=simulator).result()
print(result)

#Mostrar histograma dos resultados
from qiskit.tools.visualization import plot_histogram
plot_histogram(result.get_counts(circuit))
