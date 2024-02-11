import requests
from pprint import pprint


def aichecker(mytext):
    response = requests.post(
        "https://api.sapling.ai/api/v1/aidetect",
        json={"key": "SAJGY5I71UADG2WE5DR42Z6W7W1TU320", "text": mytext},
    )
    response_Dict = response.json()
    print(response_Dict)
    score = response_Dict["score"]

    return round(score * 100, 2)

