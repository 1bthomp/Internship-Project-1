from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from behave import given,when,then

# Get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()
# Set Chrome options for incognito mode
chrome_options = Options()
chrome_options.add_argument("--incognito")
# Create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()

@given('Open main page and login')
def main_page (context):

#Navigate to the URL
    driver.get("https://soft.reelly.io/sign-in")
    sleep(4)

# Search in user
    search_bar_1 = driver.find_element(By.ID, "email-2")
    search_bar_1.clear()
    search_bar_1.send_keys("Thompb155@gmail.com")
    sleep(4)

# Search password
    search_bar_2 = driver.find_element(By.ID, "field")
    search_bar_2.clear()
    search_bar_2.send_keys("@qqD9Kfkpymn5Fb")
    sleep(4)

# Click login
    driver.find_element(By.LINK_TEXT, 'Continue').click()
    sleep(4)

@when('click on settings, subscription and payment options')
def settings_subs_payment (context):

#Click settings (uncomment if needed)
    driver.find_element(By.LINK_TEXT, 'Settings').click()
    sleep(4)

@then('Verify subscription, back button, and upgrade plan')
def verification (context):

#Click subscription
    driver.find_element(By.CSS_SELECTOR, 'a[href="/subscription"]').click()
    sleep(4)

    check_1 = driver.find_element(By.XPATH, "//div[@class='lotion-your-h3--price size']").text
    check_2 = driver.find_element(By.XPATH, "//div[@class='back-text']").text
    check_3 = driver.find_element(By.XPATH, "//div[@class='next-step--']").text

    if check_1 == "Subscription & payments":
        print("1st check passed")
    else:
        print("not verified")

    if check_2 == "Back":
        print("2nd check passed")
    else:
        print("not verified")

    if check_3 == "Upgrade plan":
        print("3rd check passed")
    else:
        print("not verified")

driver.quit()