# Enhancing Data Flows for Distributed ML Model Training

This project aims to develop a distributed training system for machine learning models, optimizing data flows between CPU and GPU. It addresses network architecture constraints, cache management, and software optimization to enable efficient resource utilization in a distributed environment.

## Project Background
Distributed training of machine learning models requires fast data exchanges between CPU and GPU to prevent bottlenecks. This project focuses on optimizing data transfer and memory cache allocation to maintain high performance. Expertise in software and network optimization is leveraged to improve data flow efficiency across the nodes of a distributed network.

## Features
- Optimization of data flows between CPU and GPU
- Efficient cache resource management to minimize access latency
- Real-time monitoring of resource usage (CPU, GPU, network)
- Modularity to adapt to different models and training requirements

## Required Hardware
- **NVIDIA Jetson Nano OKdo Developer Kit** (with cooling module): The Jetson Nano board will be used for parallel training, utilizing both GPU and CPU computing power for increased efficiency.
- **Central Server or Workstation with SSH Connection**: This server will manage and collect data across multiple Jetson Nano units.
- **Gigabit Ethernet Switch**: Ensures a fast network connection between the central server and Jetson Nano nodes.
- **INA3221 Power Sensor (optional)**: Provides detailed power consumption monitoring during training (optional for energy performance tests).

## Required Software
All software can be installed via pip in a Python environment under Visual Studio Code:

- **Python 3.x**
- **TensorFlow or PyTorch**: For ML model training on the Jetson Nano.
- **Prometheus and Grafana**: For real-time performance monitoring and metric visualization.
- **CUDA**: Used for GPU acceleration with machine learning libraries.
- **OpenSSH**: For secure connections between the central server and nodes.

## Project Steps

### 1. Environment Preparation
- **Jetson Nano Setup**: Install Ubuntu 20.04 LTS on the Jetson Nano, configure network access, and check CUDA compatibility.
- **Dependency Installation**: Install TensorFlow or PyTorch, Prometheus, and Grafana for performance monitoring and model training on the Jetson Nano units.

### 2. Network Installation and Configuration
- **Node Connection**: Connect each Jetson Nano to the network via the Gigabit Ethernet switch.
- **SSH Configuration**: Set up SSH connections between the central server and each Jetson Nano for secure remote command execution for training and monitoring.

### 3. Data Flow Optimization
- **Performance Monitoring**: Deploy Prometheus on each Jetson Nano to track CPU, GPU, and cache metrics in real-time.
- **Python Script Development**: Create scripts to manage data transfer, batch loading, and cache management to reduce latency during parallel training across multiple Jetson Nanos.
- **Visualization with Grafana**: Set up dashboards in Grafana to display performance and power consumption data from the Jetson Nanos in real-time.

### 4. Distributed Training Testing and Optimization
- **Load and Latency Testing**: Measure latency and loading times to identify bottlenecks in data flow.
- **Network and Cache Parameter Optimization**: Adjust settings to minimize latency and improve training performance.
- **Optimization Reports**: Generate reports on performance, latency, and energy consumption to identify areas for improvement.

### 5. Documentation and Usage
Document all configurations, installations, and troubleshooting procedures in a guide for reproducibility.

## Project Usage
To start distributed training, run the main script from the central server. The Jetson Nanos will receive instructions and send performance data in real-time. Metrics are accessible in Grafana for continuous visualization.
