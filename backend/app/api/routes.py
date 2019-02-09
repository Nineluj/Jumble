from flask import render_template, redirect, url_for, flash, request
from flask_restplus import fields, Api, Resource, marshal, marshal_with
import marshmallow
from app.api import bp
from app.api import api
import pymysql.cursors

def getConnection():
    return pymysql.connect(
            host='localhost',
            user='root',
            password='gitboost0208',
            db='jumble',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

user_model = api.model('User',
    {
        'id' : fields.Integer,
        'name' : fields.String,
        'email' : fields.String,
        'major' : fields.String,
        'slack' : fields.String,
    }
)

user_model_post = api.model('User', 
    {
        'name' : fields.String,
        'email' : fields.String,
        'major' : fields.String,
        'slack' : fields.String
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
        'user' : fields.Nested(user_model),
        'interests' : fields.List(fields.Nested(interest_model))
    }
)

skills_model = api.model('Skills', 
    {
        'user' : fields.Nested(user_model),
        'skills' : fields.List(fields.Nested(skills_model))
    }
)

liked_model = api.model('Likes', 
    {
        'user' : fields.Nested(user_model),
        'likes' : fields.List(fields.Nested(user_model))
    }
)

contacts_model = api.model('Contacts',
    {
        'self' : fields.Integer,
        'contacts' : fields.List(fields.Nested(user_model))
    }
)

# Wipes the database for development
@api.route('/wipe')
class Wipe(Resource):
    def get(self):
        cnxn = pymysql.connect(
            host='localhost',
            user='root',
            password='gitboost0208',
            db='jumble',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        with cnxn.cursor() as crsr:
            sql = """
            CREATE TABLE IF NOT EXISTS JUser (
            JUserID int AUTO_INCREMENT NOT NULL PRIMARY KEY
            );
            """
            crsr.execute(sql)
            cnxn.commit()
            return {'message' : 'Successfully nuked database.'}


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

    @api.expect(user_model)
    def put(self, user_id):
        # Edit the entry in the db. Return 201 if success
        return {'message' : 'Successfully update user!'}, 201

    def delete(self, user_id):
        # Delete the user.
        return {'message' : 'Successfully deleted the user!'}, 201

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
    
    @api.expect(user_model_post)
    def post(self):
        # Add this to the db. If success, return 201.
        return {'message' : 'Successfully insert into DB!'}, 201

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

