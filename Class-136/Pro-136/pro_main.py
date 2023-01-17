from flask import Flask, jsonify, request

from pro_data import data

stuff = Flask(__name__)

@stuff.route("/")

def stuff_data():
    return jsonify({
        "data" : data,
        "message" : "success"
    })


# api to show the info about a particular planet
@stuff.route("/stars")

def stuff_planet():
    name=request.args.get("name")
   
    planet_data=next(i for i in data if i["name"] == name)
    
    return jsonify({
        "data" : planet_data,
        "message" : "success"
    })

if __name__ == "__main__":
    stuff.run()

#http://127.0.0.1:5000/