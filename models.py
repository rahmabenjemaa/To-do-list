from app import db
class Todo(db.Model):
    __tablename__ = "todos"
    tid = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(50), unique=True, nullable=False)
    done = db.Column(db.Boolean)


