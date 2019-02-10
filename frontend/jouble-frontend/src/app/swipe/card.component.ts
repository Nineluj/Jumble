import { Component, ViewChild } from '@angular/core';
import { BadgeLister } from './badge/swipe.badgeLister';
import { BadgeData } from 'app/userService';

import * as $ from 'jquery';
import { CurrentCardDataService } from 'app/services/current-card-data.service';
import { InfoComponent } from 'app/info/info.component';

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
  badgeImg: '/assets/badges/firsttimer.png'
};

const experienced: BadgeData = {
  badgeName: 'experienced',
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

  badges: BadgeData[];

  // badges = [firstTimer, design, java, pythonBadge, jsBadge, dbBadge, racket];
  constructor(private cardService: CurrentCardDataService) {
    //this.updateCard(false);
  }

  private loadNewCard = (data) => {
    const pick = Math.floor(Math.random() * 5) + 1;

    const chosenData = data[pick];

    this.cardService.setFirstName(chosenData.name);
    this.firstName = chosenData.name;
    $( '.card_user_info_name' )[0].textContent = chosenData.name;
    this.major = chosenData.major;
    $( '.card_user_major' )[0].textContent = chosenData.major;

    this.badges = chosenData.first_hack ? [firstTimer] : [experienced];

    $( '.card_user_picture' ).attr('src',  'data:image/png;base64,' + chosenData.image);

  }

  updateData(): void {
    this.firstName = this.cardService.getFirstName();
    console.log(this.firstName)
    this.major = this.cardService.getMajor();
    console.log(this.major)
    //this.badges = chosenData.first_hack ? [firstTimer] : [experienced];
  }

  // public updateCard(bool) {
  //   console.log(bool);
  //   console.log('this gets called');
  //   $.ajax({
  //     type: 'GET',
  //     url: 'http://localhost:5000/api/users',
  //     success: this.loadNewCard
  //   });

  //   return 0;
  // }
}
