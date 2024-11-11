# Grafana and Prometheus Usage Guide

In this project, Prometheus is used to collect system performance metrics (CPU, RAM, GPU, etc.) and INA3221 sensor data, while Grafana visualizes this data in real time. Here’s a step-by-step guide to setting up and using Grafana and Prometheus in this context.

## 1. Installing Prometheus

Prometheus is used to collect, store, and expose performance metrics. It provides these metrics via an HTTP server that Grafana queries to display charts.

### 1.1. Download Prometheus

1. Go to the official Prometheus website.
2. Download the version compatible with your operating system.
3. Unzip the downloaded archive and place it in a folder.

### 1.2. Configure Prometheus

1. In the Prometheus folder, open the `prometheus.yml` file to configure the "targets" (data sources). This file should include the port where your application exposes metrics (by default, on `localhost:8000`).

Here is an example configuration to collect local metrics with Prometheus:

global:
  scrape_interval: 15s  # sampling frequency

scrape_configs:
  - job_name: 'jetson-nano-metrics'
 static_configs:
  - targets: ['localhost:8000']  # Prometheus collects the Data here.

2. Start Prometheus with the following command in the terminal from the folder where Prometheus is installed:

## 2. Installing Grafana

Grafana is used to visualize metrics collected by Prometheus. You can install Grafana on the same server or a remote machine.

### 2.1. Download and Install Grafana

1. Go to the official Grafana website and download the version for your operating system.
2. Unzip the downloaded archive and launch Grafana.

Grafana will be accessible at `http://localhost:3000` by default.

To start and enable Grafana on a Linux system, use the following commands:

```bash
sudo systemctl start grafana-server
sudo systemctl enable grafana-server

## 3. Configuring Grafana to Connect to Prometheus

Once Grafana is installed and running, follow these steps to connect Grafana to Prometheus.

### 3.1. Access Grafana

1. Open your browser and go to `http://localhost:3000`. The default username is `admin`, and the password is also `admin`.
2. You will be prompted to change the password on your first login.

### 3.2. Add Prometheus as a Data Source

1. In the Grafana sidebar, click on the gear icon (Configuration) and select "Data Sources."
2. Click on "Add data source."
3. Choose "Prometheus" as the data source type.
4. In the "HTTP" section, under "URL," enter your Prometheus server address. By default, this is `http://localhost:9090`.
5. Click "Save & Test" to verify that Grafana can connect to Prometheus.

## 4. Creating a Dashboard in Grafana

Once Prometheus is configured as a data source, you can create a dashboard to visualize your metrics.

### 4.1. Create a New Dashboard

1. In the sidebar, click on the "+" icon and select "Dashboard."
2. Click on "Add new panel" to add a chart.
3. In the "Query" section, select "Prometheus" as the data source.
4. Use Prometheus queries to retrieve metrics.

For example, to display CPU usage, use the following query:

5. Configure the chart display to your preferences (chart type, titles, legend, etc.).
6. Click "Apply" to add the chart to the dashboard.

### 4.2. Adding Other Metrics

Repeat these steps to add other metrics such as GPU usage, RAM usage, or INA3221 sensor voltages. Queries for these metrics may include:

- GPU Usage: `gpu_usage`
- RAM Usage: `ram_usage`
- Voltage Channel 1: `voltage_channel_1`
- Current Channel 1: `current_channel_1`

## 5. Visualizing Data

Once the dashboard is set up with the desired metrics, you can visualize in real time the performance of your Jetson Nano and INA3221 sensors. You can also set up alerts in Grafana to be notified if certain metrics exceed defined thresholds.

## 6. Conclusion

With Prometheus for metric collection and Grafana for visualization, you have a complete solution for monitoring system and INA3221 sensor performance on your Jetson Nano. The steps described will enable you to install and configure these tools for real-time monitoring.
