from bs4 import BeautifulSoup
import requests

# Function to extract Product Title
def get_title(soup):
    try:
        title = soup.find("span", attrs={"id": 'productTitle'})
        title_value = title.string
        title_string = title_value.strip()
    except AttributeError:
        title_string = ""
    return title_string

# Function to extract Product Price
def get_price(soup):
    try:
        price = soup.find("span", attrs={'id': 'priceblock_ourprice'}).string.strip()
    except AttributeError:
        price = ""
    return price

# Function to extract Product Rating
def get_rating(soup):
    try:
        rating = soup.find("i", attrs={'class': 'a-icon a-icon-star a-star-4-5'}).string.strip()
    except AttributeError:
        try:
            rating = soup.find("span", attrs={'class': 'a-icon-alt'}).string.strip()
        except:
            rating = ""
    return rating

# Function to extract Number of User Reviews
def get_review_count(soup):
    try:
        review_count = soup.find("span", attrs={'id': 'acrCustomerReviewText'}).string.strip()
    except AttributeError:
        review_count = ""
    return review_count

# Function to extract Availability Status
def get_availability(soup):
    try:
        available = soup.find("div", attrs={'id': 'availability'})
        available = available.find("span").string.strip()
    except AttributeError:
        available = ""
    return available

# List of Amazon product URLs
product_urls = [
    "https://www.amazon.com/Sony-PlayStation-Pro-1TB-Console-4/dp/B07K14XKZH/",
    "https://www.amazon.com/Xbox-X/dp/B08H75RTZ8/ref=sr_1_1_sspa?crid=17A09AFCHYJ02&keywords=xbox&qid=1698911886&s=videogames&sprefix=xbox%2Cvideogames%2C230&sr=1-1-spons&ufe=app_do%3Aamzn1.fos.c3015c4a-46bb-44b9-81a4-dc28e6d374b3&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1",
    # Add more product URLs here
]

# List to store product information
products = []

if __name__ == '__main__':
    # Headers for request
    HEADERS = ({
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
        'Accept-Language': 'en-US, en;q=0.5'
    })

    for URL in product_urls:
        # HTTP Request
        webpage = requests.get(URL, headers=HEADERS)

        # Soup Object containing all data
        soup = BeautifulSoup(webpage.text, "html.parser")

        # Extract product information
        product_info = {
            "Title": get_title(soup),
            "Price": get_price(soup),
            "Rating": get_rating(soup),
            "Review Count": get_review_count(soup),
            "Availability": get_availability(soup)
        }

        products.append(product_info)

# Print the list of product information
for product in products:
    print("Product Title =", product["Title"])
    print("Product Price =", product["Price"])
    print("Product Rating =", product["Rating"])
    print("Number of Product Reviews =", product["Review Count"])
    print("Availability =", product["Availability"])
    print()
    print()
