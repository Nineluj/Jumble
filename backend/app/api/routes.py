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
        cnxn = getConnection()
        try:
            with cnxn.cursor() as crsr:
                sql = ["DROP DATABASE IF EXISTS jumble;",
                "CREATE DATABASE jumble;",
                "USE jumble;",
                """
                CREATE TABLE IF NOT EXISTS Major (
                MajorID int AUTO_INCREMENT NOT NULL PRIMARY KEY,
                Name text);
                """,
                """
                CREATE TABLE IF NOT EXISTS JUser (
                JUserID int AUTO_INCREMENT NOT NULL PRIMARY KEY,
                Image blob,
                Name text,
                Email text,
                Slack text);
                """,
                """
                CREATE TABLE IF NOT EXISTS MajorJUser (
                MajorID int,
                JUserID int,
                FOREIGN KEY majorjuser_major_fk(MajorID)
                REFERENCES Major(MajorID),
                FOREIGN KEY majorjuser_user_fk(JUserID)
                REFERENCES JUser(JUserID),
                PRIMARY KEY (MajorID, JUserID));
                """,
                """
                CREATE TABLE IF NOT EXISTS Interest (
                InterestID int AUTO_INCREMENT NOT NULL PRIMARY KEY,
                Name text);
                """,
                """
                CREATE TABLE IF NOT EXISTS Idea (
                IdeaID int AUTO_INCREMENT NOT NULL PRIMARY KEY,
                Name text);
                """,
                """
                CREATE TABLE IF NOT EXISTS Skill (
                SkillID int AUTO_INCREMENT NOT NULL PRIMARY KEY,
                Name text);
                """,
                """
                CREATE TABLE IF NOT EXISTS JUserInterests (
                JUserID int,
                InterestID int,
                FOREIGN KEY juserinterests_juser_fk(InterestID)
                REFERENCES Interest(InterestID),
                FOREIGN KEY juserinterests_interest_fk(JUserID)
                REFERENCES JUser(JUserID),
                PRIMARY KEY (JUserID, InterestID));
                """,
                """
                CREATE TABLE IF NOT EXISTS JUserIdeas (
                JUserID int,
                IdeaID int,
                FOREIGN KEY juserideas_juser_fk(IdeaID)
                REFERENCES Idea(IdeaID),
                FOREIGN KEY juserideas_idea_fk(JUserID)
                REFERENCES JUser(JUserID),
                PRIMARY KEY (JUserID, IdeaID));
                """,
                """
                CREATE TABLE IF NOT EXISTS JUserSkill (
                JUserID int,
                SkillID int,
                FOREIGN KEY juserskill_juser_fk(JUserID)
                REFERENCES JUser(JUserID),
                FOREIGN KEY juserskill_skii_fk(SkillID)
                REFERENCES Skill(SkillID),
                PRIMARY KEY (JUserID, SkillID));
                """,
                """
                CREATE TABLE IF NOT EXISTS Contact (
                PrimaryJUserID int PRIMARY KEY,
                ContactID int,
                FOREIGN KEY contact_primary_fk(PrimaryJUserID)
                REFERENCES JUser(JUserID),
                FOREIGN KEY contact_contact_fk(ContactID)
                REFERENCES JUser(JUserID));
                """,
                """
                CREATE TABLE IF NOT EXISTS Event (
                EventID int AUTO_INCREMENT NOT NULL PRIMARY KEY,
                AdminID int,
                EName text,
                FOREIGN KEY event_admin_fk(AdminID)
                REFERENCES JUser(JUserID));
                """,
                """
                CREATE TABLE IF NOT EXISTS JUserEvent (
                JUserID int,
                EventID int,
                FOREIGN KEY juserevent_juser_fk(JUserID)
                REFERENCES JUser(JUserID),
                FOREIGN KEY juserevent_event_fk(EventID)
                REFERENCES Event(EventID),
                PRIMARY KEY (JUserID, EventID));
                """,
                """
                CREATE TABLE IF NOT EXISTS Team (
                TeamID int AUTO_INCREMENT NOT NULL PRIMARY KEY,
                OwnerID int,
                EventID int,
                Name text,
                FOREIGN KEY team_owner_fk(OwnerID)
                REFERENCES JUser(JUserID),
                FOREIGN KEY team_event_fk(EventID)
                REFERENCES Event(EventID));
                """,
                """
                CREATE TABLE IF NOT EXISTS TeamMembers(
                TeamID int,
                JUserID int,
                FOREIGN KEY teammembers_team_fk(TeamID)
                REFERENCES Team(TeamID),
                FOREIGN KEY teammembers_juser_fk(JUserID)
                REFERENCES JUser(JUserID),
                PRIMARY KEY (TeamID, JUserID));
                """,
                """
                CREATE TABLE IF NOT EXISTS Auth (
                JUserID int,
                JUsername text,
                Password blob,
                FOREIGN KEY auth_juser_fk(JUserID)
                REFERENCES JUser(JUserID));
                """,
                """
                CREATE TABLE IF NOT EXISTS Company (
                CompanyID int AUTO_INCREMENT PRIMARY KEY,
                Website text,
                Slack text,
                Image blob,
                Description text);
                """,
                """
                CREATE TABLE IF NOT EXISTS Opening (
                OpeningID int AUTO_INCREMENT PRIMARY KEY,
                Title text);
                """,
                """
                CREATE TABLE IF NOT EXISTS CompanyOpenings (
                CompanyID int,
                OpeningID int,
                FOREIGN KEY companyopenings_company_fk(CompanyID)
                REFERENCES Company(CompanyID),
                FOREIGN KEY companyopenings_opening_fk(OpeningID)
                REFERENCES Opening(OpeningID));
                """]
                cnxn = getConnection()
                for statement in sql:
                    with cnxn.cursor() as crsr:
                        crsr.execute(statement)
                cnxn.commit()
                cnxn.close()
                return {'message' : 'Successfully nuked database.'}
        except:
            return {'error': 500}, 500
        

@api.route('/user/<user_id>')
class User(Resource):
    @api.marshal_with(user_model)
    def get(self, user_id):
        cnxn = getConnection()
        with cnxn.cursor() as crsr:
            sql = "SELECT * FROM jumble.JUser as user INNER JOIN jumble.MajorJUser as major_tie ON user.JUserID = major_tie.JUserID INNER JOIN jumble.Major as major ON major_tie.MajorID = major.MajorID WHERE user.JUserID = %s"
            crsr.execute(sql, (user_id,))
            result = crsr.fetchone()
            cnxn.close()
            return {
                'id' : result['JUserID'],
                'name' : result['Name'],
                'email' : result['Email'],
                'major' : result['major.Name'],
                'slack' : result['Slack'],
            }, 200
        return {'error' : 500}, 500


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
        user = api.payload
        cnxn = getConnection()
        #try:
        with cnxn.cursor() as crsr:
            # Determine if the Major already Exists
            crsr.execute("SELECT MajorID FROM Major WHERE Name = %s", (user['major']))
            major = crsr.fetchone()
            if major == None:
                crsr.execute("INSERT INTO jumble.Major (Name) VALUES (%s)", (user['name']))
            cnxn.commit()
        cnxn.close()
        
        cnxn = getConnection()
        with cnxn.cursor() as crsr:
            crsr.execute("INSERT INTO jumble.JUser (Name, Email, Slack) VALUES (%s, %s, %s);", (user['name'], user['email'], user['slack']))
            cnxn.commit()
        cnxn.close()
        
        cnxn = getConnection()
        with cnxn.cursor() as crsr:
            crsr.execute("SELECT MajorID FROM Major WHERE Name = %s", (user['major']))
            major_id = crsr.fetchone()

            crsr.execute("SELECT JUserID FROM jumble.JUser WHERE Email = %s", (user['email']))
            user_id = crsr.fetchone()

            crsr.execute("INSERT INTO jumble.MajorJUser (MajorID, JUserID) VALUES (%s, %s);", (major_id['MajorID'], user_id['JUserID']))
            cnxn.commit()
        cnxn.close()

        cnxn = getConnection()
        with cnxn.cursor() as crsr:
            if 'first_hack' in user:
                crsr.execute("""UPDATE jumble.JUser SET FirstHack = %s""", (user['first_hack']))
                cnxn.commit()
        cnxn.close()

        # This is trash and needs to be fixed
        cnxn = getConnection()
        with cnxn.cursor() as crsr:
            if 'image' in user:
                crsr.execute("UPDATE jumble.JUser SET Image = ...... WHERE JUser.Email = ?", (user['image'], user['email']))
                cnxn.commit()
        cnxn.close()

        return {'successfully insert user into jumble' : 200}
        #except:
        #    return {'unable to insert user into jumble' : 500}

        #return {'message' : 'Successfully insert into DB!'}, 201

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

