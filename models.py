from server import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column('id', db.Integer, primary_key=True)
    login = db.Column('login', db.String)
    email = db.Column('email', db.String)
    password = db.Column('password', db.String)
    salt = db.Column('salt', db.String)
    permissions = db.Column('permissions', db.Integer)

    def __repr__(self):
       self.id = id
       self.login = login
       self.email = email
       self.password = password
       self.salt = salt
       selt.permissions = permissions
       return self.name



class Orders(db.Model):
    __tablename__ = 'orders'
    id_order = db.Column('id_order', db.Integer, primary_key=True)
    id_user = db.Column('id_user', db.Integer) # also foreign key
    date = db.Column('date', db.Date)
    input = db.Column('input', db.String)
    clusters = db.Column('clusters', db.Integer)
    grain = db.Column('grain', db.Integer)
    method = db.Column('method', db.Integer)
    status = db.Column('status', db.Integer)
    result = db.Column('result', db.String)
    time = db.Column('time', db.Float)

    def __repr__(self):
        self.id_order = id_order
        self.id_user = id_user
        self.date = date
        self.input = input
        self.clusters = clusters
        self.grain = grain
        self.method = method
        self.status = status
        self.result = result
        self.time = time
        return self.name
