from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    subscriptionDate = db.Column(db.String(30))

    def __repr__(self):
        return '<User %r>' % self.username #Representa la tabla en forma de cadena

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "subscriptionDate": self.subscriptionDate,
            
            # do not serialize the password, its a security breach
        }
    
class Characters(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable = False)
    height = db.Column(db.Integer, nullable = False)
    mass = db.Column(db.Integer, nullable = False)
    hairColor = db.Column(db.String(20), nullable = False)
    skinColor = db.Column(db.String(20), nullable = False)
    eyeColor = db.Column(db.String(20), nullable = False)


    def __repr__(self):
        return f'<Characters {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hairColor": self.hairColor,
            "skinColor": self.skinColor,
            "eyeColor": self.eyeColor,
        }
    

class Planets(db.Model):
    __tablename__='planets'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    description = db.Column(db.String(200), nullable = False)
    population = db.Column(db.Integer, nullable = False)
    climate = db.Column(db.String(20), nullable = False)
    terrain = db.Column(db.String(20), nullable = False)
    orbitalPeriod = db.Column(db.Integer)

    def __repr__(self):
        return f'<Planets {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "orbitalPeriod": self.orbitalPeriod,
        }
    

class FavoriteCharacters(db.Model):
    __tablename__ = 'favoritecharacters'
    id = db.Column(db.Integer, primary_key= True)
    user_id = db.Column(db.Integer, nullable = False)
    character_id = db.Column(db.Integer, nullable = False)
    total = db.Column(db.Integer)

    def __repr__(self):
        return f'<FavoriteCharacters {self.id}>'
    
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id,
            "total": self.total,
        }
    
class FavoritePlanets(db.Model):
    __tablename__='favoriteplanets'
    id = db.Column(db.Integer, primary_key= True)
    user_id = db.Column(db.Integer, nullable=False)
    planet_id = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Integer)

    def __repr__(self):
        return f'<FavoritePlanets {self.id}'
    
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id,
            "total": self.total,
        }