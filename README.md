# quantique-tp

## Prérequis

- Python 3.x installé

- Un compte IBM Quantum

- Une clé API IBM Quantum

- Fichier .env contenant :

- IBMQ_API_TOKEN=your_api_key_here

## Dépendances Python :
```
pip install qiskit qiskit-ibm-provider python-dotenv
```
 
### Installation

Clonez ce dépôt :

```
git clone https://github.com/votre-repo.git
cd votre-repo
```

Installez les dépendances :
```
pip install -r requirements.txt
```
Ajoutez votre clé API IBM Quantum dans un fichier .env.

## Utilisation

Exécutez le script pour soumettre un circuit quantique :
```
python ibm_quantum_job.py
```
## Fonctionnalités

- Chargement sécurisé de la clé API depuis .env

- Connexion à IBM Quantum via IBMProvider

- Création d'un circuit quantique simple (porte Hadamard et CNOT)

- Envoi et exécution sur le simulateur ibmq_qasm_simulator

Affichage de l'ID du job soumis
