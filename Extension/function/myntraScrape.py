import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
# url = input("Enter the URL: ")
url = "https://www.myntra.com/sweatshirts/h%26m/hm-relaxed-fit-drop-shoulder-sweatshirt/25293140/buy"


# Find all script tags to find Description,Availibity and Price
# Returns a dict of all these objects!
def get_tags(url):
    response = requests.get(url, headers=headers)
    # print(response)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    script_tags = soup.find_all("script", type="application/ld+json")

    if script_tags:
        script_tag = script_tags[1]

        json_data = json.loads(script_tag.contents[0])

        # Extract information from the JSON data
        description = json_data.get("description", "")
        availability = json_data.get("offers", {}).get("availability", "")
        price = json_data.get("offers", {}).get("price", "")

        product_dict = {
            "Description": description,
            "Availability": availability,
            "Price": price,
        }
        return product_dict
    else:
        print('No script tags with type "application/ld+json" found on the page.')


# dict = get_tags(url=url)
# print("PRODUCT DETAILS : ")
# for i in dict:
#     print(i, " : ", dict[i])


def get_reviews(url):
    response = requests.get(url, headers=headers)
    html_content = response.text

    start_index = html_content.find('"topReviews":')
    end_index = html_content.find('"topImageReviews"', start_index)
    json_like_string = "{" + html_content[start_index : end_index - 1] + "}"
    json_string = json_like_string
    data = json.loads(json_string)

    review_texts = []
    for review in data["topReviews"]:
        review_texts.append(review["reviewText"])

    review_dict = {"Reviews": review_texts}
    return review_dict


# reviews = get_reviews(url)
# print("\nREVIEWS : ")
# for i in range(len(reviews["Reviews"])):
#     print(f"{i+1}.{reviews['Reviews'][i]}\n")


# final_dict = {**get_tags(url=url), **get_reviews(url=url)}

# # for i in final_dict:
# #     print(i, "  :  ", final_dict[i])
# # df = pd.DataFrame(list(final_dict.items()))
# df = pd.DataFrame([final_dict])
# a = df.to_csv()
# print(a)


# Error code = 7, Path = /lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute, Message = There was an error during the transport or processing of this request., Unknown HTTP error in underlying XHR (HTTP Status: 0) (XHR Error Code: 6) (XHR Error Message: ' [0]')
