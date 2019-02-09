import { Component, OnInit } from '@angular/core';
import { SampleData, User } from 'app/userService';
import { CurrentCardDataService } from 'app/services/current-card-data.service';

@Component({
  selector: 'app-info',
  templateUrl: './info.component.html',
  styleUrls: ['./info.component.scss']
})
export class InfoComponent implements OnInit {

  private name: string;
  private email: string;
  private major: string;
  private slack: string;
  
  private contacts: User[];
  constructor(private currentCardData: CurrentCardDataService) { 
    this.contacts = new SampleData().getContacts();
  }

  ngOnInit() {
    this.name = this.currentCardData.getFirstName();//this.contacts[0].firstName;
    this.email = this.currentCardData.getEmail();//"email@email.com";
    this.major = this.currentCardData.getMajor();//"CE - TEST";
    this.slack = this.currentCardData.getSlack();//this.contacts[0].slackUsername;
  }

}
