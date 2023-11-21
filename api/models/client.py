from database.database import db

# Client model
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=False, nullable=False)
    phone_number = db.Column(db.String(255), nullable=False)
    cin = db.Column(db.String(255), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    create_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    # One-to-Many relationship with Car
    cars = db.relationship('Car', backref='client', lazy=True)
    @classmethod
    def client_exists_by_id(cls, client_id):
        return cls.query.filter_by(id=client_id).first() is not None