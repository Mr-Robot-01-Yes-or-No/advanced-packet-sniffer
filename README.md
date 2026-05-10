# 🔥 Advanced Packet Sniffer using Scapy

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Scapy](https://img.shields.io/badge/Scapy-Network%20Analysis-red?style=for-the-badge)
![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Project-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

🚀 A real-time network packet sniffer built using **Python** and **Scapy** for live traffic analysis and protocol inspection.

</div>

---

# 📌 Overview

This project captures and analyzes live network packets in real time.

It can detect and monitor:

- 🌐 TCP Traffic
- 📡 UDP Traffic
- 📶 ICMP Packets
- 🔍 DNS Requests
- 🌍 HTTP Traffic

The sniffer displays:

✅ Source IP  
✅ Destination IP  
✅ Ports  
✅ Packet Length  
✅ TCP Flags  
✅ Protocol Statistics  
✅ Live Packet Logs  

---

# 🖥️ Preview

```text
[1] [14:22:11] TCP

SRC : 192.168.1.5:50422
DEST: 142.250.xx.xx:80
LEN : 52
INFO: Flags=S [SYN]
```

---

# ✨ Features

## 🚀 Core Features

- 🎯 Real-time packet capture
- 🎯 Live protocol detection
- 🎯 TCP / UDP / ICMP analysis
- 🎯 DNS packet detection
- 🎯 HTTP traffic monitoring
- 🎯 Packet statistics tracking
- 🎯 Colored terminal output
- 🎯 Packet logging system
- 🎯 Noise filtering

---

## 🛡️ Cybersecurity Features

- 🔥 TCP Flag Inspection
- 🔥 SYN Packet Detection
- 🔥 Traffic Monitoring
- 🔥 Real-Time Network Analysis

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| 🐍 Python | Core Programming |
| 📡 Scapy | Packet Capture & Analysis |
| 🎨 Colorama | Colored Terminal Output |

---

# 📂 Project Structure

```text
advanced-packet-sniffer/
│
├── sniffer.py
├── utils.py
├── requirements.txt
├── README.md
├── .gitignore
└── screenshots/
```

---

# ⚙️ Installation

## 📥 Clone Repository

```bash
git clone https://github.com/your-username/advanced-packet-sniffer.git
```

---

## 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Project

⚠️ Run terminal as **Administrator**

```bash
python sniffer.py
```

---

# 🧪 Generate Test Traffic

## 🌍 HTTP Traffic

Open:

```text
http://example.com
```

---

## 📡 ICMP Traffic

```bash
ping google.com
```

---

# 📊 Example Output

```text
[15] [18:32:41] DNS

SRC : 192.168.1.5:53122
DEST: 8.8.8.8:53
LEN : 74
INFO:
------------------------------------------------------------

[16] [18:32:44] TCP

SRC : 192.168.1.5:50422
DEST: 142.250.xx.xx:80
LEN : 52
INFO: Flags=S [SYN]
```

---

# 📈 Future Improvements

- 🖥️ GUI Dashboard
- 📊 Live Traffic Graphs
- 📁 PCAP Export
- 🚨 Intrusion Detection
- 🔍 Port Scan Detection
- 🌐 Web Monitoring Dashboard
- 🤖 AI-based Threat Detection

---

# 🎯 Learning Outcomes

This project helped in understanding:

- 🌐 Computer Networking
- 📡 Packet Analysis
- 🔐 Cybersecurity Basics
- 🛡️ Network Monitoring
- ⚡ TCP/IP Protocols

---

---

# 🤝 Contributing

Contributions are welcome!

If you'd like to improve this project:
- Fork the repository
- Create a new branch
- Submit a pull request

---

# ⭐ Support

If you liked this project:

⭐ Star the repository  
🍴 Fork the project  
📢 Share it with others  

---

# 👨‍💻 Author

## Ujas Gohil

💡 Beginner Cybersecurity & Networking Enthusiast

---

<div align="center">

🔥 Built with Python & Scapy 🔥

</div>
