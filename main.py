import time
import psutil
import os
import tensorflow as tf
from prometheus_client import start_http_server, Gauge
import board
import busio
from adafruit_ina3221 import INA3221
import paramiko
import threading

# Métriques Prometheus
cpu_usage = Gauge('cpu_usage', 'Percentage of CPU usage')
gpu_usage = Gauge('gpu_usage', 'Percentage of GPU usage')
ram_usage = Gauge('ram_usage', 'Percentage of RAM usage')
voltage_channel_1 = Gauge('voltage_channel_1', 'Voltage of Channel 1')
current_channel_1 = Gauge('current_channel_1', 'Current of Channel 1')
voltage_channel_2 = Gauge('voltage_channel_2', 'Voltage of Channel 2')
current_channel_2 = Gauge('current_channel_2', 'Current of Channel 2')
voltage_channel_3 = Gauge('voltage_channel_3', 'Voltage of Channel 3')
current_channel_3 = Gauge('current_channel_3', 'Current of Channel 3')

# Démarrer le serveur Prometheus sur le port 8000
start_http_server(8000)

# Initialiser I2C pour le capteur INA3221
i2c = busio.I2C(board.SCL, board.SDA)
ina3221 = INA3221(i2c)

# Fonction pour récupérer l'utilisation du GPU (via NVIDIA nvidia-smi)
def get_gpu_usage():
    try:
        gpu_usage = os.popen("nvidia-smi --query-gpu=utilization.gpu --format=csv,noheader,nounits").read()
        return int(gpu_usage.strip())
    except Exception as e:
        print("Erreur lors de la récupération des informations GPU:", e)
        return 0

# Fonction pour surveiller les performances et lire les données du capteur INA3221
def monitor_performance():
    """Surveiller les performances système et lire les données du capteur INA3221."""
    while True:
        # Obtenir les informations système
        cpu_usage.set(psutil.cpu_percent())  # Utilisation du CPU
        ram_usage.set(psutil.virtual_memory().percent())  # Utilisation de la RAM
        gpu_usage.set(get_gpu_usage())  # Utilisation du GPU

        # Lire les données du capteur INA3221 pour chaque canal
        for i in range(3):
            voltage = ina3221.voltage(i)
            current = ina3221.current(i)
            # Mettre à jour les métriques Prometheus pour chaque canal
            if i == 0:
                voltage_channel_1.set(voltage)
                current_channel_1.set(current)
            elif i == 1:
                voltage_channel_2.set(voltage)
                current_channel_2.set(current)
            elif i == 2:
                voltage_channel_3.set(voltage)
                current_channel_3.set(current)

        # Attendre 5 secondes avant la prochaine mise à jour
        time.sleep(5)

# Fonction pour l'entraînement distribué avec TensorFlow
def distributed_training():
    """Entraînement d'un modèle TensorFlow en utilisant des données fictives."""
    # Exemple de modèle pré-entraîné MobileNetV2
    model = tf.keras.applications.MobileNetV2(input_shape=(224, 224, 3), weights='imagenet', include_top=False)
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # Exemple de données fictives pour l'entraînement
    x_train = tf.random.normal([32, 224, 224, 3])  # Données d'entrée
    y_train = tf.random.uniform([32], maxval=1000, dtype=tf.int32)  # Labels de sortie

    # Entraînement du modèle
    model.fit(x_train, y_train, epochs=10, batch_size=32)

# Fonction pour se connecter à la Jetson Nano en SSH
def ssh_connect():
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connexion SSH avec l'adresse IP privée et la clé SSH
        ssh_client.connect('172.18.2.142', username='bmond', key_filename='C:/Users/bmond/.ssh/id_rsa')
        print("Connexion SSH établie avec la Jetson Nano")
        
        return ssh_client
    except Exception as e:
        print(f"Erreur lors de la connexion SSH: {e}")
        return None

if __name__ == "__main__":
    # Lancer la connexion SSH
    ssh_client = ssh_connect()
    
    if ssh_client is not None:
        # Lancer le monitoring des performances en arrière-plan
        performance_thread = threading.Thread(target=monitor_performance)
        performance_thread.daemon = True
        performance_thread.start()

        # Lancer l'entraînement distribué en parallèle
        distributed_training()

        # Fermer la connexion SSH
        ssh_client.close()
    else:
        print("La connexion SSH a échoué. Veuillez vérifier la configuration.")
