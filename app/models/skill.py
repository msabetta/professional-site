from app import db

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    level = db.Column(db.Integer)  # 1–5

    def __init__(self, id, name, level):
        self.name = name
        self.level = level
        self.id = id

    def __repr__(self):
        return '<Skill %r>' % self.name

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)

    def update(self):
        db.session.commit()
