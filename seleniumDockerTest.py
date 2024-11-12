from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

print("Test Execution Started")
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')

# Start the Selenium WebDriver
driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    options=options
)

# Maximize the window size
driver.maximize_window()
time.sleep(10)
driver.get("http://host.docker.internal:8000")  # Access the local server
time.sleep(10)

try:
    # Wait for the "Get started free" link to be clickable
    link = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Get started"))
    )
    link.click()  # Click the link
    time.sleep(10)  # Wait for any resulting page to load

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "user_email_login"))
    )
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "user_password"))
    )

    # Enter login credentials
    username = driver.find_element(By.ID, "user_email_login")
    password = driver.find_element(By.ID, "user_password")
    login_button = driver.find_element(By.NAME, "commit")

    username.send_keys("ac@gmail.com")  # Replace with actual username
    password.send_keys("psword")  # Replace with actual password
    login_button.click()

    # Check for a post-login element (adjust to your page's unique element for logged-in users)
    try:
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "error-message"))
        )
        time.sleep(10)
        print("Login failed: Incorrect credentials")
    except:
        # No error message found, proceed with checking for dashboard
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "dashboard"))  # Replace with actual post-login element ID
        )
        print("Login Successful!")

except Exception as e:
    print(f"An error occurred while trying to click the link: {e}")

finally:
    # Ensure the browser quits after execution
    driver.quit()
    print("Test Execution Completed!")
