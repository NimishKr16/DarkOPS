from flask import Flask, request, jsonify
from flask_cors import CORS
from aichecker import aichecker
from urlscanner import IPQS

app = Flask(__name__)
CORS(app)

strictness = 0

    # custom feilds
additional_params = {
        'strictness': strictness
    }

@app.route("/ff", methods=["POST"])
def process_url():
    data = request.get_json()
    check_URL = data.get("url", "URL not found")
    # result_message = f"URL: {url.upper()}\nURL length : {len(url)}"
    ipqs = IPQS()
    res = ipqs.malicious_url_scanner_api(url = check_URL)
    result_message = "Risk Score: " +  str(res['risk_score'])
    return jsonify({"message": result_message})   


if __name__ == "__main__":
    app.run(debug=True, port=1100)
