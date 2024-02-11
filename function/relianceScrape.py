import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urlparse

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}




# ------- Page: Reliance Digital; Find all script tags to find Description,Availibity and Price ------ #

def Reliance_get_tags(url):
    response = requests.get(url, headers=headers)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    script_tags = soup.find_all('script', type='application/ld+json')
    try:
        if script_tags:
            # script_tag = script_tags[2]
            script_text = script_tags[0].text
            data = json.loads(script_text)
            if "@type" in data and data["@type"] == "Product":
                price = data['offers']['price']
                name = data['name']
                rating_value = data.get('aggregateRating', {}).get('ratingValue', 'N/A')

                dict = {
                    "Description":name,
                    "Price":price,
                    "Rating":rating_value
                }
                return dict
    except Exception as e:
        return("Hmm...Product Attributes not Found")
    

# ------- Page: Reliance Digital; Find all Product Reviews ------ #

def Reliance_get_reviews(url):
    response = requests.get(url, headers=headers)
    print(response)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    revs = soup.find_all('div',id='reviews')
    reviews_container = soup.find('div', {'id': 'reviews'})
    try:
        if reviews_container:
            # Find all individual reviews
            reviews = reviews_container.find_all('div', {'class': 'SingleReview__ReviewText-sc-1knvtv4-0'})
            final_rev = []
            for review in reviews:
                myrev = review.get_text(strip=True)
                final_rev.append(myrev)
            newlist = [item for item in final_rev if item != '']
            if not newlist:
                return []
            else:
                return ({"Reviews":newlist})
    except Exception as e:
        return ("Hmm...Reviews not found")

