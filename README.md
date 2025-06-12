# 🚀 Gurupadigm Form Filler

A Python automation script using **Selenium** to auto-fill Gurupadigm Google Forms with your saved Chrome profile.

## ✨ Features
- ✅ Auto-fills email checkbox, mentee name, date, register number, mentor name & department
- 📅 Sets today’s date automatically
- 👤 Uses your Chrome profile (no repeated logins)
- 🛑 Pauses before submission for manual review




## 🧰 Requirements
- Python 3.7+
- Google Chrome (installed)
- Signed-in Chrome profile
- Python libs:
  ```bash
  pip install selenium webdriver-manager

## ⚙️ Setup
```bash
git clone https://github.com/akashkrish1010/gurupadigm-form-filler.git
cd gurupadigm-form-filler
```
Edit script
```bash
person_data = {
    "mentee_name": "Your Name",
    "date": datetime.now().strftime("%d-%m-%Y"),
    "register_number": "Your Reg No",
    "mentor_name": "Mentor Name"
}
DEPARTMENT_NAME = "Mentor Dept"
```
## ▶️ Run Script
```bash
python guru_auto_form.py
```

## ⚠️ Notes
Chrome must be closed on first run

Script exits after manual confirmation

Chrome auto-closes if open during profile copy

## 👨‍💻 Author
Akash Krish
🔗 github.com/akashkrish1010

## 📄 License
MIT License


