from flask import Flask, jsonify
from flask_cors import CORS
from database import db, DATABASE_URI

app = Flask(__name__)

CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.route("/")
def home():
    return jsonify({
        "message": "Shoe Platform API running"
    })


@app.route("/test")
def test():
    return jsonify({
        "status": "Database connected"
    })


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)