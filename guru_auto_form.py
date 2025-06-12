import os
import shutil
import subprocess
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

original_profile = r"C:\Users\PAAL-DABBA\AppData\Local\Google\Chrome\User Data\Default"
custom_profile_dir = r"C:\SeleniumProfiles\GuruProfile"
form_link = "https://forms.gle/YpFZoZEfc847ioWc6"

DEPARTMENT_NAME = "Mathematics for Excellence"

current_date = datetime.now().strftime("%d-%m-%Y")

person_data = {
    "mentee_name": "Akash S",
    "date": current_date,
    "register_number": "192321029",
    "mentor_name": "Dr.Sharmila mary arul"
}

def copy_chrome_profile():
    print("[STEP 1] Checking Chrome profile...")
    if os.path.exists(custom_profile_dir):
        print("[INFO] Custom profile already exists. Skipping copy.")
        return
    print("[STEP 2] Closing Chrome...")
    subprocess.call(["taskkill", "/F", "/IM", "chrome.exe"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(2)
    print("[STEP 3] Copying Chrome profile...")
    shutil.copytree(original_profile, custom_profile_dir)
    print("[DONE] Chrome profile copied. Please sign in manually the first time.\n")

def fill_form():
    print("[STEP 4] Launching Chrome with copied profile...")
    options = webdriver.ChromeOptions()
    options.add_argument(f"--user-data-dir={custom_profile_dir}")
    options.add_argument("--profile-directory=Default")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)

    browser.get(form_link)
    wait = WebDriverWait(browser, 20)

    try:
        print("[STEP 5] Waiting for form to load...")
        email_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@role="checkbox"]')))
        email_checkbox.click()
        print("[INFO] Email checkbox clicked.")

        print("[STEP 6] Filling text input fields...")
        text_inputs = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//input[@type="text"]')))
        date_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="date"]')))

        if len(text_inputs) < 3:
            raise Exception(f"[ERROR] Expected at least 3 text input fields, found {len(text_inputs)}")

        date_input.clear()
        date_input.send_keys(person_data["date"])
        print(f"[INFO] Date filled: {person_data['date']}")

        text_inputs[0].send_keys(person_data["mentee_name"])
        text_inputs[1].send_keys(person_data["register_number"])
        text_inputs[2].send_keys(person_data["mentor_name"])
        print("[INFO] Text inputs filled.")

        print("[STEP 7] Selecting department...")
        dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@role="listbox"]')))
        dropdown.click()
        time.sleep(1)

        dropdown_options = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, '//div[@role="option"]')))
        
        option_found = False
        for option in dropdown_options:
            if option.text.strip() == DEPARTMENT_NAME:
                option.click()
                option_found = True
                print(f"[INFO] Selected department: {DEPARTMENT_NAME}")
                break
        
        if not option_found:
            raise Exception(f"Department '{DEPARTMENT_NAME}' not found in dropdown options")

        print("\nAll fields filled. Please review and click 'Submit' manually.")
        input("Press Enter to close the browser...")
        
    except Exception as e:
        print(f"[ERROR] Something went wrong: {str(e)}")
        print("[DEBUG] URL:", browser.current_url)
        print("[DEBUG] Page Source (partial):", browser.page_source[:500])
        input("Press Enter to close the browser after error...")
    finally:
        browser.quit()
        print("[INFO] Browser closed.")

if __name__ == "__main__":
    copy_chrome_profile()
    fill_form()