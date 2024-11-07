from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/get_data', methods=['GET'])
def get_data():
    # Example data to be sent to the frontend
    data = {
        'fname': 'John Doe',
        'headshot': 'image.png',  # URL/path to the image
        'teamname': 'Team Phoenix',
        'nameacro': 'J.D.',
        'drivernum': '42'
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
