from app import db


class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(100))
    company = db.Column(db.String(100))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    description = db.Column(db.Text)

    def __repr__(self):
        return '<User %r>' % self.requester_id

    def __init__(self,id, role, company, start_date, end_date, description):
        self.id = id
        self.role = role
        self.company = company
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
