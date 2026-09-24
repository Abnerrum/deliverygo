from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(180), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False, default="customer")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    def set_password(self, password): self.password_hash = generate_password_hash(password)
    def check_password(self, password): return check_password_hash(self.password_hash, password)

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, default="")
    delivery_fee = db.Column(db.Float, default=0)
    minimum_order = db.Column(db.Float, default=0)
    is_open = db.Column(db.Boolean, default=True)
    owner = db.relationship("User", backref=db.backref("restaurants", lazy=True))

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurant.id"), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    restaurant = db.relationship("Restaurant", backref=db.backref("categories", lazy=True, cascade="all, delete-orphan"))

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurant.id"), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, default="")
    price = db.Column(db.Float, nullable=False)
    available = db.Column(db.Boolean, default=True)
    restaurant = db.relationship("Restaurant", backref=db.backref("products", lazy=True, cascade="all, delete-orphan"))
    category = db.relationship("Category", backref=db.backref("products", lazy=True))

class DriverProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), unique=True, nullable=False)
    vehicle_type = db.Column(db.String(50), default="Moto")
    vehicle_plate = db.Column(db.String(20), default="")
    is_online = db.Column(db.Boolean, default=True)
    user = db.relationship("User", backref=db.backref("driver_profile", uselist=False))

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurant.id"), nullable=False)
    driver_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)
    address = db.Column(db.String(255), nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)
    payment_status = db.Column(db.String(30), default="PAID_SIMULATED")
    status = db.Column(db.String(30), default="PENDING")
    subtotal = db.Column(db.Float, default=0)
    delivery_fee = db.Column(db.Float, default=0)
    total = db.Column(db.Float, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    customer = db.relationship("User", foreign_keys=[customer_id])
    driver = db.relationship("User", foreign_keys=[driver_id])
    restaurant = db.relationship("Restaurant")

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Float, nullable=False)
    observation = db.Column(db.String(255), default="")
    order = db.relationship("Order", backref=db.backref("items", lazy=True, cascade="all, delete-orphan"))
    product = db.relationship("Product")

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"), unique=True, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurant.id"), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, default="")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    order = db.relationship("Order", backref=db.backref("review", uselist=False))
    customer = db.relationship("User")
    restaurant = db.relationship("Restaurant", backref=db.backref("reviews", lazy=True))
