# INA3221 Sensor Usage Guide

The INA3221 sensor is a three-channel voltage and current monitor designed to measure the voltage and current of different systems. It is ideal for monitoring the power supply of components in your multi-node AI architecture project, particularly for obtaining detailed information on the power consumption of AI nodes. This guide will walk you through how to connect and use the INA3221 sensor with your Jetson Nano and retrieve measurement data.

---

## 1. Introduction to the INA3221 Sensor

The INA3221 is a three-channel voltage and current sensor capable of measuring:
- Voltage (for each channel)
- Current (for each channel)
- Power (calculated from voltage and current)

This sensor uses an I2C interface to communicate with the Jetson Nano. This allows you to retrieve data via I2C queries for each channel.

---

## 2. Required Hardware

- Jetson Nano
- INA3221 Sensor
- Connection cables (to connect the INA3221 to the Jetson Nano)
- Power supply for the Jetson Nano and the devices to be measured

---

## 3. Connecting the INA3221 Sensor to the Jetson Nano

The INA3221 sensor connects to the Jetson Nano via the I2C interface. Here are the steps to make the connection:

1. **Pinout of the Jetson Nano:**
   - VCC (INA3221) → 3.3V (Jetson Nano)
   - GND (INA3221) → GND (Jetson Nano)
   - SDA (INA3221) → SDA (Jetson Nano)
   - SCL (INA3221) → SCL (Jetson Nano)

2. Use the cables to connect the corresponding pins of the Jetson Nano to the pins of the INA3221 sensor.

3. The INA3221 is powered by 3.3V, so it is important not to connect the INA3221 to a higher voltage pin (such as 5V), as this could damage the sensor.

---

## 4. Installing the Python Library for INA3221

To interact with the INA3221 sensor from Python, you need to use a library that supports I2C communication and reading sensor data.

### 4.1. Install Dependencies

1. Open a terminal on the Jetson Nano and ensure the I2C interface is enabled:
    ```bash
    sudo systemctl enable i2c
    sudo systemctl start i2c
    ```

2. Install the necessary libraries:
    ```bash
    sudo apt-get install python3-smbus i2c-tools
    ```

3. Install the Python INA3221 library:
    Several Python libraries are available, but a popular and well-supported one is `ina3221`. Install it with pip:
    ```bash
    sudo pip3 install ina3221
    ```

---

## 5. Verifying the I2C Connection

Before you start retrieving data, it's important to verify that the I2C interface is correctly configured and that the INA3221 sensor is detected.

1. List connected I2C devices:
    ```bash
    sudo i2cdetect -y 1
    ```

2. If the INA3221 sensor is correctly connected, you should see an address (usually 0x40) in the displayed table.

---

## 6. Reading Data from the INA3221 Sensor

Once the I2C connection is established and the sensor is detected, you can start reading the voltage, current, and power measurement data for each channel.

---

## 7. Visualizing Data with Grafana

Once you have retrieved the voltage, current, and power data from the INA3221, you can send this data to Prometheus and visualize it in Grafana.

### 7.1. Configure Prometheus to Retrieve INA3221 Metrics

You can use PushGateway or a custom Python script to send INA3221 data to Prometheus.

1. Install `prometheus_client` to send metrics from Python:
    ```bash
    sudo pip3 install prometheus_client
    ```

You now need to send the data to Prometheus, where it can be retrieved by Grafana for display.

---

## 8. Conclusion

The INA3221 sensor provides crucial data for monitoring the energy consumption of your AI nodes, which is essential in performance optimization and energy efficiency management projects. Thanks to its ease of connection via I2C and its ability to measure the voltage and current of three different channels, it is an ideal tool for monitoring your hardware. By integrating INA3221 with Prometheus and Grafana, you get a complete solution for monitoring and visualizing the performance of your systems.
