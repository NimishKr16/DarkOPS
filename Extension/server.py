from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/ff", methods=["POST"])
def process_url():
    data = request.get_json()
    url = data.get("url", "URL not found")
    result_message = f"URL: {url.upper()}\nURL length : {len(url)}"
    return jsonify({"message": result_message})


if __name__ == "__main__":
    app.run(debug=True, port=1100)
