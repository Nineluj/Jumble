CREATE TABLE IF NOT EXISTS User (
UserID int AUTO_INCREMENT NOT NULL PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS Major (
	MajorID int AUTO_INCREMENT NOT NULL PRIMARY KEY,
   Name text
);

CREATE TABLE IF NOT EXISTS MajorUser (
	MajorID int PRIMARY KEY,
    UserID int PRIMARY KEY,
    FOREIGN KEY major_fk(MajorID)
   REFERENCES Major(MajorID),
   FOREIGN KEY user_fk(UserID)
   REFERENCES User(UserID)
   );

CREATE TABLE IF NOT EXISTS Attributes (
   UserID int PRIMARY KEY,
   Image blob,
   Name text,
   Email text,
   Slack text,
   FOREIGN KEY user_fk(UserID)
   REFERENCES User(UserID)
);

CREATE TABLE IF NOT EXISTS Interest (
    InterestID int AUTO_INCREMENT NOT NULL PRIMARY KEY,
   Name text
);

CREATE TABLE IF NOT EXISTS Skill (
    SkillID int AUTO_INCREMENT NOT NULL PRIMARY KEY,
   Name text
);

CREATE TABLE IF NOT EXISTS UserInterests (
    UserID int,
   InterestID int,
    FOREIGN KEY interest_fk(InterestID)
   REFERENCES Interest(InterestID),
   FOREIGN KEY user_fk(UserID)
   REFERENCES User(UserID),
   PRIMARY KEY (UserID, InterestID)
);

CREATE TABLE IF NOT EXISTS UserSkill (
    UserID int,
   SkillID int,
    FOREIGN KEY user_fk(UserID)
   REFERENCES User(UserID),
    FOREIGN KEY skill_fk(SkillID)
   REFERENCES Skill(SkillID),
   PRIMARY KEY (UserID, SkillID)
);

CREATE TABLE IF NOT EXISTS Contact (
    PrimaryUserID int PRIMARY KEY,
	ContactID int,
    FOREIGN KEY pr_fk(PrimaryUserID)
   REFERENCES User(PrimaryUserID),
    FOREIGN KEY contact_fk(ContactUserID)
   REFERENCES User(ContactUserID)
);

CREATE TABLE IF NOT EXISTS Event (
    EventID int AUTO_INCREMENT NOT NULL PRIMARY KEY,
   AdminID int,
   EName text,
    FOREIGN KEY admin_fk(AdminID)
   REFERENCES User(AdminID)
);

CREATE TABLE IF NOT EXISTS UserEvent (
	UserID int,
    EventID int,
    FOREIGN KEY user_fk(UserID)
   REFERENCES User(UserID),
   FOREIGN KEY event_fk(EventID)
   REFERENCES Event(EventID),
   PRIMARY KEY (UserID, EventID)
   );

CREATE TABLE IF NOT EXISTS Team (
    TeamID int AUTO_INCREMENT NOT NULL PRIMARY KEY,
    OwnerID int,
    EventID int,
   Name text,
    FOREIGN KEY owner_fk(OwnerID)
   REFERENCES User(OwnerID),
 FOREIGN KEY event_fk(EventID)
   REFERENCES Event(EventID)
);

CREATE TABLE IF NOT EXISTS TeamMembers(
    TeamID int,
   UserID int,
    FOREIGN KEY team_fk(TeamID)
   REFERENCES Team(TeamID),
    FOREIGN KEY user_fk(UserID)
   REFERENCES User(UserID),
   PRIMARY KEY (TeamID, UserID)
);

CREATE TABLE IF NOT EXISTS Auth (
    UserID int,
   Username text,
   Password blob,
    FOREIGN KEY user_fk(UserID)
   REFERENCES User(UserID)
);