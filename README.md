![Python](https://img.shields.io/badge/Python-3.12-blue)
![Arduino](https://img.shields.io/badge/Arduino-Uno-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Matplotlib](https://img.shields.io/badge/Visualization-Matplotlib-orange)

# 🧠 MultiSensor_Logger

**Developer:** Adam Gosine  
**Hardware:** Arduino Uno + LDR + Joystick + Microphone  
**Languages:** C++ (Arduino), Python  
**Data Visualization:** Matplotlib + CSV logging  

---

## ⚙️ Overview

The **MultiSensor Logger** is an Arduino-based data acquisition system that captures real-time sensor readings from:
- **LDR (Light-Dependent Resistor):** Measures ambient light intensity  
- **Joystick (X, Y, Switch):** Captures movement and press actions  
- **Microphone:** Detects ambient sound levels  

All sensor values are:
- Streamed over serial at 115200 baud  
- Smoothed using an **Exponential Moving Average (EMA)**  
- Logged automatically into a **timestamped CSV file** (e.g., `log_2025-11-11_20-03-49.csv`)  
- Visualized live with **Matplotlib** during acquisition

---

## 🧰 Hardware Setup

| Sensor | Arduino Pin | Description |
|--------|--------------|-------------|
| LDR | A0 | Analog light intensity |
| Joystick X | A1 | Horizontal axis |
| Joystick Y | A2 | Vertical axis |
| Joystick SW | D2 | Button (INPUT_PULLUP) |
| Microphone (AOUT) | A3 | Analog sound signal |

All sensors share the **5V** and **GND** rails.

---

## 💻 Software

### 1️⃣ Arduino Code
- Collects data from all sensors
- Applies an EMA filter (`ALPHA = 0.25`)
- Streams comma-separated sensor data to serial

### 2️⃣ Python Script (`serial_log.py`)
- Connects to Arduino COM port  
- Waits for header line (auto sync)  
- Records
