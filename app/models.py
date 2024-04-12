from . import db

class Participant(db.Model):
    __tablename__ = 'picks'
    isbn = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    rd1_picks = db.Column(db.JSON)
    rd2_picks = db.Column(db.JSON)
    rd3_picks = db.Column(db.JSON)
    rd4_picks = db.Column(db.JSON)
    tie_breaker = db.Column(db.String(100), nullable=False)

    def to_json(self):
        return {
            'isbn': self.isbn,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'rd1_picks': self.rd1_picks,
            'rd2_picks': self.rd2_picks,
            'rd3_picks': self.rd3_picks,
            'rd4_picks': self.rd4_picks,
            'tie_breaker': self.tie_breaker
        }