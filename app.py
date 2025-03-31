from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

# Database Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///superheroes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize DB and Migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import models
from models import Hero, Power, HeroPower


# Routes
@app.route("/heroes", methods=["GET"])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([{
        "id": h.id, "name": h.name, "super_name": h.super_name
    } for h in heroes])


@app.route("/heroes/<int:id>", methods=["GET"])
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404
    return jsonify({
        "id": hero.id,
        "name": hero.name,
        "super_name": hero.super_name,
        "hero_powers": [{
            "id": hp.id,
            "strength": hp.strength,
            "power": {
                "id": hp.power.id,
                "name": hp.power.name,
                "description": hp.power.description
            }
        } for hp in hero.hero_powers]
    })


@app.route("/powers", methods=["GET"])
def get_powers():
    powers = Power.query.all()
    return jsonify([{
        "id": p.id, "name": p.name, "description": p.description
    } for p in powers])


@app.route("/powers/<int:id>", methods=["GET"])
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    return jsonify({
        "id": power.id, "name": power.name, "description": power.description
    })


@app.route("/powers/<int:id>", methods=["PATCH"])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    
    data = request.get_json()
    if "description" not in data or not data["description"]:
        return jsonify({"errors": ["Invalid description"]}), 400
    if len(data["description"]) < 20:
        return jsonify({"errors": ["Description must be at least 20 characters"]}), 400

    power.description = data["description"]
    db.session.commit()
    
    return jsonify({
        "id": power.id,
        "name": power.name,
        "description": power.description
    })


@app.route("/hero_powers", methods=["POST"])
def create_hero_power():
    data = request.get_json()
    if not data or "hero_id" not in data or "power_id" not in data or "strength" not in data:
        return jsonify({"errors": ["Missing hero_id, power_id, or strength"]}), 400
    
    hero = Hero.query.get(data["hero_id"])
    power = Power.query.get(data["power_id"])
    
    if not hero or not power:
        return jsonify({"errors": ["Hero or Power not found"]}), 404

    hero_power = HeroPower(hero_id=hero.id, power_id=power.id, strength=data["strength"])

    if not hero_power.validate_strength():
        return jsonify({"errors": ["Strength must be one of 'Strong', 'Weak', or 'Average'"]}), 400
    
    db.session.add(hero_power)
    db.session.commit()
    
    return jsonify({
        "id": hero_power.id,
        "strength": hero_power.strength,
        "hero": {
            "id": hero.id, "name": hero.name, "super_name": hero.super_name
        },
        "power": {
            "id": power.id, "name": power.name, "description": power.description
        }
    })

