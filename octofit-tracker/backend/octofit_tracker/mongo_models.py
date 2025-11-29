from mongoengine import Document, StringField, ReferenceField, IntField, DateField

class Team(Document):
    name = StringField(required=True, unique=True, max_length=100)
    meta = {'collection': 'teams'}

class User(Document):
    name = StringField(required=True, max_length=100)
    email = StringField(required=True, unique=True, max_length=100)
    team = ReferenceField(Team, required=True)
    meta = {'collection': 'users'}

class Activity(Document):
    user = ReferenceField(User, required=True)
    type = StringField(required=True, max_length=100)
    duration = IntField(required=True)
    date = DateField(required=True)
    meta = {'collection': 'activities'}

class Workout(Document):
    name = StringField(required=True, max_length=100)
    description = StringField()
    difficulty = StringField(max_length=50)
    meta = {'collection': 'workouts'}

class Leaderboard(Document):
    user = ReferenceField(User, required=True)
    score = IntField(required=True)
    meta = {'collection': 'leaderboard'}
