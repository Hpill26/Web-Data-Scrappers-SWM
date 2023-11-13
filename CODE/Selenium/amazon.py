from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

products = []

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")


driver = webdriver.Chrome(options=chrome_options)


driver.get("https://www.amazon.com/")


search_box = driver.find_element("id", "twotabsearchtextbox")
search_box.send_keys("electronics")
search_box.send_keys(Keys.RETURN)

time.sleep(5)


wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.s-result-item")))


search_results = driver.find_elements(By.CSS_SELECTOR, "div.s-result-item")

for result in search_results:
    
    title_elements = result.find_elements(By.CSS_SELECTOR, "span.a-size-medium.a-color-base.a-text-normal")
    product_title = title_elements[0].text.strip() if title_elements else "Title not available"

    try:
        price_element = result.find_element(By.CSS_SELECTOR, "span.a-price-whole")
        product_price = price_element.text.strip()
    except:
        product_price = "Price not available"

    try:
        rating_element = result.find_element(By.CSS_SELECTOR, "span.a-icon-alt")
        product_rating = rating_element.get_attribute("innerHTML").split()[0]
    except:
        product_rating = "Rating not available"

    # Extract number of reviews
    try:
        reviews_element = result.find_element(By.CSS_SELECTOR, "span.a-size-base")
        num_reviews = reviews_element.text.strip()
    except:
        num_reviews = "Reviews not available"

    # Extract product availability
    try:
        availability_element = result.find_element(By.CSS_SELECTOR, "div.a-row span.a-size-medium")
        product_availability = availability_element.text.strip()
    except:
        product_availability = "Availability not available"

    products.append({
        'Title': product_title,
        'Price': product_price,
        'Ratings': product_rating,
        'Number of Reviews': num_reviews,
    })
    # Print the extracted details
    # print("Title:", product_title)
    # print("Price:", product_price)
    # print("Rating:", product_rating)
    # print("Number of Reviews:", num_reviews)
    # print("Availability:", product_availability)
    # print("\n" + "=" * 50 + "\n")

    # Store the details in a CSV file
with open('amazon_products.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Title', 'Price', 'Ratings', 'Number of Reviews']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(products)

# Close the webdriver
driver.quit()