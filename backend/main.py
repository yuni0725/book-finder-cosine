from flask import Flask, request
from flask_cors import CORS
import pickle
from utils import match_data

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

db = []


@app.route("/send-data", methods=["POST"])
def send_data():
    book_name = request.data.decode("utf-8")

    return match_data(book_name)


@app.route("/send-book-data", methods=["GET"])
def send_book_data():
    return "sald"


if __name__ == "__main__":
    app.run(port="8000", debug=True)
