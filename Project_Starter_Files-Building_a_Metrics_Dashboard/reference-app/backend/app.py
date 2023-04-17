from flask import Flask, render_template, request, jsonify

import pymongo
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "example-mongodb"
app.config[
    "MONGO_URI"
] = "mongodb://example-mongodb-svc.default.svc.cluster.local:27017/example-mongodb"

mongo = PyMongo(app)


@app.route("/")
def homepage():
    return "Hello World"


@app.route("/api")
def my_api():
    answer = "something"
    return jsonify(repsonse=answer)


@app.route("/star", methods=["POST"])
def add_star():
    with opentracing.tracer.start_span(
        "star-endpoint",child_of=flask_tracer_span
    ) as span:
        try:
            
            star = mongo.db.stars
            name = request.json["name"]
            distance = request.json["distance"]
            star_id = star.insert({"name": name, "distance": distance})
            new_star = star.find_one({"_id": star_id})
            output = {"name": new_star["name"], "distance": new_star["distance"]}

            response = jasonify({"result" = output})
            span.set_tag("message",json.dumps(response))
            
            return response
        except:
            span.set_tag("response","Can not retrieve from Dashboard")


if __name__ == "__main__":
    app.run()


