# ✈️ Dynamic Flight Price Prediction System

Welcome to the **Dynamic Flight Price Prediction** project — a smart, responsive system that predicts flight ticket prices based on real-world dynamic factors like **date**, **demand**, **festivals**, **offers**, and **seat availability**.

## 🔍 Overview

Flight ticket prices vary constantly depending on multiple real-time factors. This project aims to replicate such a pricing mechanism using **Machine Learning** and custom **rule-based logic** to generate **realistic, dynamic predictions**.

### 💡 Key Features

- 📅 Predicts prices based on **date**, **month**, **weekend**, and **holiday seasons**.
- 🎉 Accounts for **festivals**, **special offers**, and **student discounts**.
- ✈️ Considers **seat availability**, **class type**, and **passenger preferences**.
- 📊 Integrates **ML model (pkl)** trained on flight data for intelligent predictions.
- 🖥️ Built using **Flask** with a clean and interactive **frontend**.
- 🧠 Includes business rules for fine-tuned price adjustments.

---

## 🧠 Prediction Logic

The final ticket price is determined using both the trained ML model and dynamic rules:

| Factor                     | Adjustment to Base Price |
|---------------------------|--------------------------|
| Festival Day              | + ₹2000                  |
| Weekend (Saturday/Sunday)| + ₹1000                  |
| Travel Class: Business    | + ₹3000                  |
| Seat Preference: Window   | + ₹500                   |
| Seat Preference: Middle   | + ₹200                   |
| Seat Preference: Aisle    | + ₹100                   |
| Passenger Type: Student   | Discounted               |
| Last Few Seats Left       | Surge Pricing            |

---

## 🚀 Tech Stack

- **Frontend**: HTML, CSS, Bootstrap  
- **Backend**: Python, Flask  
- **Machine Learning**: Scikit-learn, Pandas, Pickle  
- **Data**: Custom/generated dataset with flight records  

---

## 📂 Project Structure

Dynamic-Pricing/
│
├── backend/
│ ├── app.py # Main Flask app
│ ├── model.pkl # Trained ML model
│ ├── model_pred.pkl # (Optional) Secondary model
│ ├── templates/ # HTML templates (index, result, etc.)
│ └── static/ # Static images and styling
