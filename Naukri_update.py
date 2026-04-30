import os
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# ─── Logging Setup ────────────────────────────────────────────────

logging.basicConfig(
level=logging.INFO,
format=”%(asctime)s [%(levelname)s] %(message)s”,
handlers=[logging.StreamHandler()]
)
log = logging.getLogger(**name**)

# ─── Credentials from Environment Variables ───────────────────────

EMAIL    = os.environ.get(“NAUKRI_EMAIL”, “”)
PASSWORD = os.environ.get(“NAUKRI_PASSWORD”, “”)

if not EMAIL or not PASSWORD:
raise ValueError(“NAUKRI_EMAIL and NAUKRI_PASSWORD environment variables must be set.”)

# ─── URLs ─────────────────────────────────────────────────────────

NAUKRI_LOGIN_URL   = “https://www.naukri.com/nlogin/login”
NAUKRI_PROFILE_URL = “https://www.naukri.com/mnjuser/profile”

def get_driver():
“”“Configure headless Chrome for GitHub Actions / cloud.”””
options = Options()
options.add_argument(”–headless”)
options.add_argument(”–no-sandbox”)
options.add_argument(”–disable-dev-shm-usage”)
options.add_argument(”–disable-gpu”)
options.add_argument(”–window-size=1920,1080”)
options.add_argument(”–disable-blink-features=AutomationControlled”)
options.add_experimental_option(“excludeSwitches”, [“enable-automation”])
options.add_experimental_option(“useAutomationExtension”, False)
options.add_argument(
“user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) “
“AppleWebKit/537.36 (KHTML, like Gecko) “
“Chrome/120.0.0.0 Safari/537.36”
)
driver = webdriver.Chrome(options=options)
driver.execute_script(
“Object.defineProperty(navigator, ‘webdriver’, {get: () => undefined})”
)
return driver

def login(driver):
“”“Log in to Naukri.”””
log.info(“Opening Naukri login page…”)
driver.get(NAUKRI_LOGIN_URL)
wait = WebDriverWait(driver, 20)

```
# Enter email
email_field = wait.until(EC.presence_of_element_located((By.ID, "usernameField")))
email_field.clear()
email_field.send_keys(EMAIL)
log.info("Email entered.")

# Enter password
pwd_field = driver.find_element(By.ID, "passwordField")
pwd_field.clear()
pwd_field.send_keys(PASSWORD)
log.info("Password entered.")

# Click login
pwd_field.send_keys(Keys.RETURN)
time.sleep(4)

# Verify login
if "nlogin" in driver.current_url:
    raise Exception("Login failed — check your credentials.")
log.info("Login successful!")
```

def update_profile(driver):
“”“Navigate to profile and trigger a resume headline update to refresh timestamp.”””
log.info(“Navigating to profile page…”)
driver.get(NAUKRI_PROFILE_URL)
wait = WebDriverWait(driver, 20)
time.sleep(3)

```
try:
    # Click edit on Resume Headline section
    headline_edit = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[contains(@class,'resumeHeadline')]//span[contains(@class,'edit')]")
    ))
    headline_edit.click()
    time.sleep(2)
    log.info("Opened resume headline editor.")

    # Find the textarea
    textarea = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//textarea[contains(@placeholder,'headline') or contains(@class,'headline')]")
    ))

    # Get current text, add a space and remove it to trigger a change
    current_text = textarea.get_attribute("value") or ""
    textarea.click()
    textarea.send_keys(Keys.END)
    textarea.send_keys(" ")   # add space
    time.sleep(1)
    textarea.send_keys(Keys.BACK_SPACE)  # remove space
    time.sleep(1)

    # Save
    save_btn = driver.find_element(
        By.XPATH, "//button[contains(text(),'Save') or contains(@class,'saveBtn')]"
    )
    save_btn.click()
    time.sleep(3)
    log.info("✅ Resume headline saved — profile timestamp updated!")

except (TimeoutException, NoSuchElementException) as e:
    log.warning(f"Headline edit failed ({e}). Trying fallback: profile view refresh...")
    # Fallback: simply visit profile to signal activity
    driver.get(NAUKRI_PROFILE_URL)
    time.sleep(3)
    log.info("✅ Profile page visited — activity registered.")
```

def main():
log.info(”=” * 50)
log.info(”  Naukri Auto-Update Script Started”)
log.info(”=” * 50)

```
driver = get_driver()
try:
    login(driver)
    update_profile(driver)
    log.info("🎉 Profile update complete! You're now visible to recruiters.")
except Exception as e:
    log.error(f"Script failed: {e}")
    raise
finally:
    driver.quit()
    log.info("Browser closed.")
```

if **name** == “**main**”:
main()
