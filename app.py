from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, default=0)
    price = db.Column(db.Float, default=0.0)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([
        {'id': p.id, 'name': p.name, 'quantity': p.quantity, 'price': p.price}
        for p in products
    ])

@app.route('/api/products', methods=['POST'])
def add_product():
    data = request.get_json()
    product = Product(name=data['name'], quantity=data['quantity'], price=data['price'])
    db.session.add(product)
    db.session.commit()
    return jsonify({'message': 'Product added'}), 201




if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
