from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import requests

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open Google Flights for Brazil
driver.get("https://www.google.com/flights?hl=pt-BR")

# Define a function to search for flights using Selenium and BeautifulSoup
def search_flights(departure, destination, departure_date, return_date):
    try:
        # Input departure location
        departure_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='De onde?']"))
        )
        departure_input.clear()
        departure_input.send_keys(departure)
        time.sleep(2)  # Add delay to let suggestions load
        departure_input.send_keys(Keys.ENTER)

        # Input destination location
        destination_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Para onde?']"))
        )
        destination_input.clear()
        destination_input.send_keys(destination)
        time.sleep(2)  # Add delay to let suggestions load
        destination_input.send_keys(Keys.ENTER)

        # Input departure date
        departure_date_input = driver.find_element(By.XPATH, "//input[@placeholder='Data de ida']")
        departure_date_input.click()
        departure_date_input.clear()
        departure_date_input.send_keys(departure_date)
        departure_date_input.send_keys(Keys.ENTER)

        # Input return date
        return_date_input = driver.find_element(By.XPATH, "//input[@placeholder='Data de volta']")
        return_date_input.click()
        return_date_input.clear()
        return_date_input.send_keys(return_date)
        return_date_input.send_keys(Keys.ENTER)

        # Click the search button
        search_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Pesquisar')]")
        search_button.click()

        # Wait for the results to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='gws-flights-results__result-list']"))
        )

        # Extract the page source and parse with BeautifulSoup
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')

        # Extract flight details
        flights = soup.find_all('div', class_='gws-flights-results__result-item')
        for flight in flights:
            # Extract specific details (example)
            airline = flight.find('div', class_='gws-flights__ellipsize').text
            times = flight.find_all('div', class_='gws-flights-results__times')
            departure_time = times[0].text if times else 'N/A'
            arrival_time = times[1].text if times else 'N/A'
            print(f"Airline: {airline}, Departure: {departure_time}, Arrival: {arrival_time}")

    except Exception as e:
        print("An error occurred:", e)

# Call the function with your search parameters
search_flights("São Paulo", "Rio de Janeiro", "2024-07-01", "2024-07-10")

# Close the driver
driver.quit()
