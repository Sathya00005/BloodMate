# 🩸 Blood Bank Management System

A streamlined Blood Bank Management System built with **Python Flask**, enabling efficient **donor-recipient management**, **registration**, and **blood donation tracking** through a modern web interface.

---

## 🚀 Features

- Donor Registration with Eligibility Check  
- Recipient Registration and Donor Matching  
- Auto-generated Donation Certificate for Eligible Donors  
- View Registered Donors and Recipients  
- Donor Request Management  
- Secure Login & Signup System  
- Sidebar Navigation Dashboard  
- Clean and Responsive UI (HTML, CSS, Bootstrap)

---

## 🛠 Tech Stack

- **Backend:** Python, Flask  
- **Frontend:** HTML5, CSS3, Bootstrap  
- **Database:** SQLite  
- **Template Engine:** Jinja2

---

## 📁 Project Structure

BloodBankSystem/ │ ├── app.py ├── static/ │ ├── css/ │ │ └── style.css │ └── images/ │ └── certificate.png │ ├── templates/ │ ├── index.html │ ├── login.html │ ├── register.html │ ├── donor_registration.html │ ├── recipient_registration.html │ ├── view_donors.html │ ├── request_donor.html │ ├── certificate.html │ ├── database/ │ └── bloodbank.db (auto-created) │ └── README.md


#Clone the repository
https://github.com/Sathya00005/BloodMate.git
# Navigate into the project directory
cd BloodMate

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py

