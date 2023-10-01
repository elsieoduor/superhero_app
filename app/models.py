from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

#Define Hero class as a model
class Hero(db.Model, SerializerMixin):
    #Set name of model
    __tablename__ = 'heroes'

    # Define serialization rules for this model
    serialize_rules = ('-hero_powers.hero')

    #Define columns for the heroes table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Create a relationship with the 'HeroPizza model, allowing access to related hero data
    hero_powers = db.relationship('HeroPizza', backref='hero')


    def __repr__(self):
        return f'<Hero {self.name}, Super name is {self.super_name}.'

#Define Power class as a model
class Power(db.Model, SerializerMixin):
    #Set name of model
    __tablename__ = 'powers'

    # Define serialization rules for this model
    serialize_rules = ('-hero_powers.power')

    #Define columns for the powers table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Create a relationship with the 'HeroPizza model, allowing access to related power data
    hero_powers = db.relationship('HeroPizza', backref='power')


    def __repr__(self):
        return f'<Power {self.name}, Super power is {self.description}.'

#Define HeroPower class as a model
class HeroPower(db.Model, SerializerMixin):
    #Set name of model
    __tablename__ = 'hero_powers'

    # Define serialization rules for this model
    serialize_rules = ('-hero.hero_powers', '-power.hero_powers')

    #Define columns for the hero_powers table
    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'))
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))


    def __repr__(self):
        return f'<Strength {self.strength}, Super name is {self.super_name}.'

