# qiskitHadamard
Exemplo de porta Hadamard no Qiskit


Segue a seguir a implementação mais simples possível do qiskit: um gerador de números aleatórios.

Este tutorial foi baseado na aula oficial do Qiskit, disponível em: https://www.youtube.com/watch?v=RrUTwq5jKM4

Explicando linha a linha.

Importação do módulo qiskit a ser utilizado.

from qiskit import *

Cria um registrador quântico, ou seja, um qubit.

qr = QuantumRegister(1)

Cria um registrador clássico para armazenar a resposta, ou seja, um bit.

cr = ClassicalRegister(1)

Cria um circuito quântico, composto de um qubit e um bit

circuit = QuantumCircuit(qr,cr)

Aplica uma porta Hadamard, representado pelo “h”, sobre o primeiro qubit.

circuit.h(qr[0]) 

Faz a medição do circuito, armazenando no registrador clássico

circuit.measure(qr,cr)

O comando a seguir server para mostrar o circuito. Como estou utilizando o Spyder, estou utilizando “print”.

print(circuit)

#No Jupyter Notebook

#utilizar %matplotlib.inline

#circuit.draw()

![](https://informacaoquantica.files.wordpress.com/2020/04/hadamard.png)

Define qual o backend a utilizar. No caso, vou rodar num simulador de computador quântico, o qasm_simulator. Qasm vem de “quantum assembly simulator”.

simulator = Aer.get_backend('qasm_simulator')

Roda o circuito no simulador escolhido e armazena o resultado na variável “result”.

result = execute(circuit, backend=simulator).result()

print(result)

O resultado será algo como o da figura a seguir.
![](https://informacaoquantica.files.wordpress.com/2020/04/qiskit2.png)


O código a seguir serve para mostrar histograma dos resultados.

from qiskit.tools.visualization import plot_histogram

plot_histogram(result.get_counts(circuit))
![](https://informacaoquantica.files.wordpress.com/2020/04/qiskit3.png)

Relembrando um pouco da teoria.

Um qubit  

|0\rangle

após passar por uma porta Hadamard, gera um qubit no estado superposto:

\frac{|0\rangle+ |1\rangle}{ \sqrt{2}}

Este estado tem igual probabilidade de resultar em 0 ou 1, após ser medido – este é exatamente o resultado do qiskit, com 52,1% de resultar em 0 e 47,9%.

Existe uma aplicação prática de um circuito como o mostrado: um autêntico gerador de números aleatórios!

Qualquer gerador de números aleatórios encontrado num computador clássico não é autêntico. É sempre um algoritmo pseudo-aleatório, uma função tão errática que aparenta ter um comportamento aleatório, um procedimento determinístico, no final das contas.

Somente um computador quântico tem um comportamento verdadeiramente aleatório, por natureza!
