from app import db

# Hero Model
class Hero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    super_name = db.Column(db.String, nullable=False)
    hero_powers = db.relationship('HeroPower', backref='hero', lazy=True, cascade="all, delete-orphan")


# Power Model
class Power(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    hero_powers = db.relationship('HeroPower', backref='power', lazy=True, cascade="all, delete-orphan")

    # Ensure description is at least 20 characters long
    def validate_description(self):
        return len(self.description) >= 20


# HeroPower Model (Association Table)
class HeroPower(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('power.id'), nullable=False)
    strength = db.Column(db.String, nullable=False)

    # Ensure strength is one of the valid options
    def validate_strength(self):
        return self.strength in ['Strong', 'Weak', 'Average']
