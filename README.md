# 🏥 Hospital Appointment System

## 📌 Project Overview
The **Hospital Appointment System** is a simple web-based application built using **Python and Streamlit**. It allows doctors to **book, reschedule, cancel, and view appointments** efficiently. The system uses a **JSON file** for data storage instead of a database.

## 🚀 Features
✅ Book a new appointment  
✅ Reschedule an existing appointment  
✅ Cancel an appointment  
✅ View all appointments  

## 🛠️ Technologies Used
- **Python**: Main programming language
- **Streamlit**: Web UI framework
- **JSON**: Data storage format

## 📥 Installation & Setup
### **Prerequisites:**
- Install **Python 3.x**
- Install required dependencies:
  ```bash
  pip install streamlit
  ```

### **Running the App:**
- Save the code as `app.py`
- Open the terminal and run:
  ```bash
  streamlit run app.py
  ```
- The app will open in a browser

## 🔍 How the System Works
### **Booking an Appointment:**
1. Enter the **patient's name**
2. Select a **date** and **time**
3. Click **"Book Appointment"**
4. System confirms the booking

### **Rescheduling an Appointment:**
1. Enter the **patient's name**
2. Select a **new date** and **time**
3. Click **"Reschedule Appointment"**
4. System updates the appointment

### **Canceling an Appointment:**
1. Enter the **patient's name**
2. Click **"Cancel Appointment"**
3. System removes the appointment

### **Viewing Appointments:**
- Click **"View Appointments"**
- The system displays all booked appointments

## 📂 File Structure
```
📁 Hospital Appointment System  
 ├── 📄 app.py  # Main Streamlit app  
 ├── 📄 appointments.json  # Stores appointment data  
 ├── 📄 README.md  # Documentation  
```

## ✅ Test Cases & Expected Outputs
| Test Scenario                | Input | Expected Output |
|-----------------------------|-----------------|-----------------|
| Book a new appointment  | Name: John, Date: 2025-03-20, Time: 10:00 AM | "✅ Appointment booked successfully." |
| Book an already booked slot | Name: Jane, Date: 2025-03-20, Time: 10:00 AM | "❌ Slot not available. Choose another time." |
| Reschedule an appointment | Name: John, New Date: 2025-03-21, New Time: 11:00 AM | "✅ Appointment rescheduled." |
| Cancel an appointment | Name: John | "✅ Appointment canceled." |
| View all appointments | Click "View Appointments" | Table showing booked appointments |

## 🔮 Future Enhancements
- 🔹 Add **doctor availability** feature
- 🔹 Implement a **database (SQLite/PostgreSQL)** instead of JSON
- 🔹 Send **email reminders** for appointments

## 🎯 Conclusion
This **Hospital Appointment System** provides a simple way for doctors to **manage patient bookings**. It is built using **Python & Streamlit**, making it lightweight and easy to use. The system can be upgraded with additional features in the future.

---
Made with ❤️ using Python & Streamlit 🚀

