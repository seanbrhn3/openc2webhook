from flask import Flask, render_template, request, jsonify
import json
import os
import dialogflow

app = Flask(__name__)

"""
{"headers": {"Accept-Encoding": "identity", "Content-Length": "52", "Content-Type": "application/openc2-cmd+json;version=1.0", "X-Request-Id": "54578d1f-05e4-4b0e-b5f0-63161bfdd4a1", "Date": "Sun, 21 Jun 2020 19:52:04 GMT", "From": "8c508e30-1a97-4223-bf82-a3db3bfe0905@127.0.0.1:5000", "Host": "openc2_language_objects@52.186.141.94:5001"}, "content": {"target": {"artifact": {"mime_type": "rwerwerwe"}}}}
"""

app.route('/')
def index():
    return "please talk"

app.route('/webhook',methods=['GET','POST'])
def webhook():
    response = request.get_json(silent=True)
    reply = {
            "fulfillmentText": "sending response to actuator",
        }
    return  jsonify(reply)

app.route("/acuator",methods=['GET','POST'])
def actuator():
    message = request.get_json()
    return jsonify("scanning device")

if __name__ == '__main__':
    app.run(host="0.0.0.0")
