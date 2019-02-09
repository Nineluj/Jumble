USE jumble;

/*
DELETE FROM MajorJUser WHERE MajorID > 0;
DELETE FROM UserLikes WHERE UserMainID > 0;
DELETE FROM JUserInterests WHERE JUserID > 0;
DELETE FROM JUserIdeas WHERE JUserID > 0;
DELETE FROM JUserSkill WHERE JUserID > 0;
DELETE FROM Contact WHERE PrimaryJUserID > 0;
DELETE FROM JUserEvent WHERE JUserID > 0;
DELETE FROM Auth WHERE JUserID > 0;

DELETE FROM JUser WHERE JUserID <> 0;
ALTER TABLE JUser AUTO_INCREMENT = 1;

DELETE FROM Major WHERE MajorID <> 0;
ALTER TABLE Major AUTO_INCREMENT = 1;

DELETE FROM Interest WHERE InterestID <> 0;
ALTER TABLE Interest AUTO_INCREMENT = 1;

DELETE FROM Idea WHERE IdeaID <> 0;
ALTER TABLE Idea AUTO_INCREMENT = 1;

DELETE FROM Skill WHERE SkillID <> 0;
ALTER TABLE Skill AUTO_INCREMENT = 1;

DELETE FROM Event WHERE EventID <> 0;
ALTER TABLE Event AUTO_INCREMENT = 1;
*/
INSERT INTO JUser (Image, Name, Email, Slack, FirstHack)
VALUES (LOAD_FILE('../../pictures/BB.jpg'), 'Barry B. Benson', 'bb123@beehive.com', 'barry_bee', FALSE),
(LOAD_FILE('../../pictures/ChadBradley.jpg'), 'Chad Bradley', 'totally@bro.com', 'lit_gainz', TRUE),
(LOAD_FILE('../../pictures/ChickenLou.jpg'), 'Chicken Louis', 'dave@chickenlous.net', 'crispy-luscious_deluxe', FALSE),
(LOAD_FILE('../../pictures/DorialBeckham.jpg'), 'Dorial Green-Beckham', 'nfllegends@retired.com', 'oops-I-did-it-again', TRUE),
(LOAD_FILE('../../pictures/JosephAoun.jpg'), 'Joseph Aoun', 'aoun.j@northeastern.edu', 'flatscreens4lyfe', FALSE),
(LOAD_FILE('../../pictures/PacoDadog.jpg'), 'Paco DaDog', 'oofboof@woof.com', 'big_bad_dog', FALSE),
(LOAD_FILE('../../pictures/SalVulcano.jpg'), 'Sal Vulcano', 'big_loser@impracticaljokers.com', 'tonights_loser', TRUE),
(LOAD_FILE('../../pictures/TonyBologna.jpg'), 'Tony Bologna', 'tony@bologna.com', 'ya_like_jazz?', FALSE);

INSERT INTO Major (Name)
VALUES ('Computer Engineering'),
 ('Computer Science'),
 ('Information Science'),
 ('Data Science'),
 ('Finance');

INSERT INTO MajorJUser (MajorID, JUserID)
VALUES (1, 1), (2, 2), (2, 3), (4, 4), (2, 5), (1, 6), (3, 7), (5, 8);

INSERT INTO Interest (Name)
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
 ('Back-End Development');

 INSERT INTO UserLikes (UserMainID, UserLikedID)
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
 (8, 6);
 
 INSERT INTO Idea (Name)
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
 ('Back-End Development');
 
 INSERT INTO Skill (Name)
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
 ('Microsoft Powerpoint');
 
 INSERT INTO JUserInterests (JUserID, InterestID)
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
 (8,8);
 
 INSERT INTO JUserIdeas (JUserID, IdeaID)
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
 (8,4);
 
 INSERT INTO JUserSkill (JUserID, SKillID)
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
 (8,7);
 
 INSERT INTO Contact (PrimaryJUserID, ContactID)
 VALUES (1,6),
 (2,4),
 (4,2),
 (6,1),
 (6,8),
 (8,6);
 
 INSERT INTO Event (AdminID, EName)
 VALUES (8, 'HackBeanpot'),
 (2, 'Fratathon');
 
 INSERT INTO JUserEvent (EventID, JUserID)
 VALUES (2, 4),
 (2, 5),
 (1,1),
 (1,3),
 (1,4),
 (1,5),
 (1,6),
 (1,7);
 
 INSERT INTO Auth (JUserID, JUsername, JPassword)
 VALUES (1, 'barryb', 1),
 (2, 'chadb', 2),
 (3, 'louisc', 3),
 (4, 'dorialgoat', 4),
 (5, 'flatscreen', 5),
 (6, 'oofboof', 6),
 (7, 'loser', 7),
 (8, 'magianos', 8);