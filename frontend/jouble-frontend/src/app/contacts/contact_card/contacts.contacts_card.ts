import { Component, Input, OnInit } from '@angular/core';
import { User } from '../../userService';

@Component({
  selector: 'contacts-card',
  templateUrl: './contacts.contacts_card.html',
  styleUrls: ['./contacts.contacts_card.scss']
})
export class ContactsCardComponent implements OnInit {
  @Input() contact: User;

  constructor() {
  }

  ngOnInit() {
  }
}
