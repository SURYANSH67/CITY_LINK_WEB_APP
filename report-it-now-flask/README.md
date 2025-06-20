🚀 CityLink Connect

Civic Issue Reporting Portal

CityLink Connect is a web app that helps citizens easily report local civic problems (like potholes, broken lights, or garbage dumps) and allows officials to manage and fix them efficiently.

It has two sides:
	•	Public Portal: For people to report issues.
	•	Admin Dashboard: For government officials to track and resolve them.

⸻

🔗 Live Demo

[Add your live website link here if deployed]

⸻

🧩 Features Overview

✅ For the Public
	•	Clean, easy-to-use homepage.
	•	Step-by-step form to submit issues.
	•	Google Maps autocomplete for accurate addresses.
	•	Upload images as proof.
	•	Confirmation email with a unique ticket ID.
	•	Public status page to check updates on your complaint.

🔒 For Officials/Admins
	•	Secure login with role-based access (Admin vs Official).
	•	Admins see all complaints; officials see only assigned ones.
	•	Dashboard with charts and stats (via Chart.js).
	•	Search, sort, and filter complaints live with AJAX (no page reload!).
	•	Update status, write notes, and resolve issues.
	•	Citizens get email when their issue is marked resolved.

⸻

🛠️ Tech Stack

🔙 Backend
	•	Python + Flask
	•	MySQL + SQLAlchemy
	•	Flask Extensions: Flask-Login, Flask-WTF, Flask-Mail, Flask-Migrate

🎨 Frontend
	•	Jinja2 + Bootstrap 5
	•	Vanilla JavaScript
	•	Chart.js (for graphs)
	•	Google Maps API (for address input)

⸻

💻 How to Run Locally

Follow these simple steps:

1. Clone the Project
  --- git clone [your-repo-link]
  --- cd citylink-connect

2. Set Up Virtual Environment

  --- python3 -m venv venv
  --- source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Required Packages
  --- pip install -r requirements.txt

4. Set Up MySQL Database
	•	Make sure MySQL is running.
	•	Create a new database (e.g., citylink_db) and user with password.

5. Configure .env File

SECRET_KEY='your_secret_key'
SQLALCHEMY_DATABASE_URI='mysql+pymysql://username:password@localhost/citylink_db'

MAIL_SERVER='smtp.googlemail.com'
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME='your_email@gmail.com'
MAIL_PASSWORD='your_app_password'
MAIL_DEFAULT_SENDER='your_email@gmail.com'

GOOGLE_MAPS_API_KEY='your_google_maps_api_key'

6. Run Database Migrations
  --- export FLASK_APP=run.py  # On Windows: set FLASK_APP=run.py
  --- lask db upgrade

7. Create Admin User

  --- flask create-admin "Admin Name" "admin@example.com" "adminpassword"
8. Start the App

  --- python3 run.py


✅ That’s it!

You’re now ready to use CityLink Connect — a complete civic complaint platform.