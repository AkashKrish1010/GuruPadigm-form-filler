🚀 Gurupadigm Form Filler
A Python script that automates the process of filling out the Gurupadigm Google Form using Selenium and a persistent Chrome profile.
This project is especially useful for students or mentors who need to fill the same form regularly with minor changes.

📁 Directory Structure
css
Copy
Edit
akashkrish1010-gurupadigm-form-filler/
├── guru_auto_form.py     # Main automation script
🔧 Features
Auto-fills:

Email checkbox

Mentee name

Date (automatically set to today's date)

Register number

Mentor name

Mentor department (from a dropdown)

Uses your Chrome profile, so you stay signed in without needing to authenticate every time.

Designed to pause before submission, allowing manual confirmation and submission by the user.

🧰 Requirements
Python 3.7+

Google Chrome installed

Chrome profile already signed in once

The following Python libraries:

selenium

webdriver_manager

Install dependencies via pip:

bash
Copy
Edit
pip install selenium webdriver-manager
⚙️ Setup Instructions
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/akashkrish1010/gurupadigm-form-filler.git
cd gurupadigm-form-filler
2. Configure the Script
Edit guru_auto_form.py to update the following:

person_data: Fill in your personal information.

DEPARTMENT_NAME: The exact name of your mentor's department as listed in the form dropdown.

python
Copy
Edit
person_data = {
    "mentee_name": "Your Name",
    "date": datetime.now().strftime("%d-%m-%Y"),
    "register_number": "Your Register Number",
    "mentor_name": "Your Mentor's Name"
}
DEPARTMENT_NAME = "Your Mentor's Department"
3. Chrome Profile Setup (One-Time Only)
On first run, your existing Chrome profile will be copied and reused. Make sure Chrome is closed before running the script. This ensures you stay logged in.

Your default Chrome profile is assumed to be at:

python
Copy
Edit
original_profile = r"C:\Users\<Your-Username>\AppData\Local\Google\Chrome\User Data\Default"
▶️ How to Run
After setup:

bash
Copy
Edit
python guru_auto_form.py
Chrome will open automatically with your profile.

The form will be auto-filled.

You’ll be prompted to manually review and submit the form.

❗ Notes
Do not manually close Chrome during profile copy.

The script will terminate after you press Enter post-review.

If Chrome is running, it will be closed automatically to allow profile copy.

🧑‍💻 Author
Akash Krish
GitHub: akashkrish1010

📄 License
This project is open source and available under the MIT License.
