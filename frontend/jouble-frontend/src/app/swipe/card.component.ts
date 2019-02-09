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


  badges = [firstTimer, pythonBadge, jsBadge, dbBadge];
}
