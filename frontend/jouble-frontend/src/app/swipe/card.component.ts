import { Component } from '@angular/core';
import { BadgeLister } from './badge/swipe.badgeLister';
import { BadgeData } from 'app/userService';

import * as $ from 'jquery';

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
  imgpath = '';
  firstName = '';
  lastName = '';
  major = '';

  badges = [firstTimer, design, java, pythonBadge, jsBadge, dbBadge, racket];


  constructor() {
    this.updateCard(false);
  }

  loadNewCard(data) {
    const firstData = data[0];

    this.firstName = firstData.name;
    $( '.card_user_info_name' )[0].textContent = firstData.name;
    this.major = firstData.major;
    $( '.card_user_major' )[0].textContent = firstData.major;

    $( '.card_user_picture' ).attr('src',  'data:image/png;base64,' + firstData.image);
  }

  updateCard(bool) {
    console.log(bool);
    console.log('this gets called');
    $.ajax({
      type: 'GET',
      url: 'http://localhost:5000/api/users',
      success: this.loadNewCard
    });

    return 0;
  }
}
