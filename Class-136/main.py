from flask import Flask, jsonify, request

from data import data

stuff = Flask(__name__)

# api to show the info about all the planets(entire data)
@stuff.route("/")

def stuff_data():
    return jsonify({
        "data" : data,
        "message" : "success"
    })


# api to show the info about a particular planet
@stuff.route("/planet")

def stuff_planet():
    name=request.args.get("name")
    #
    planet_data=next(i for i in data if i["name"] == name)
    
    return jsonify({
        "data" : planet_data,
        "message" : "success"
    })

if __name__ == "__main__":
    stuff.run()

#http://127.0.0.1:5000/
# http://127.0.0.1:5000/planet?name=11 Comae Berenices b

#  we are first fetching the name
# of the planet from the URL argument.
# We are then using the next() function
# to find a dictionary that satisfies the
# condition, which is, the value of name
# should match with the name we are
# providing!

# next() will help us to check all the data/planet's name kept in the data(variable) one after another