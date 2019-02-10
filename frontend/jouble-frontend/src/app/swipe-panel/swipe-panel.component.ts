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
      url: 'http://localhost:5000/api/users',
      success: this.updateAll
    })};

  private updateAll = (data) => {
    const pick = Math.floor(Math.random() * 5) + 1;

    const chosenData = data[pick];

    this.cardService.setFirstName(chosenData.name);
    this.cardService.setEmail(chosenData.email);
    this.cardService.setMajor(chosenData.major);
    this.cardService.setSlack(chosenData.slack);

    //this.firstName = chosenData.name;
    $( '.card_user_info_name' )[0].textContent = chosenData.name;
    //this.major = chosenData.major;
    $( '.card_user_major' )[0].textContent = chosenData.major;

    //this.badges = chosenData.first_hack ? [firstTimer] : [experienced];

    $( '.card_user_picture' ).attr('src',  'data:image/png;base64,' + chosenData.image);
    this.infoTable.updateData();
    this.swipeCard.updateData();
  }

}
