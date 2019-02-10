import { Component, OnInit, ViewChild } from '@angular/core';
import { InfoComponent } from 'app/info/info.component';
import * as $ from 'jquery';
import { CurrentCardDataService } from 'app/services/current-card-data.service';
import { Card } from 'app/swipe/card.component';

@Component({
  selector: 'app-swipe-panel',
  templateUrl: './swipe-panel.component.html',
  styleUrls: ['./swipe-panel.component.scss']
})
export class SwipePanelComponent implements OnInit {

  @ViewChild('infoTable') infoTable: InfoComponent;
  @ViewChild('swipe') swipeCard: Card;
  constructor(private cardService: CurrentCardDataService) { 
    this.updateCard(false);
  }

  ngOnInit() {
  }

  public updateCard(bool) {
    console.log(bool);
    console.log('this gets called');
    $.ajax({
      type: 'GET',
      url: 'http://localhost:5000/api/next/9',
      success: this.getDetails
    })
  };

  public getDetails(data) {
    $.ajax({
      type: 'GET',
      url: 'http://localhost:5000/api/user/' + data.id,
      success: this.updateAll
    })

  }

  private updateAll = (user) => {

    this.cardService.setFirstName(user.name);
    this.cardService.setEmail(user.email);
    this.cardService.setMajor(user.major);
    this.cardService.setSlack(user.slack);

    //this.firstName = chosenData.name;
    $( '.card_user_info_name' )[0].textContent = user.name;
    //this.major = chosenData.major;
    $( '.card_user_major' )[0].textContent = user.major;

    //this.badges = chosenData.first_hack ? [firstTimer] : [experienced];

    $( '.card_user_picture' ).attr('src',  'data:image/png;base64,' + user.image);
    this.infoTable.updateData();
    this.infoTable.updateInterests(user.id);
    this.infoTable.updateSkills(user.id);
    this.infoTable.updateIdeas(user.id);
    this.swipeCard.updateData();
  }

}
