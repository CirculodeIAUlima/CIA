from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import random

# 1. Create a list of WhatsApp contacts
contacts = [
    "Juler",
    "Micali",
    "Javi"
]

# 2. Create a list of random messages
messages = [
    "Hola {name}!",
    "Si",
    "Miau"
]

# 3. Open Google and WhatsApp Web
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(5)

driver.get("https://www.google.com/")
driver.implicitly_wait(5)
driver.get("https://web.whatsapp.com/")
time.sleep(70)  # Wait for QR code scanning and session to load

# 4. Define a function to send messages
def send_messages():
    for contact in contacts:
        # Select a random message for each contact
        random_message = random.choice(messages)

        # Find the search box and enter the contact name
        search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true" and @data-tab="3" and @role="textbox" and @title="Cuadro de texto para ingresar la búsqueda"]')
        search_box.clear()
        search_box.send_keys(contact)
        search_box.send_keys(Keys.ENTER)  # Simulate pressing Enter to open the chat
        time.sleep(2)  # Allow time for the chat to open

        # Send the selected random message, formatted to include the contact name if needed
        formatted_message = random_message.format(name=contact) if '{name}' in random_message else random_message
        message_box = driver.switch_to.active_element  # Ensure focus is on the active message input
        message_box.send_keys(formatted_message)
        message_box.send_keys(Keys.ENTER)  # Simulate pressing Enter to send the message
        print(f"Message sent to {contact}: {formatted_message}")

# 5. Send messages
send_messages()

# Close the browser after sending messages
driver.quit()
