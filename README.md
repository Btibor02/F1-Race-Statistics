
# 🏎️ F1 Dashboard

**Explore race stats, lap times, and driver insights in real-time.**


## 🌐 Live Demo

👉 [Check out the live app](https://f1-race-statistics.onrender.com/)

---

## 📌 About the Project

**F1 Dashboard** is a sleek and responsive web application that showcases Formula 1 race statistics using real-time data from FastF1. Dive into lap times, driver comparisons, and performance analytics with interactive charts and a clean user interface.

---

## 🎯 Our Mission

To provide F1 fans with an engaging platform for real-time race analytics and data visualizations.

---

## ⚙️ Technology Stack

**Frontend**
- HTML
- CSS
- Bootstrap
- JavaScript
- Chart.js

**Backend**
- Python
- Flask
- FastF1

**Database**
- SQLite (via SQLAlchemy)

---

## 👥 Meet the Team

- **Daniel Marcarini** — Frontend Developer (HTML/CSS)  
- **Arda Dzhoshkun** — Frontend Developer (JavaScript/Charts)  
- **Hakan Ibryam** — Backend Developer (Flask & FastF1)  
- **Daniel Holderik** — Database & Documentation Specialist  
- **Tibor Blascsok** — User Authentication Engineer  

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- `pip`
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/Btibor02/f1-dashboard.git
cd f1-dashboard

# Install dependencies
pip install -r requirements.txt
```

### Run the Application

```bash
@echo off
echo --- Starting Flask app ---

echo Create a new database named f1_db
pause

REM Downloading required packages
pip install -r requirements.txt

REM Open backend folder
cd backend

REM Start Flask app
echo running run.py
python run.py
echo --- Flask app started ---
```

Alternatively:

```bash
cd backend
python run.py
```

---

## 📄 License

This project is licensed under the MIT License.
