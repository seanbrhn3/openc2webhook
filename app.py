from flask import Flask, render_template, request, jsonify
import json
import os
import dialogflow

app = Flask(__name__)


@app.route('/')
def index():
    return "please talk"

@app.route('/webhook',methods=['GET','POST'])
def webhook():
    response = request.get_json(silent=True)
    reply = {
            "fulfillmentText": "sending response to actuator",
        }
    return  jsonify(reply)

@app.route("/acuator",methods=['GET','POST'])
def actuator():
    message = request.get_json()
    return jsonify("scanning device")

if __name__ == '__main__':
    app.run(host="0.0.0.0")
