from FilterAPI import db


class Data(db.Model):
    # create models here
    id = db.Column(db.Integer, primary_key=True)
