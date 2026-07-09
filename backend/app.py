from flask import Flask, jsonify, request
from flask_cors import CORS

from database import db, DATABASE_URI
from models import Product, Order, Review

app = Flask(__name__)

CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


# ------------------------
# Home
# ------------------------

@app.route("/")
def home():
    return jsonify({
        "message": "Shoe Platform API is running"
    })


# ------------------------
# Products
# ------------------------

@app.route("/products", methods=["GET"])
def get_products():
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products])


@app.route("/products", methods=["POST"])
def add_product():
    data = request.json

    product = Product(
        name=data["name"],
        brand=data["brand"],
        category=data["category"],
        price=data["price"],
        stock=data["stock"],
        image=data["image"]
    )

    db.session.add(product)
    db.session.commit()

    return jsonify(product.to_dict()), 201


# ------------------------
# Orders
# ------------------------

@app.route("/orders", methods=["GET"])
def get_orders():
    orders = Order.query.all()
    return jsonify([order.to_dict() for order in orders])


@app.route("/orders", methods=["POST"])
def add_order():
    data = request.json

    order = Order(
        customer=data["customer"],
        phone=data["phone"],
        address=data["address"]
    )

    db.session.add(order)
    db.session.commit()

    return jsonify(order.to_dict()), 201


# ------------------------
# Reviews
# ------------------------

@app.route("/reviews", methods=["GET"])
def get_reviews():
    reviews = Review.query.all()
    return jsonify([review.to_dict() for review in reviews])


@app.route("/reviews", methods=["POST"])
def add_review():
    data = request.json

    review = Review(
        product_id=data["product_id"],
        username=data["username"],
        rating=data["rating"],
        fit=data["fit"],
        comment=data["comment"]
    )

    db.session.add(review)
    db.session.commit()

    return jsonify(review.to_dict()), 201


# ------------------------
# Create Database Tables
# ------------------------

with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)