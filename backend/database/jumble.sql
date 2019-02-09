USE jumble;

CREATE TABLE IF NOT EXISTS JUser (
JUserID int AUTO_INCREMENT NOT NULL PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS Major (
	MajorID int AUTO_INCREMENT NOT NULL PRIMARY KEY,
   Name text
);

CREATE TABLE IF NOT EXISTS MajorJUser (
	MajorID int,
    JUserID int,
    FOREIGN KEY major_fk(MajorID)
   REFERENCES Major(MajorID),
   FOREIGN KEY Juser_fk(JUserID)
   REFERENCES JUser(JUserID),
   PRIMARY KEY (MajorID, JUserID)
   );

CREATE TABLE IF NOT EXISTS Attributes (
   JUserID int PRIMARY KEY,
   Image blob,
   Name text,
   Email text,
   Slack text,
   FOREIGN KEY Juser_fk(JUserID)
   REFERENCES JUser(JUserID)
);

CREATE TABLE IF NOT EXISTS Interest (
    InterestID int AUTO_INCREMENT NOT NULL PRIMARY KEY,
   Name text
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
    FOREIGN KEY interest_fk(InterestID)
   REFERENCES Interest(InterestID),
   FOREIGN KEY Juser_fk(JUserID)
   REFERENCES JUser(JUserID),
   PRIMARY KEY (JUserID, InterestID)
);

CREATE TABLE IF NOT EXISTS JUserIdeas (
    JUserID int,
   IdeaID int,
    FOREIGN KEY idea_fk(IdeaID)
   REFERENCES Idea(IdeaID),
   FOREIGN KEY Juser_fk(JUserID)
   REFERENCES JUser(JUserID),
   PRIMARY KEY (JUserID, IdeaID)
);

CREATE TABLE IF NOT EXISTS JUserSkill (
    JUserID int,
   SkillID int,
    FOREIGN KEY Juser_fk(JUserID)
   REFERENCES JUser(JUserID),
    FOREIGN KEY skill_fk(SkillID)
   REFERENCES Skill(SkillID),
   PRIMARY KEY (JUserID, SkillID)
);

CREATE TABLE IF NOT EXISTS Contact (
    PrimaryJUserID int PRIMARY KEY,
	ContactID int,
    FOREIGN KEY pr_fk(PrimaryJUserID)
   REFERENCES JUser(JUserID),
    FOREIGN KEY contact_fk(ContactID)
   REFERENCES JUser(JUserID)
);

CREATE TABLE IF NOT EXISTS Event (
    EventID int AUTO_INCREMENT NOT NULL PRIMARY KEY,
   AdminID int,
   EName text,
    FOREIGN KEY admin_fk(AdminID)
   REFERENCES JUser(JUserID)
);

CREATE TABLE IF NOT EXISTS JUserEvent (
	JUserID int,
    EventID int,
    FOREIGN KEY Juser_fk(JUserID)
   REFERENCES JUser(JUserID),
   FOREIGN KEY event_fk(EventID)
   REFERENCES Event(EventID),
   PRIMARY KEY (JUserID, EventID)
   );

CREATE TABLE IF NOT EXISTS Team (
    TeamID int AUTO_INCREMENT NOT NULL PRIMARY KEY,
    OwnerID int,
    EventID int,
   Name text,
    FOREIGN KEY owner_fk(OwnerID)
   REFERENCES JUser(JUserID),
 FOREIGN KEY event_fk(EventID)
   REFERENCES Event(EventID)
);

CREATE TABLE IF NOT EXISTS TeamMembers(
    TeamID int,
   JUserID int,
    FOREIGN KEY team_fk(TeamID)
   REFERENCES Team(TeamID),
    FOREIGN KEY Juser_fk(JUserID)
   REFERENCES JUser(JUserID),
   PRIMARY KEY (TeamID, JUserID)
);

CREATE TABLE IF NOT EXISTS Auth (
    JUserID int,
   JUsername text,
   Password blob,
    FOREIGN KEY Juser_fk(JUserID)
   REFERENCES JUser(JUserID)
);