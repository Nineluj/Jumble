USE jumble;

DELETE FROM MajorJUser WHERE MajorID > 0;

DELETE FROM JUser WHERE JUserID <> 0;
ALTER TABLE JUser AUTO_INCREMENT = 1;

DELETE FROM Major WHERE MajorID <> 0;
ALTER TABLE Major AUTO_INCREMENT = 1;

DELETE FROM Interest WHERE InterestID <> 0;
ALTER TABLE Interest AUTO_INCREMENT = 1;

INSERT INTO JUser (Image, Name, Email, Slack, FirstHack)
VALUES (LOAD_FILE('/Users/alex_tapley/Desktop/teamgitboost-beanpot/pictures/BB.jpg'), 'Barry B. Benson', 'bb123@beehive.com', 'barry_bee', 0),
(LOAD_FILE('../../pictures/ChadBradley.jpg'), 'Chad Bradley', 'totally@bro.com', 'lit_gainz', 1),
(LOAD_FILE('../../pictures/ChickenLou.jpg'), 'Chicken Louis', 'dave@chickenlous.net', 'crispy-luscious_deluxe', 0),
(LOAD_FILE('../../pictures/DorialBeckham.jpg'), 'Dorial Green-Beckham', 'nfllegends@retired.com', 'oops-I-did-it-again', 1),
(LOAD_FILE('../../pictures/JosephAoun.jpg'), 'Joseph Aoun', 'aoun.j@northeastern.edu', 'flatscreens4lyfe', 0),
(LOAD_FILE('../../pictures/PacoDadog.jpg'), 'Paco DaDog', 'oofboof@woof.com', 'big_bad_dog', 0),
(LOAD_FILE('../../pictures/SalVulcano.jpg'), 'Sal Vulcano', 'big_loser@impracticaljokers.com', 'tonights_loser', 1),
(LOAD_FILE('../../pictures/TonyBologna.jpg'), 'Tony Bologna', 'tony@bologna.com', 'ya_like_jazz?', 0);

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
 
 