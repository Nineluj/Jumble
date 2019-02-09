import { Component, OnInit } from '@angular/core';

import { User, SampleData } from '../userService';

@Component({
  selector: 'app-contacts',
  templateUrl: './contacts.component.html',
  styleUrls: ['./contacts.component.scss']
})
export class ContactsComponent implements OnInit {
  contacts: User[];

  constructor() {
    this.contacts = new SampleData().getContacts();
  }

  ngOnInit() {
  }

}
