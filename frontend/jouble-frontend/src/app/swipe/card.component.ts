import { Component } from '@angular/core';

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
}
