from database.database import db
# Abonement model
class Abonement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    create_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    sold = db.Column(db.Float)

    # Foreign Key to Car
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'), nullable=False)
    @classmethod
    def abonement_exists_by_id(cls, abonement_id):
        return cls.query.filter_by(id=abonement_id).first() is not None