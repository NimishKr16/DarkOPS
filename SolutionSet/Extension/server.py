from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json
import urllib.parse
import pandas as pd

# Importing custom functions
from function.myntraScrape import get_reviews, get_tags
from function.reviewCheck import aichecker
from function.screenshot import get_screenshot
from function.rflow import prediction


# App initiation
app = Flask(__name__)
CORS(app)


class IPQS:
    key = "GQNWfzROpleQ0AXMwIMZtLTobllWgc3V"

    def malicious_url_scanner_api(self, url: str, vars: dict = {}) -> dict:
        url = "https://www.ipqualityscore.com/api/json/url/%s/%s" % (
            self.key,
            urllib.parse.quote_plus(url),
        )
        x = requests.get(url, params=vars)
        print(x.text)
        return json.loads(x.text)


# ------------------------ Malicious Scanner Function ------------------------ #
@app.route("/scanweb", methods=["POST"])
def scan_threat():
    data = request.get_json()
    tabURL = data.get("url", "URL not found")
    ipqs = IPQS()
    result = ipqs.malicious_url_scanner_api(url=tabURL)
    score = result["risk_score"]

    if score >= 0 and score < 20:
        category = "Safe & Trusted"
    elif score > 20 and score < 40:
        category = "Low Risk"
    elif score > 40 and score < 60:
        category = "Moderately Risky"
    elif score > 60 and score < 80:
        category = "Highly Risky"
    elif score > 80 and score < 90:
        category = "Potentially Scam"
    elif score > 90 and score <= 100:
        category = "Highly Unsafe"
    else:
        category = "Uncategorized"
    # result_message = f"Risk Score : {str(result['risk_score'])}\n{category}"
    result_message = f"Website Category : {category}"
    print(result_message)
    return jsonify({"message": result_message})


# -------------------------- REVIEW SCANNER FUNCTION ------------------------- #
def scan_review(taburl, attributes, reviews):
    percentList = []
    for i in reviews["Reviews"]:
        fakePercent = aichecker(i)
        percentList.append(fakePercent)

    if len(percentList) != 0:
        finalPercent = sum(percentList) / len(percentList)

        if finalPercent < 20.0:
            msg = "Reviews are genuine"
        elif finalPercent > 20.0:
            msg = "Reviews might be fake"
        elif finalPercent > 50.0:
            msg = "Reviews are fake."
        # result_msg1 = f"Fake Reviews : {round(finalPercent, 2)}%\n{msg}"
        result_msg1 = f"{msg}"

    else:
        result_msg1 = ""
    print(result_msg1)
    return result_msg1


# -------------------------- CSV OPERATION FUNCTION -------------------------- #
def csv_operations(dict1, dict2, csvpath):
    final_dict = {**dict1, **dict2}
    required_keys = ["Description", "Availability", "Price", "Reviews"]
    if (
        all(key in final_dict for key in required_keys)
        and len(final_dict["Reviews"]) != 0
    ):
        df = pd.DataFrame([final_dict])
        try:
            file = pd.read_csv("test.csv")
            final_df = pd.concat([file, df], ignore_index=True)
        except FileNotFoundError:
            final_df = df
        final_df.to_csv(csvpath, index=False)
        result_msg2 = "All attributes found"
    else:
        result_msg2 = "Not all attributes are present"
    print(result_msg2)
    return result_msg2


# ----------------------- FINAL ATTRIBUTE SCAN FUNCTION ---------------------- #
@app.route("/scan", methods=["POST"])
def check_all():
    data = request.get_json()
    taburl = data.get("url", "URL not found")
    attributes = get_tags(taburl)
    reviews = get_reviews(taburl)
    csvpath = "./test.csv"

    reviews_scan = scan_review(taburl, attributes, reviews)
    csv_op = csv_operations(attributes, reviews, csvpath)

    return jsonify({"message1": reviews_scan, "message2": csv_op})


# -------------------------- GET UI ELEMENTS FUNCTION ------------------------- #

@app.route("/uiscan", methods=["POST"])
def uiscan():
    # Perform your UI scanning logic and get the image path
    data = request.get_json()
    taburl = data.get("url", "URL not found")
    get_screenshot(url = taburl)
    prediction()
    image_path = "prediction.jpg"

    # Return the image path in the response
    return jsonify({
        'message1': 'UI Scan successful',
        'message2': 'UI Elements found!',
        'imagePath': image_path
    })

# ------------------------------- MAIN FUNCTION ------------------------------ #
if __name__ == "__main__":
    app.run(debug=True, port=1100)
