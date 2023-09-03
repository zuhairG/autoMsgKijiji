import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException

# Set up Chrome options with user data directory, replace with applicable path
options = Options()
options.add_argument("user-data-dir=C:\\Users\\USER\\AppData\\Local\\Google\\Chrome\\User Data")

# Initialize the driver
driver = webdriver.Chrome(options=options)

# Go to the website
driver.get("https://www.kijiji.ca")

# Find the search bar and type a search term
search_bar = driver.find_element(By.ID, "SearchKeyword")
search_bar.send_keys("concrete")
search_bar.send_keys(Keys.RETURN)

# Wait for the results page to load
time.sleep(5)

# Get the listings
listings = driver.find_elements(By.CSS_SELECTOR, "li[data-testid^='listing-card-list-item-']")
total_listings = len(listings)

print(f"Total listings: {total_listings}")

# Iterate through listings
for i in range(total_listings):
    print(f"Clicked on listing {i}")

    # Open listing in new tab
    listing = listings[i]
    action = ActionChains(driver)
    action.key_down(Keys.CONTROL).click(listing).key_up(Keys.CONTROL).perform()

    # Switch to new tab
    new_window = driver.window_handles[-1]
    driver.switch_to.window(new_window)
    time.sleep(5)

    # Find message box and send
    try:
        message_box = driver.find_element(By.ID, "message")
        message_box.clear()
        message_box.send_keys("Hello! In need of machinery for your project? We've got you covered with a fleet of 2023 Bobcat MT100 available for rent at $200/day. Reach out at 2262222210 to book yours!")
        send_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Send message')]")
        send_btn.click()
        time.sleep(5)
    except: NoSuchElementException
       

    # Close tab
    driver.close()

    # Switch back to main window
    driver.switch_to.window(driver.window_handles[0])

# Close the browser
driver.quit()
