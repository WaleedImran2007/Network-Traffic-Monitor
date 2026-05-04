# Network-Traffic-Monitor
A real-time network traffic monitoring system that captures, analyzes, and visualizes network packets using Python and a web-based interface.

# Screenshots of Working System

# DASHBOARD:
<img width="1919" height="1000" alt="image" src="https://github.com/user-attachments/assets/56cc7532-7f0b-4ce9-b013-0d8cf8748a79" />

# Packet Capturing:
<img width="1919" height="1004" alt="image" src="https://github.com/user-attachments/assets/307bc377-99fd-4761-b9ae-c7c9a527f014" />

# Clear Data:
<img width="1919" height="1127" alt="image" src="https://github.com/user-attachments/assets/20cfa167-aa54-4150-baa0-0cb856f62e75" />

# Cleared:
<img width="1919" height="1005" alt="image" src="https://github.com/user-attachments/assets/a80926d2-e826-4f28-8b25-480b8249bde3" />

# Important:
<img width="959" height="563" alt="First SS" src="https://github.com/user-attachments/assets/46335f36-4cf5-477a-bb15-33fb4c2cccad" />

As visible in my browser tabs, I am currently attending a live lecture on Google Meet. My packet sniffer website captured this real-time traffic, showing hundreds of UDP packets flooding in from IP 74.125.250.240 — a Google-owned server. This IP belongs to Google's infrastructure which Meet uses to stream audio and video. The reason so many UDP packets appear is because Google Meet sends 30–60 video frames per second, each as a separate packet. UDP is chosen over TCP because video calls prioritize speed over reliability — if a packet is lost, UDP simply drops it and moves on to the next frame, keeping the call smooth. TCP would instead pause and retransmit the lost packet, causing the call to freeze — which is far worse than a tiny glitch. This is why all major video platforms use UDP for their media streams.
