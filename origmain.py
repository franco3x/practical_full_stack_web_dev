import os
import requests
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from flask_cors import CORS
from mongo_client import mongo_client
import logging # new import

logging.basicConfig(level=logging.DEBUG) # new line

gallery = mongo_client.gallery
images_collection = gallery.images

load_dotenv(dotenv_path="./.env.local")

UNSPLASH_URL = 'https://api.unsplash.com/photos/random/'
UNSPLASH_KEY = os.environ.get("UNSPLASH_KEY", "")
DEBUG = bool(os.environ.get("DEBUG", True))

if not UNSPLASH_KEY:
    raise EnvironmentError("UNSPLASH_KEY is not set in .env.local file")

app = Flask(__name__)
db = mongo_client["images_gallery"] # new line
images_collection = db["images"] # new line

CORS(app)

app.config["DEBUG"] = DEBUG

@app.route("/new-image")
def new_image():
    word = request.args.get("query")
    headers = {
        "Accept-Version": "v1",
        "Authorization": "Client-ID " + UNSPLASH_KEY
    }
    params = {"query": word}

    response = requests.get(url=UNSPLASH_URL, params=params, headers=headers)
    
    data =response.json()
    return data

@app.route("/images", methods=["GET", "POST"])
def images():
    if request.method == "GET":
        # read images from the database
        images = images_collection.find({})
        return jsonify([img for img in images])

    if request.method == "POST":
        # save image in the database
        image = request.get_json()
        image["_id"] = image.get("id")
        result = images_collection.insert_one(image)
        inserted_id = result.inserted_id
        return {"inserted_id": inserted_id}
        

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
