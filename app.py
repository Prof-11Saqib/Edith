from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/')
def hello():
    return "This app is now running 1" # To make sure that this app is running
@app.route('/get_data', methods=['GET']) # an open reponse gate for this app -- Needs to be replaced with the correct function in future.
def get_data():
    # Example data to be sent to the frontend
    data = {
    "broadcast_name": "M VERSTAPPEN",
    "country_code": "NED",
    "driver_number": 1,
    "first_name": "Max",
    "full_name": "Max VERSTAPPEN",
    "headshot_url": "https://www.formula1.com/content/dam/fom-website/drivers/M/MAXVER01_Max_Verstappen/maxver01.png.transform/1col/image.png",
    "last_name": "Verstappen",
    "meeting_key": 1219,
    "name_acronym": "VER",
    "session_key": 9158,
    "team_colour": "3671C6",
    "team_name": "Red Bull Racing"

    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
