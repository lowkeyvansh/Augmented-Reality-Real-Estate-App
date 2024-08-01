from flask import Flask, jsonify, request, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///real_estate.db'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
db = SQLAlchemy(app)

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_file = db.Column(db.String(100), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

db.create_all()

@app.route('/properties', methods=['GET'])
def get_properties():
    properties = Property.query.all()
    result = []
    for prop in properties:
        prop_data = {
            'id': prop.id,
            'title': prop.title,
            'description': prop.description,
            'price': prop.price,
            'image_file': url_for('static', filename='uploads/' + prop.image_file),
            'latitude': prop.latitude,
            'longitude': prop.longitude
        }
        result.append(prop_data)
    return jsonify(result)

@app.route('/properties', methods=['POST'])
def add_property():
    data = request.form
    image_file = request.files['image_file']
    
    if image_file:
        image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], image_file.filename))
        new_property = Property(
            title=data['title'],
            description=data['description'],
            price=data['price'],
            image_file=image_file.filename,
            latitude=data['latitude'],
            longitude=data['longitude']
        )
        db.session.add(new_property)
        db.session.commit()
        return jsonify({'message': 'Property added successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)
