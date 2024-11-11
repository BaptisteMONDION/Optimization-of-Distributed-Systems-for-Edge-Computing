#!/bin/bash

# Mettre à jour le système
sudo apt update -y
sudo apt upgrade -y

# Installer les dépendances système nécessaires
sudo apt install -y python3-pip python3-dev python3-venv git

# Installer TensorFlow, psutil, prometheus_client, et autres packages Python nécessaires
pip3 install tensorflow psutil prometheus_client adafruit-ina3221 adafruit-blinka

# Installer NVIDIA drivers et CUDA (si non déjà installés pour TensorFlow et le GPU)
sudo apt install -y nvidia-driver-460
sudo apt install -y nvidia-cuda-toolkit

# Vérifier que les dépendances sont installées correctement
echo "Vérification de l'installation de TensorFlow"
python3 -c "import tensorflow as tf; print('TensorFlow version:', tf.__version__)"

echo "Vérification de l'installation de psutil"
python3 -c "import psutil; print('psutil version:', psutil.__version__)"

echo "Vérification de l'installation de Prometheus Client"
python3 -c "import prometheus_client; print('prometheus_client version:', prometheus_client.__version__)"

echo "Vérification de l'installation de Adafruit INA3221"
python3 -c "import adafruit_ina3221; print('adafruit_ina3221 version:', adafruit_ina3221.__version__)"

echo "Installation terminée. Vous pouvez maintenant exécuter le script avec ./run.sh."
