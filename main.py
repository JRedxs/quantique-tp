import os
from qiskit import QuantumCircuit, transpile, assemble
from qiskit_ibm_provider import IBMProvider
from dotenv import dotenv_values

config = dotenv_values(".env")
api_key = config.get("IBMQ_API_TOKEN")

if not api_key:
    raise RuntimeError("⚠️ Impossible de récupérer la clé API IBM Quantum. Vérifie le fichier .env.")

provider = IBMProvider(token=api_key)

simulator = provider.get_backend("ibmq_qasm_simulator")

circuit = QuantumCircuit(2)
circuit.h(0)
circuit.cx(0, 1)
circuit.measure_all()

compiled_circuit = transpile(circuit, simulator)
qobj = assemble(compiled_circuit)
execution = simulator.run(qobj)

print(f"✅ Job soumis avec succès ! ID du job : {execution.job_id()}")
