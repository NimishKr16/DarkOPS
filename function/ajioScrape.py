import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urlparse

headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

# ------- Page: AJIO; Find all script tags to find Description,Availibity and Price ------ #
# ------- Page: AJIO doesnt have reviews or ratings. ------ #

def Ajio_get_tags(url):
    response = requests.get(url, headers=headers)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    script_tags = soup.find_all('script', type='application/ld+json')

    try:
        if script_tags:
            script_tag = script_tags[2]
            script_text = script_tag.text
            data = json.loads(script_text)
            price = data['offers']['price']
            brand_name = data['brand']['name']
            product_name = data['name']

            availability_url = data['offers']['availability']
            availability_status = urlparse(availability_url).path.split('/')[-1]

            ans_dict = {
                "Name":product_name,
                "Brand":brand_name,
                "Price": price,
                "Currency": data['offers']['priceCurrency'],
                "Availability":availability_status
            }

            return ans_dict
    except Exception as e:
       return("Hmm...Product Attributes not Found")
