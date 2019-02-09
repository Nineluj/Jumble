from flask import render_template, redirect, url_for, flash, request
from flask_restplus import fields, Api, Resource, marshal, marshal_with
import marshmallow
from app.api import bp
from app.api import api

user_model = api.model('User',
    {
        'id' : fields.Integer,
        'name' : fields.String,
        'email' : fields.String,
        'major' : fields.String,
        'slack' : fields.String,
    }
)

event_model = api.model('Event', 
    {
        'id' : fields.Integer,
        'name' : fields.String,
        'creator' : fields.Nested(user_model),
        'admins' : fields.List(fields.Nested(user_model)),
        'attendies' : fields.List(fields.Nested(user_model))
    }
)

interest_model = api.model('Interest', 
    {
        'id' : fields.Integer,
        'name' : fields.String
    }
)

skills_model = api.model('Skill',
    {
        'id' : fields.Integer,
        'name' : fields.String
    }
)

interests_model = api.model('Interests',
    {
        'user' : fields.Integer,
        'interests' : fields.List(fields.Nested(interest_model))
    }
)

skills_model = api.model('Skills', 
    {
        'user' : fields.Integer,
        'skills' : fields.List(fields.Nested(skills_model))
    }
)

contacts_model = api.model('Contacts',
    {
        'self' : fields.Integer,
        'contacts' : fields.List(fields.Nested(user_model))
    }
)


@api.route('/user/<user_id>')
class User(Resource):
    @api.marshal_with(user_model)
    def get(self, user_id):
        return {
        'id' : 0,
        'name' : 'The OG Git Booster',
        'email' : 'thatOGboost@boost.org',
        'major' : 'Boosting',
        'slack' : 'thatOGBooster',
        }

@api.route('/users')
class Users(Resource):
    @api.marshal_list_with(user_model)
    def get(self):
        return [
                {
            'id' : 0,
            'name' : 'The OG Git Booster',
            'email' : 'thatOGboost@boost.org',
            'major' : 'Boosting',
            'slack' : 'thatOGBooster',
            }
        ]

@api.route('/event/<event_id>')
class Event(Resource):
    @api.marshal_with(event_model)
    def get(self, event_id):
        return {
            'id' : '1',
            'name' : 'Hack Beanpot',
            'creator' : {
                            'id' : 0,
                            'name' : 'The OG Git Booster',
                            'email' : 'thatOGboost@boost.org',
                            'major' : 'Boosting',
                            'slack' : 'thatOGBooster',
                        },
            'admins' : [{
                            'id' : 0,
                            'name' : 'The OG Git Booster',
                            'email' : 'thatOGboost@boost.org',
                            'major' : 'Boosting',
                            'slack' : 'thatOGBooster',
                        }],
            'attendies' : [{
                            'id' : 0,
                            'name' : 'The OG Git Booster',
                            'email' : 'thatOGboost@boost.org',
                            'major' : 'Boosting',
                            'slack' : 'thatOGBooster',
                        }]
        }

@api.route('/events')
class Events(Resource):
    @api.marshal_list_with(event_model)
    def get(self):
        return [
                {
                'id' : '1',
                'name' : 'Hack Beanpot',
                'creator' : {
                                'id' : 0,
                                'name' : 'The OG Git Booster',
                                'email' : 'thatOGboost@boost.org',
                                'major' : 'Boosting',
                                'slack' : 'thatOGBooster',
                            },
                'admins' : [{
                                'id' : 0,
                                'name' : 'The OG Git Booster',
                                'email' : 'thatOGboost@boost.org',
                                'major' : 'Boosting',
                                'slack' : 'thatOGBooster',
                            }],
                'attendies' : [{
                                'id' : 0,
                                'name' : 'The OG Git Booster',
                                'email' : 'thatOGboost@boost.org',
                                'major' : 'Boosting',
                                'slack' : 'thatOGBooster',
                            }]
            }
        ]

