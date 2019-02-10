from flask import render_template, redirect, url_for, flash, request
from flask_restplus import fields, Api, Resource, marshal, marshal_with
import marshmallow
from app.api import bp
from app.api import api
import pymysql.cursors
import requests
import time
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

UPLOAD_FOLDER = dir_path + '/user-uploads/'

def getConnection():
    return pymysql.connect(
            host='localhost',
            user='root',
            password='tapley4656',
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
        'first_hack': fields.Boolean,
        'image': fields.String
    }
)

user_id_model = api.model('User',
    {
        'id': fields.Integer
    }
)

user_model_post = api.model('User', 
    {
        'name' : fields.String,
        'email' : fields.String,
        'major' : fields.String,
        'slack' : fields.String,
        'first_hack': fields.Boolean,
        'image': fields.String
    }
)

event_model_list = api.model('Event', 
    {
        'id' : fields.Integer,
        'name' : fields.String,
        'admin' : fields.Nested(user_model),
        'attendies' : fields.List(fields.Nested(user_model))
    }
)

interest_model = api.model('Interest', 
    {
        'id' : fields.Integer,
        'name' : fields.String
    }
)

interest_model_post = api.model('Interest', 
    {
        'interestID' : fields.Integer,
        'name' : fields.String
    }
)

major_model = api.model('Major', 
    {
        'id' : fields.Integer,
        'name' : fields.String
    }
)

idea_model = api.model('Idea', 
    {
        'id' : fields.Integer,
        'name' : fields.String
    }
)

skill_model = api.model('Skill',
    {
        'id' : fields.Integer,
        'name' : fields.String
    }
)

event_model = api.model('Event',
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
                Image text,
                Name text,
                Email text,
                Slack text,
                FirstHack BOOLEAN);
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
                CREATE TABLE IF NOT EXISTS UserLikes (
	            UserMainID int,
                UserLikedID int,
                FOREIGN KEY userlikes_usermain_fk(UserMainID)
                REFERENCES JUser(JUserID),
                FOREIGN KEY userlikes_userliked_fk(UserLikedID)
                REFERENCES JUser(JUserID),
                PRIMARY KEY (UserMainID, UserLikedID)
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS UserDislikes (
	            UserMainID int,
                UserDislikedID int,
                FOREIGN KEY userdislikes_usermain_fk(UserMainID)
	            REFERENCES JUser(JUserID),
	            FOREIGN KEY userdislikes_userdisliked_fk(UserDislikedID)
	            REFERENCES JUser(JUserID),
	            PRIMARY KEY (UserMainID, UserDislikedID)
                );
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
                PrimaryJUserID int,
                ContactID int,
                FOREIGN KEY contact_primary_fk(PrimaryJUserID)
                REFERENCES JUser(JUserID),
                FOREIGN KEY contact_contact_fk(ContactID)
                REFERENCES JUser(JUserID),
                PRIMARY KEY (PrimaryJUserID, ContactID)
                );
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
                JPassword blob,
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
                for statement in sql:
                    with cnxn.cursor() as crsr:
                        crsr.execute(statement)
                cnxn.commit()
                cnxn.close()
                return {'message' : 'Successfully nuked database.'}
        except:
            return {'error': 500}, 500
        
@api.route('/fill')
class Fill(Resource):
    def get(self):
        r = requests.get('http://localhost:5000/api/wipe')
        if r.status_code == 200:
            cnxn = getConnection()
            try:
                with cnxn.cursor() as crsr:
                    sql = ["""USE jumble;""",

                            """INSERT INTO JUser (Image, Name, Email, Slack, FirstHack)
                            VALUES ('bb64', 'Barry B. Benson', 'bb123@beehive.com', 'barry_bee', FALSE),
                            ('chadbradley64', 'Chad Bradley', 'totally@bro.com', 'lit_gainz', TRUE),
                            ('chickenlous64', 'Chicken Louis', 'dave@chickenlous.net', 'crispy-luscious_deluxe', FALSE),
                            ('dorialbeckham64', 'Dorial Green-Beckham', 'nfllegends@retired.com', 'oops-I-did-it-again', TRUE),
                            ('josephaoun64', 'Joseph Aoun', 'aoun.j@northeastern.edu', 'flatscreens4lyfe', FALSE),
                            ('pacodadog64', 'Paco DaDog', 'oofboof@woof.com', 'big_bad_dog', FALSE),
                            ('salvulcano64', 'Sal Vulcano', 'big_loser@impracticaljokers.com', 'tonights_loser', TRUE),
                            ('tonybologna64', 'Tony Bologna', 'tony@bologna.com', 'ya_like_jazz?', FALSE);""",

                            """INSERT INTO Major (Name)
                            VALUES ('Computer Engineering'),
                            ('Computer Science'),
                            ('Information Science'),
                            ('Data Science'),
                            ('Finance');""",

                            """INSERT INTO MajorJUser (MajorID, JUserID)
                            VALUES (1, 1), (2, 2), (2, 3), (4, 4), (2, 5), (1, 6), (3, 7), (5, 8);""",

                            """INSERT INTO Interest (Name)
                            VALUES ('Green Engineering'),
                            ('Animals'),
                            ('Music'),
                            ('Sports'),
                            ('Partying'),
                            ('Game Design'),
                            ('Food'),
                            ('Robotics'),
                            ('Entertainment'),
                            ('Education'),
                            ('Machine Learning'),
                            ('Artificial Intelligence'),
                            ('Web Development'),
                            ('Back-End Development');""",

                            """INSERT INTO UserLikes (UserMainID, UserLikedID)
                            VALUES (1, 6),
                            (1, 8),
                            (2, 4),
                            (2, 8),
                            (3, 6),
                            (4, 2),
                            (4, 5),
                            (5, 1),
                            (5, 3),
                            (6, 1),
                            (6, 8),
                            (7, 1),
                            (7, 5),
                            (8, 3),
                            (8, 6);""",

                            """
                            INSERT INTO UserDislikes (UserMainID, UserDislikedID)
                            VALUES (1, 5),
                            (1, 7),
                            (2, 3),
                            (2, 7),
                            (3, 5),
                            (4, 1),
                            (4, 3),
                            (5, 6),
                            (5, 2),
                            (6, 2),
                            (6, 7),
                            (8, 2),
                            (8, 7);
                            """,
        
                            """INSERT INTO Idea (Name)
                            VALUES ('Green Engineering'),
                            ('Animals'),
                            ('Music'),
                            ('Sports'),
                            ('Partying'),
                            ('Game Design'),
                            ('Food'),
                            ('Robotics'),
                            ('Entertainment'),
                            ('Education'),
                            ('Machine Learning'),
                            ('Artificial Intelligence'),
                            ('Web Development'),
                            ('Back-End Development');""",
        
                            """INSERT INTO Skill (Name)
                            VALUES ('Python'),
                            ('Java'),
                            ('Node.js'),
                            ('Angular.js'),
                            ('SQL'),
                            ('Tensorflow'),
                            ('C++'),
                            ('Arduino'),
                            ('HTML'),
                            ('Microsoft Word'),
                            ('Microsoft Powerpoint');""",
                            
                            """INSERT INTO JUserInterests (JUserID, InterestID)
                            VALUES (1, 1),
                            (1,2),
                            (1,3),
                            (2,3),
                            (2,4),
                            (2,5),
                            (2,6),
                            (3,7),
                            (3,8),
                            (4,4),
                            (4,5),
                            (5,9),
                            (5,10),
                            (6,7),
                            (6,2),
                            (7,13),
                            (7,9),
                            (8,12),
                            (8,11),
                            (8,8);""",
        
                            """INSERT INTO JUserIdeas (JUserID, IdeaID)
                            VALUES (1,1),
                            (1,8),
                            (3,2),
                            (3, 12),
                            (4, 4),
                            (4, 5),
                            (5, 1),
                            (5, 2),
                            (5,3),
                            (5,4),
                            (5,5),
                            (5,6),
                            (5,7),
                            (5,8),
                            (5,9),
                            (5,10),
                            (6,4),
                            (6,2),
                            (7, 13),
                            (7,12),
                            (8,11),
                            (8,12),
                            (8,4);""",
        
                            """INSERT INTO JUserSkill (JUserID, SKillID)
                            VALUES (1,1),
                            (1,8),
                            (2,10),
                            (2,11),
                            (4,7),
                            (4,5),
                            (5,1),
                            (5,2),
                            (5,3),
                            (5,4),
                            (5,6),
                            (5,7),
                            (5,8),
                            (5,9),
                            (6,9),
                            (6,4),
                            (7,3),
                            (7,4),
                            (8,1),
                            (8,2),
                            (8,7);""",
        
                            """INSERT INTO Contact (PrimaryJUserID, ContactID)
                            VALUES (1,6),
                            (2,4),
                            (4,2),
                            (6,1),
                            (6,8),
                            (8,6);""",
        
                            """INSERT INTO Event (AdminID, EName)
                            VALUES (8, 'HackBeanpot'),
                            (2, 'Fratathon');""",
        
                            """INSERT INTO JUserEvent (EventID, JUserID)
                            VALUES (2, 4),
                            (2, 5),
                            (1,1),
                            (1,3),
                            (1,4),
                            (1,5),
                            (1,6),
                            (1,7);""",
        
                            """INSERT INTO Auth (JUserID, JUsername, JPassword)
                            VALUES (1, 'barryb', 1),
                            (2, 'chadb', 2),
                            (3, 'louisc', 3),
                            (4, 'dorialgoat', 4),
                            (5, 'flatscreen', 5),
                            (6, 'oofboof', 6),
                            (7, 'loser', 7),
                            (8, 'magianos', 8);"""]
                for statement in sql:
                    with cnxn.cursor() as crsr:
                        crsr.execute(statement)
                cnxn.commit()
                cnxn.close()
                return {'message' : 'Successfully filled database.'}
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

# Get data regarding this JUser
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

# Get all interests for all users
@api.route('/interests')
class Interests(Resource):
    @api.marshal_list_with(interest_model)
    def get(self):
        list_of_interests = []
        cnxn = getConnection()
        with cnxn.cursor() as crsr:
            sql = "SELECT * FROM Interest;"
            crsr.execute(sql)
            result = crsr.fetchall()
            for interest in result:
                list_of_interests.append({
                    'id' : interest['InterestID'],
                    'name' : interest['Name'],
                })
        cnxn.close()
        return list_of_interests, 200

@api.route('/interest/<user_id>')
class GetUserInterest(Resource):
    @api.marshal_with(interest_model_post)
    def post(self, user_id):
        list_of_interests = []
        cnxn = getConnection()
        with cnxn.cursor() as crsr:
            sql = "SELECT Interest.InterestID, Interest.Name from Interest INNER JOIN JUserInterests ON Interest.InterestID = JUserInterests.InterestID INNER JOIN JUser ON JUser.JUserID = JUserInterests.JUserID WHERE JUser.JUserID = %s"
            crsr.execute(sql, (user_id,))
            result = crsr.fetchall()
            cnxn.close()
            for interest in result:
                list_of_interests.append({
                'interestID' : interest['InterestID'],
                'name' : interest['Name'],
            })
        return list_of_interests, 200


# Get all majors for all users
@api.route('/majors')
class Major(Resource):
    @api.marshal_list_with(major_model)
    def get(self):
        list_of_majors = []
        cnxn = getConnection()
        with cnxn.cursor() as crsr:
            sql = "SELECT * FROM Major;"
            crsr.execute(sql)
            result = crsr.fetchall()
            for major in result:
                list_of_majors.append({
                    'id' : major['MajorID'],
                    'name' : major['Name'],
                })
        cnxn.close()
        return list_of_majors, 200

# Gets all ideas for all users
@api.route('/ideas')
class Ideas(Resource):
    @api.marshal_list_with(idea_model)
    def get(self):
        list_of_ideas = []
        cnxn = getConnection()
        with cnxn.cursor() as crsr:
            sql = "SELECT * FROM Idea;"
            crsr.execute(sql)
            result = crsr.fetchall()
            for idea in result:
                list_of_ideas.append({
                    'id' : idea['IdeaID'],
                    'name' : idea['Name'],
                })
        cnxn.close()
        return list_of_ideas, 200

# Get all skills for all users
@api.route('/skills')
class Skills(Resource):
    @api.marshal_list_with(skill_model)
    def get(self):
        list_of_skills = []
        cnxn = getConnection()
        with cnxn.cursor() as crsr:
            sql = "SELECT * FROM Skill;"
            crsr.execute(sql)
            result = crsr.fetchall()
            for skill in result:
                list_of_skills.append({
                    'id' : skill['SkillID'],
                    'name' : skill['Name'],
                })
        cnxn.close()
        return list_of_skills, 200

# Get all events for all users
@api.route('/events')
class Events(Resource):
    @api.marshal_list_with(event_model)
    def get(self):
        list_of_events = []
        cnxn = getConnection()
        with cnxn.cursor() as crsr:
            sql = "SELECT * FROM Event;"
            crsr.execute(sql)
            result = crsr.fetchall()
            for event in result:
                list_of_events.append({
                    'id' : event['EventID'],
                    'name' : event['EName'],
                })
        cnxn.close()
        return list_of_events, 200

@api.route('/events/<user_id>')
class GetUserEvents(Resource):

    # Returns the events a given user is registered for.
    @api.marshal_list_with(event_model)
    def get(self, user_id):
        try:
            list_of_events = []
            sql = "SELECT * FROM Event INNER JOIN JUserEvent ON Event.EventID = JUserEvent.EventID WHERE JUserID = %s"
            cnxn = getConnection()
            with cnxn.cursor() as crsr:
                crsr.execute(sql, (user_id))
                result = crsr.fetchall()
                for event in result:
                    list_of_events.append(
                        {
                            'id' : event['EventID'],
                            'name' : event['EName'],
                        }
                    )
            cnxn.commit()
            cnxn.close()
            return list_of_events, 200
        except:
            return {'error' : 500}, 500


@api.route('/users')
class Users(Resource):
    @api.marshal_list_with(user_model)
    def get(self):
        list_of_users = []
        cnxn = getConnection()
        with cnxn.cursor() as crsr:
            sql = "SELECT * FROM jumble.JUser as user INNER JOIN jumble.MajorJUser as major_tie ON user.JUserID = major_tie.JUserID INNER JOIN jumble.Major as major ON major_tie.MajorID = major.MajorID"
            crsr.execute(sql)
            result = crsr.fetchall()
            for user in result:
                # Get image data (it's in base64)
                f = open(UPLOAD_FOLDER + user['Image'], "r")

                list_of_users.append({
                    'id' : user['JUserID'],
                    'name' : user['Name'],
                    'email' : user['Email'],
                    'major' : user['major.Name'],
                    'slack' : user['Slack'],
                    'first_hack': user['FirstHack'],
                    'image' : f.read()
                })

                f.close()
        cnxn.close()
        return list_of_users, 200
    
    @api.expect(user_model_post)
    def post(self):
        user = api.payload
        cnxn = getConnection()

        try:
            with cnxn.cursor() as crsr:
                # Determine if the Major already Exists
                crsr.execute("SELECT MajorID FROM Major WHERE Name = %s", (user['major']))
                major = crsr.fetchone()
                if major == None:
                    crsr.execute("INSERT INTO jumble.Major (Name) VALUES (%s)", (user['major']))
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
                    print("asserting that shit")
                    file_name = str(int(time.time()*10**7))
                    f = open(UPLOAD_FOLDER + file_name, "w+")
                    f.write(user['image'])
                    f.close()

                    crsr.execute("UPDATE jumble.JUser SET Image = %s WHERE JUser.Email = %s", (file_name, user['email']))
                    cnxn.commit()
            cnxn.close()

            return {'successfully insert user into jumble': 200}
        except Exception as e:
            import traceback
            traceback.print_last()
            return {'unable to insert user into jumble ' + str(e): 500}

@api.route('/event/<event_id>')
class Event(Resource):
    @api.marshal_with(event_model_list)
    def get(self, event_id):
        try:
            sql = "SELECT * FROM Event INNER JOIN JUserEvent ON Event.EventID = JUserEvent.EventID INNER JOIN JUser ON JUserEvent.JUserID = JUser.JUserID INNER JOIN MajorJUser ON MajorJUser.JUserID = JUserEvent.JUserID INNER JOIN Major ON Major.MajorID = MajorJUser.MajorID WHERE Event.EventID = %s"
            cnxn = getConnection()
            crsr = cnxn.cursor()
            crsr.execute(sql, (event_id))
            result = crsr.fetchall()
            cnxn.close()

            list_of_attendies = []
            for atendee in result:
                list_of_attendies.append({
                    'id' : atendee['JUser.JUserID'],
                    'name' : atendee['Name'],
                    'email' : atendee['Email'],
                    'major' : atendee['Name'],
                    'slack' : atendee['Slack'],
                    'first_hack' : atendee['FirstHack']
                })

            sql = "SELECT * FROM Event INNER JOIN JUser ON JUser.JUserID = Event.AdminID JOIN MajorJUser ON MajorJUser.JUserID = JUser.JUserID INNER JOIN Major ON Major.MajorID = MajorJUser.MajorID WHERE Event.EventID = %s"
            cnxn = getConnection()
            crsr = cnxn.cursor()
            crsr.execute(sql, (event_id))
            result_admin = crsr.fetchone()
            cnxn.close()

            return {
                'id' : result_admin['EventID'],
                'name' : result_admin['EName'],
                'admin' : {
                                'id' : result_admin['AdminID'],
                                'name' : result_admin['Name'],
                                'email' : result_admin['Email'],
                                'major' : result_admin['Name'],
                                'slack' : result_admin['Slack'],
                                'first_hack' : atendee['FirstHack']
                            },
                'attendies' : list_of_attendies
            }, 200
        except:
            return {"error": 500}, 500

    # Add the a user to the given event.
    @api.expect(user_id_model)
    def post(self, event_id):
        try:
            user_id = api.payload['id']
            sql = "INSERT INTO JUserEvent VALUES (" + str(user_id) + ", " + str(event_id) + ")"
            cnxn = getConnection()
            with cnxn.cursor() as crsr:
                crsr.execute(sql)
            cnxn.commit()
            cnxn.close()
            return {"Message": "We added user: " + str(user_id) + " to the event: " + str(event_id)}, 200
        except:
            return {"Message": "We COULD NOT add user: " + str(user_id) + " to the event: " + str(event_id)}, 500