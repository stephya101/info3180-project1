from . import db


class Property(db.Model):

    __tablename__ = 'property'

    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    property_title = db.Column(db.String(80))
    description= db.Column(db.String(255))
    no_of_rooms = db.Column(db.String(80))
    no_of_bthrooms = db.Column(db.String(80))
    price = db.Column(db.String(80))
    property_type = db.Column(db.String(80))
    photo = db.Column(db.String(80))
    location = db.Column(db.String(80))
    

    def __init__(self, property_title, description, no_of_rooms, no_of_bthrooms, price, property_type, photo, location):
        self.property_title = property_title
        self.description= description 
        self.no_of_rooms = no_of_rooms
        self.no_of_bthrooms = no_of_bthrooms
        self.price = price
        self. property_type = property_type
        self.photo = photo
        self.location = location   
         

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<Property %r>' % (self.property_title)


