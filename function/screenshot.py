import time
from selenium import webdriver
from PIL import Image
from PIL import ImageDraw
from io import BytesIO
import pytesseract



def capture_screenshot_with_message(url, message):
    driver = webdriver.Chrome()	

    driver.get(url)

    time.sleep(5)

    driver.execute_script("var element = document.createElement('div'); element.style.position = 'fixed'; element.style.top = '0'; element.style.left = '0'; element.style.background = 'white'; element.style.padding = '10px'; element.innerText = arguments[0]; document.body.appendChild(element);", message)

    time.sleep(2)

    screenshot = driver.get_screenshot_as_png()

    driver.quit()

    return screenshot

def extract_text_from_screenshot(screenshot):

    image = Image.open(BytesIO(screenshot))

    text = pytesseract.image_to_string(image)
    return text.strip()


def get_screenshot(url):
    message = "DO NOT CLOSE THIS PAGE"

    screenshot = capture_screenshot_with_message(url, message)
    image = Image.open(BytesIO(screenshot)).convert("RGB")
    image.save("screenshots/screenshot.jpg")
    text = extract_text_from_screenshot(screenshot)
    print(f'Detected text: {text}')

