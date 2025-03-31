from sqlalchemy.orm import validates

class HeroPower(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hero_id = db.Column(db.Integer, db.ForeignKey("hero.id"), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey("power.id"), nullable=False)
    strength = db.Column(db.String, nullable=False)

    @validates("strength")
    def validate_strength(self, key, value):
        if value not in ["Strong", "Weak", "Average"]:
            raise ValueError("Strength must be Strong, Weak, or Average")
        return value
