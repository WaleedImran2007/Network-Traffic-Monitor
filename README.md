# 🚀 Network Traffic Monitor

A real-time network traffic monitoring system that captures, analyzes, and visualizes network packets using Python and a web-based interface.

---

## 📸 Screenshots

### 🖥️ Dashboard
<p align="center">
  <img src="https://github.com/user-attachments/assets/56cc7532-7f0b-4ce9-b013-0d8cf8748a79" width="800"/>
</p>

---

### 📡 Packet Capturing
<p align="center">
  <img src="https://github.com/user-attachments/assets/307bc377-99fd-4761-b9ae-c7c9a527f014" width="800"/>
</p>

---

### 🧹 Clear Data Feature
<p align="center">
  <img src="https://github.com/user-attachments/assets/20cfa167-aa54-4150-baa0-0cb856f62e75" width="800"/>
</p>

---

### ✅ After Clearing Data
<p align="center">
  <img src="https://github.com/user-attachments/assets/a80926d2-e826-4f28-8b25-480b8249bde3" width="800"/>
</p>

---

## 🔍 Real-Time Traffic Analysis (Important)

<p align="center">
  <img src="https://github.com/user-attachments/assets/46335f36-4cf5-477a-bb15-33fb4c2cccad" width="600"/>
</p>

While capturing live traffic, the system monitored packets during an active video call session.

- The application detected a large number of **UDP packets** originating from IP `74.125.250.240`
- This IP belongs to **Google’s infrastructure**, used by video streaming services
- The high packet rate occurs because video streams send **30–60 frames per second**, each transmitted as individual packets

### ⚡ Why UDP is Used Instead of TCP?

- **UDP (User Datagram Protocol)** prioritizes speed over reliability  
- Lost packets are simply ignored → ensures smooth video playback  
- **TCP**, on the other hand:
  - Retransmits lost packets  
  - Causes delays and freezing in real-time communication  

👉 This is why platforms like video conferencing and streaming services rely heavily on UDP.

---

## 🛠️ Features

- 📡 Live packet capture  
- 🔍 Protocol identification (TCP, UDP, ICMP)  
- 📊 Real-time statistics visualization  
- 🌐 Web-based dashboard  
- 🧹 Clear/reset captured data functionality  

---

## ⚙️ Tech Stack

- **Python** (Scapy for packet sniffing)  
- **Flask** (Backend server)  
- **HTML, CSS, JavaScript** (Frontend)  

---

## 💡 Conclusion

This project demonstrates practical implementation of core networking concepts including packet sniffing, protocol analysis, and real-time data visualization in a full-stack environment.

---
