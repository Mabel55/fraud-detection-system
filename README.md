# 🔒 SecureBank AI - Advanced Fraud Detection System

**SecureBank AI** is a Full-Stack Financial Security Application designed to detect and prevent banking fraud in real-time. It combines **Machine Learning**, **Biometric Security**, and **Rule-Based Logic** to identify suspicious patterns and protect user funds.

## 🚀 Key Features

### 🧠 1. AI-Powered Analysis
* Uses a **Machine Learning Model (Scikit-Learn)** to analyze transaction patterns.
* Detects anomalies based on **Amount, Location, Time, and Account Type**.

### 🛡️ 2. Scam & Anomaly Prevention
* **"Reversal Scam" Detector:** Specifically engineered to block fake "Chargeback/Refund" requests (a common banking fraud in Nigeria).
* **Global Blacklist Check:** Instantly blocks known high-risk locations.

### 🔐 3. Enterprise Security
* **Biometric Login Simulation:** Features a futuristic "Fingerprint Laser" animation for secure access.
* **Admin Dashboard:** A restricted manager area to view the live **Blacklist Database** of blocked transactions.
* **Emergency Recovery:** Master PIN system for password recovery.

### 🔊 4. Audio-Visual Alerts
* **Real-time Feedback:** Plays a "Ding" 🛎️ for safe transactions and a **"Police Siren" 🚨** for detected fraud.
* **Professional UX:** Includes realistic server connection animations ("Connecting to CBN Database...").

---

## 🛠️ Tech Stack
* **Backend:** Python (Flask)
* **AI Engine:** Scikit-Learn (Pandas, Decision Trees)
* **Frontend:** HTML5, CSS3, JavaScript
* **Database:** CSV Logging System (Lightweight storage)

---

## 📸 How It Works
1.  **Manager Login:** The admin logs in using the secure biometric terminal.
2.  **Transaction Entry:** The admin enters details of a transfer (Amount, Location, Type).
3.  **The Analysis:**
    * The app first checks for **Hard Rules** (e.g., Reversal Scams).
    * If the rule passes, the **AI Model** predicts the probability of fraud.
4.  **The Verdict:** The system displays a **SAFE** or **FRAUD** alert with accompanying audio cues.

---

## 💻 Installation
1.  Clone the repository:
    ```bash
    git clone [https://github.com/YourUsername/fraud-detection-system.git](https://github.com/YourUsername/fraud-detection-system.git)
    ```
2.  Install dependencies:
    ```bash
    pip install flask pandas scikit-learn
    ```
3.  Run the application:
    ```bash
    python app.py
    ```

---
*Built by Mabel. Designed for the Future of Fintech.*