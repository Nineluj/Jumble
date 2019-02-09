DROP DATABASE IF EXISTS jumble;
CREATE DATABASE jumble;
USE jumble;

CREATE TABLE IF NOT EXISTS Major (
   MajorID int AUTO_INCREMENT NOT NULL PRIMARY KEY,
   Name text NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS JUser (
JUserID int AUTO_INCREMENT NOT NULL PRIMARY KEY,
Image blob,
Name text,
Email text,
Slack text,
FirstHack BOOLEAN
);

CREATE TABLE IF NOT EXISTS MajorJUser (
   MajorID int,
   JUserID int,
   FOREIGN KEY majorjuser_major_fk(MajorID)
REFERENCES Major(MajorID),
FOREIGN KEY majorjuser_user_fk(JUserID)
REFERENCES JUser(JUserID),
PRIMARY KEY (MajorID, JUserID));

CREATE TABLE IF NOT EXISTS Interest (
   InterestID int AUTO_INCREMENT NOT NULL PRIMARY KEY,
Name text
);

CREATE TABLE IF NOT EXISTS UserLikes (
	UserMainID int,
    UserLikedID int,
    FOREIGN KEY userlikes_usermain_fk(UserMainID)
REFERENCES JUser(JUserID),
FOREIGN KEY userlikes_userliked_fk(UserLikedID)
REFERENCES JUser(JUserID),
PRIMARY KEY (UserMainID, UserLikedID)
);

CREATE TABLE IF NOT EXISTS Idea (
   IdeaID int AUTO_INCREMENT NOT NULL PRIMARY KEY,
Name text
);

CREATE TABLE IF NOT EXISTS Skill (
   SkillID int AUTO_INCREMENT NOT NULL PRIMARY KEY,
Name text
);

CREATE TABLE IF NOT EXISTS JUserInterests (
   JUserID int,
InterestID int,
   FOREIGN KEY juserinterests_juser_fk(InterestID)
REFERENCES Interest(InterestID),
FOREIGN KEY juserinterests_interest_fk(JUserID)
REFERENCES JUser(JUserID),
PRIMARY KEY (JUserID, InterestID));

CREATE TABLE IF NOT EXISTS JUserIdeas (
   JUserID int,
IdeaID int,
   FOREIGN KEY juserideas_juser_fk(IdeaID)
REFERENCES Idea(IdeaID),
FOREIGN KEY juserideas_idea_fk(JUserID)
REFERENCES JUser(JUserID),
PRIMARY KEY (JUserID, IdeaID)
);

CREATE TABLE IF NOT EXISTS JUserSkill (
   JUserID int,
SkillID int,
   FOREIGN KEY juserskill_juser_fk(JUserID)
REFERENCES JUser(JUserID),
   FOREIGN KEY juserskill_skii_fk(SkillID)
REFERENCES Skill(SkillID),
PRIMARY KEY (JUserID, SkillID)
);

CREATE TABLE IF NOT EXISTS Contact (
   PrimaryJUserID int PRIMARY KEY,
   ContactID int,
   FOREIGN KEY contact_primary_fk(PrimaryJUserID)
REFERENCES JUser(JUserID),
   FOREIGN KEY contact_contact_fk(ContactID)
REFERENCES JUser(JUserID)
);

CREATE TABLE IF NOT EXISTS Event (
   EventID int AUTO_INCREMENT NOT NULL PRIMARY KEY,
AdminID int,
EName text,
   FOREIGN KEY event_admin_fk(AdminID)
REFERENCES JUser(JUserID));

CREATE TABLE IF NOT EXISTS JUserEvent (
   JUserID int,
   EventID int,
   FOREIGN KEY juserevent_juser_fk(JUserID)
REFERENCES JUser(JUserID),
FOREIGN KEY juserevent_event_fk(EventID)
REFERENCES Event(EventID),
PRIMARY KEY (JUserID, EventID)
);

CREATE TABLE IF NOT EXISTS Team (
   TeamID int AUTO_INCREMENT NOT NULL PRIMARY KEY,
   OwnerID int,
   EventID int,
Name text,
   FOREIGN KEY team_owner_fk(OwnerID)
REFERENCES JUser(JUserID),
FOREIGN KEY team_event_fk(EventID)
REFERENCES Event(EventID)
);

CREATE TABLE IF NOT EXISTS TeamMembers(
   TeamID int,
JUserID int,
   FOREIGN KEY teammembers_team_fk(TeamID)
REFERENCES Team(TeamID),
   FOREIGN KEY teammembers_juser_fk(JUserID)
REFERENCES JUser(JUserID),
PRIMARY KEY (TeamID, JUserID)
);

CREATE TABLE IF NOT EXISTS Auth (
   JUserID int,
JUsername text,
Password blob,
   FOREIGN KEY auth_juser_fk(JUserID)
REFERENCES JUser(JUserID)
);

CREATE TABLE IF NOT EXISTS Company (
	CompanyID int AUTO_INCREMENT PRIMARY KEY,
    Website text,
    Slack text,
    Image blob,
    Description text
    );

CREATE TABLE IF NOT EXISTS Opening (
	   OpeningID int AUTO_INCREMENT PRIMARY KEY,
      Title text
    );

CREATE TABLE IF NOT EXISTS CompanyOpenings (
	CompanyID int,
    OpeningID int,
     FOREIGN KEY companyopenings_company_fk(CompanyID)
REFERENCES Company(CompanyID),
 FOREIGN KEY companyopenings_opening_fk(OpeningID)
REFERENCES Opening(OpeningID)
);