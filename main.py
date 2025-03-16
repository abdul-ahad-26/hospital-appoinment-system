import streamlit as st
import json
import os

APPOINTMENT_FILE = "appointments.json"

def load_appointments():
    if os.path.exists(APPOINTMENT_FILE):
        with open(APPOINTMENT_FILE, "r") as file:
            return json.load(file)
    return []

def save_appointments(appointments):
    with open(APPOINTMENT_FILE, "w") as file:
        json.dump(appointments, file, indent=4)

def book_appointment(patient_name, date, time):
    appointments = load_appointments()
    
    for appt in appointments:
        if appt["date"] == date and appt["time"] == time:
            return "❌ Slot not available. Choose another time."
    
    appointments.append({"patient_name": patient_name, "date": date, "time": time})
    save_appointments(appointments)
    return "✅ Appointment booked successfully."

def reschedule_appointment(patient_name, new_date, new_time):
    appointments = load_appointments()
    for appt in appointments:
        if appt["patient_name"] == patient_name:
            appt["date"], appt["time"] = new_date, new_time
            save_appointments(appointments)
            return "✅ Appointment rescheduled."
    return "❌ Appointment not found."

def cancel_appointment(patient_name):
    appointments = load_appointments()
    updated_appointments = [appt for appt in appointments if appt["patient_name"] != patient_name]
    save_appointments(updated_appointments)
    return "✅ Appointment canceled."

# Streamlit UI
st.title("🏥 Hospital Appointment System")

menu = ["Book Appointment", "Reschedule Appointment", "Cancel Appointment", "View Appointments"]
choice = st.sidebar.selectbox("Select an Option", menu)

if choice == "Book Appointment":
    st.subheader("📅 Book a New Appointment")
    patient_name = st.text_input("Enter Patient Name")
    date = st.date_input("Select Date")
    time = st.time_input("Select Time")
    
    if st.button("Book Appointment"):
        message = book_appointment(patient_name, str(date), str(time))
        st.success(message)

elif choice == "Reschedule Appointment":
    st.subheader("🔄 Reschedule an Appointment")
    patient_name = st.text_input("Enter Patient Name")
    new_date = st.date_input("Select New Date")
    new_time = st.time_input("Select New Time")
    
    if st.button("Reschedule Appointment"):
        message = reschedule_appointment(patient_name, str(new_date), str(new_time))
        st.success(message)

elif choice == "Cancel Appointment":
    st.subheader("❌ Cancel an Appointment")
    patient_name = st.text_input("Enter Patient Name")
    
    if st.button("Cancel Appointment"):
        message = cancel_appointment(patient_name)
        st.success(message)

elif choice == "View Appointments":
    st.subheader("📋 All Appointments")
    appointments = load_appointments()
    if appointments:
        st.table(appointments)
    else:
        st.info("No appointments found.")
