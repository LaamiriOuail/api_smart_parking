from database.database import db
# Car model
class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    matricule = db.Column(db.String(255), nullable=False)
    is_in_parking = db.Column(db.Boolean, default=False) #True : 1 , False : 0
    model = db.Column(db.String(255))
    
    # Foreign Key to Client
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)

    # One-to-One relationship with Abonement
    abonement = db.relationship('Abonement', backref='car', uselist=False, cascade='all, delete-orphan', lazy=True)
    