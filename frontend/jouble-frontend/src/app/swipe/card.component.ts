import { Component } from '@angular/core';
import { BadgeLister } from './badge/swipe.badgeLister';
import { BadgeData } from 'app/userService';

const pythonBadge: BadgeData = {
  badgeName: 'python',
  badgeImg: '/assets/badges/python.png'
};

const jsBadge: BadgeData = {
  badgeName: 'js',
  badgeImg: '/assets/badges/javascript.png'
};

const dbBadge: BadgeData = {
  badgeName: 'js',
  badgeImg: '/assets/badges/database.png'
};

const firstTimer: BadgeData = {
  badgeName: 'first',
  badgeImg: '/assets/badges/experienced.png'
};

const java: BadgeData = {
  badgeName: 'java',
  badgeImg: '/assets/badges/java.png'
};

const racket: BadgeData = {
  badgeName: 'racket',
  badgeImg: '/assets/badges/racket.png'
};

const design: BadgeData = {
  badgeName: 'design',
  badgeImg: '/assets/badges/design.png'
};

@Component({
  selector: 'swipe_card',
  templateUrl: './card.component.html',
  styleUrls: ['./card.component.scss']
})
export class Card {
  title = 'card_module';
  imgpath = '../../assets/user.jpg';
  firstName = 'Alex';
  lastName = 'Tapley';
  major = 'Computer Engineering';


  badges = [firstTimer, design, java, pythonBadge, jsBadge, dbBadge, racket];
}
