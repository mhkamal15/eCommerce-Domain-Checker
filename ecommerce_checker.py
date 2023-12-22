import requests
from bs4 import BeautifulSoup

def check_ecommerce(domain):
    url = f"https://{domain}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an exception for non-200 status codes
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {domain}: {e}")
        return None

    soup = BeautifulSoup(response.content, "html.parser")

    # Check for a shopping cart on the webpage
    shopping_cart_elements = soup.find_all("div", class_="shopping-cart")  # Adjust class name as needed
    if shopping_cart_elements:
        return True

    # Check for other ecommerce indicators such as...
    # - Products listed on front page
    # - Checkout button present
    # - Payment gateways mentioned (e.g., PayPal, Stripe)

    return False

# Load domains from a file of choice
domains = []
with open("domains.txt", "r") as file:
    domains = file.read().splitlines()

# Check each domain and write results to a file
with open("ecommerce_domains.txt", "w") as file:
    for domain in domains:
        is_ecommerce = check_ecommerce(domain)
        if is_ecommerce is not None:  # Handle potential errors
            file.write(f"{domain}: {is_ecommerce}\n")
