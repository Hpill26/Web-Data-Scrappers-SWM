from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Replace these variables with your Twitter username and password
twitter_username = "gob33264@zslsz.com"
twitter_password = "Rohith@1234"

# Replace this URL with the Twitter search URL or user's profile URL
twitter_url = "https://twitter.com/home"

# Start the Selenium WebDriver (make sure to have the appropriate WebDriver installed)
driver = webdriver.Chrome(executable_path="C:\\Users\\Rohit Reddy\\Downloads\\chrome-win64\\chromedriver.exe")  # You may need to download and specify the path to your webdriver

# Open Twitter login page
driver.get("https://twitter.com/i/flow/login")
time.sleep(2)  # Let the page load

# Log in to Twitter
username_input = driver.find_element_by_css_selector(
    "input[autocomplete='username']"
)
username_input.send_keys(twitter_username)
username_input.send_keys(Keys.RETURN)
driver.implicitly_wait(10)
password_input = driver.find_element_by_css_selector(
    "input[autocomplete='current-password']"
)
password_input.send_keys(twitter_password)

password_input.send_keys(Keys.RETURN)

time.sleep(2)  # Allow time for the login to complete

# Open the Twitter page you want to scrape (e.g., a user's profile or a search page)
driver.get(twitter_url)
time.sleep(2)  # Let the page load

# Scroll down to load more tweets (you may need to adjust the number of scrolls)
for i in range(3):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

# Extract and print the tweets
tweet_elements = driver.find_elements_by_css_selector("div[data-testid='tweet']")
for tweet_element in tweet_elements:
    tweet_text = tweet_element.text
    print(tweet_text)

# Close the browser
driver.quit()
