import time
from selenium import webdriver
from PIL import Image
from PIL import ImageDraw
from io import BytesIO
import pytesseract



def capture_screenshot_with_message(url, message):
    # Set up the web driver (assuming Chrome here)
    driver = webdriver.Chrome()	

    # Navigate to the Amazon product page
    driver.get(url)

    # Wait for some time for the page to load (you might need to adjust this)
    time.sleep(5)

    # Add a message at the top of the page
    driver.execute_script("var element = document.createElement('div'); element.style.position = 'fixed'; element.style.top = '0'; element.style.left = '0'; element.style.background = 'white'; element.style.padding = '10px'; element.innerText = arguments[0]; document.body.appendChild(element);", message)

    # Wait for the message to be added
    time.sleep(2)

    # Capture screenshot
    screenshot = driver.get_screenshot_as_png()

    # Close the browser window
    driver.quit()

    return screenshot

def extract_text_from_screenshot(screenshot):
    # Open the screenshot using PIL
    image = Image.open(BytesIO(screenshot))

    # Perform OCR
    text = pytesseract.image_to_string(image)
    return text.strip()

# Example usage with an Amazon product URL
def get_screenshot(url):
    message = "Hello world"
    # url = input("Enter a URL: ")
    screenshot = capture_screenshot_with_message(url, message)
    image = Image.open(BytesIO(screenshot)).convert("RGB")
    image.save("screenshots/screenshot.jpg")
    text = extract_text_from_screenshot(screenshot)
    print(f'Detected text: {text}')

# url = input("Enter a URL: ")
# get_screenshot(url=url)