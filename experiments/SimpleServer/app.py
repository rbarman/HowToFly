from flask import Flask,jsonify
from random import randint, choice

app = Flask(__name__)

@app.route("/stats")
def get_stats():
	# random stats
    return jsonify(
        temperature=randint(50,100),
        coords=(randint(0,100),randint(0,100)),
        detected_landmark = choice(['person','building','tree','dog']),
        flight_duration=100,
    )

if __name__ == "__main__":
	# running on pi's ip address instead of localhost
    app.run(host= '0.0.0.0')