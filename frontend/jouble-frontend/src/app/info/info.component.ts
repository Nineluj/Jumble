import { Component, OnInit } from '@angular/core';
import { SampleData, User } from 'app/userService';
import { CurrentCardDataService } from 'app/services/current-card-data.service';
import * as $ from 'jquery'

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
  private interests: string;
  private skills: string;
  private ideas: string;
  
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

  public updateData() {
    this.name = this.currentCardData.getFirstName();
    this.email = this.currentCardData.getEmail();
    this.major = this.currentCardData.getMajor();
    this.slack = this.currentCardData.getSlack();
  }

  updateInterests(id: number): void {
    $.ajax({
      type: 'POST',
      url: 'http://localhost:5000/api/interest/' + id,
      success: this.updateInterestsCallback
    })
  }

  updateInterestsCallback(data) {
    this.interests = data.name;
  }

  updateSkills(id: number): void {
    $.ajax({
      type: 'POST',
      url: 'http://localhost:5000/api/skills/' + id,
      success: this.updateSkillsCallback
    })
  }

  updateSkillsCallback(data) {
    this.skills = data.name;
  }

  updateIdeas(id: number): void {
    $.ajax({
      type: 'POST',
      url: 'http://localhost:5000/api/ideas/' + id,
      success: this.updateIdeasCallback
    })
  }

  updateIdeasCallback(data) {
    this.ideas = data.name;
  }

}
